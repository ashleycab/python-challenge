import csv
from collections import defaultdict
from typing import Dict, List, Tuple
import os
 
def analyze_election_data(input_file: str) -> Tuple[int, Dict[str, int], str]:
    total_votes = 0
    candidate_votes = defaultdict(int)
 
    try:
        with open(input_file, 'r') as election_file:
            csv_reader = csv.reader(election_file)
            next(csv_reader)  # Skip the header row
 
            for vote in csv_reader:
                total_votes += 1
                candidate = vote[2]  # Assuming candidate name is in the third column
                candidate_votes[candidate] += 1
 
        if not candidate_votes:
            raise ValueError("No valid data found in the CSV file")
 
        winner = max(candidate_votes, key=candidate_votes.get)
        return total_votes, dict(candidate_votes), winner
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except IndexError:
        print("Error: The CSV file does not have the expected structure.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
 
    return None  # Return None if any error occurs
 
def generate_election_report(total_votes: int, candidate_votes: Dict[str, int], winner: str) -> List[str]:
    report_lines = [
        "Election Results",
        "-------------------------",
        f"Total Votes: {total_votes}",
        "-------------------------"
    ]
 
    for candidate, votes in candidate_votes.items():
        percentage = (votes / total_votes) * 100
        report_lines.append(f"{candidate}: {percentage:.3f}% ({votes})")
 
    report_lines.extend([
        "-------------------------",
        f"Winner: {winner}",
        "-------------------------"
    ])
 
    return report_lines
 
def save_and_print_report(report: List[str], output_file: str) -> None:
    for line in report:
        print(line)
 
    with open(output_file, 'w') as file:
        file.write('\n'.join(report))
 
def main():
    # Define file paths using os.path.join for cross-platform compatibility
    base_path = os.path.dirname(os.path.abspath(__file__))
    input_csv = os.path.join(base_path, "Resources", "election_data.csv")
    output_txt = os.path.join(base_path, "analysis", "election_results.txt")
 
    # Ensure the analysis directory exists
    os.makedirs(os.path.dirname(output_txt), exist_ok=True)
 
    # Analyze election data
    result = analyze_election_data(input_csv)
    if result is None:
        print("Failed to analyze election data. Please check the error messages above.")
        return
 
    total_votes, candidate_votes, winner = result
 
    # Generate report
    report = generate_election_report(total_votes, candidate_votes, winner)
 
    # Save and print results
    save_and_print_report(report, output_txt)
    print(f"\nElection analysis results saved to: {output_txt}")
 
if __name__ == "__main__":
    main()