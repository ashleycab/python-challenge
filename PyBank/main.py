# Import necessary modules
import csv
from typing import List, Tuple
import os
 
def analyze_financial_data(input_file: str) -> Tuple[int, int, float, Tuple[str, int], Tuple[str, int]]:
    # Initialize variables to store financial data
    total_months = 0
    net_total = 0
    prev_profit_loss = None
    changes = []
    greatest_increase = ("", 0)
    greatest_decrease = ("", 0)
 
    try:
        # Open and read the CSV file
        with open(input_file, 'r') as financial_file:
            csv_reader = csv.reader(financial_file)
            next(csv_reader)  # Skip the header row
 
            # Process each row in the CSV file
            for row in csv_reader:
                date = row[0]
                profit_loss = int(row[1])
 
                # Update total months and net total
                total_months += 1
                net_total += profit_loss
 
                # Calculate and track changes in profit/loss
                if prev_profit_loss is not None:
                    change = profit_loss - prev_profit_loss
                    changes.append(change)
 
                    # Update greatest increase and decrease
                    if change > greatest_increase[1]:
                        greatest_increase = (date, change)
                    if change < greatest_decrease[1]:
                        greatest_decrease = (date, change)
 
                prev_profit_loss = profit_loss
 
        # Calculate average change
        average_change = sum(changes) / len(changes) if changes else 0
 
        # Return the calculated financial data
        return total_months, net_total, average_change, greatest_increase, greatest_decrease
 
    # Handle potential errors
    except FileNotFoundError:
        print(f"Error: The file {input_file} was not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
 
    return None
 
def generate_financial_report(total_months: int, net_total: int, average_change: float, 
                              greatest_increase: Tuple[str, int], greatest_decrease: Tuple[str, int]) -> List[str]:
    # Create a formatted report with the financial analysis results
    report_lines = [
        "Financial Analysis",
        "----------------------------",
        f"Total Months: {total_months}",
        f"Total: ${net_total}",
        f"Average Change: ${average_change:.2f}",
        f"Greatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})",
        f"Greatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})"
    ]
    return report_lines
 
def save_and_print_report(report: List[str], output_file: str) -> None:
    # Print the report to the console
    for line in report:
        print(line)
 
    # Save the report to a text file
    with open(output_file, 'w') as file:
        file.write('\n'.join(report))
 
def main():
    # Set up file paths
    base_path = os.path.dirname(os.path.abspath(__file__))
    input_csv = os.path.join(base_path, "Resources", "budget_data.csv")
    output_txt = os.path.join(base_path, "analysis", "financial_analysis.txt")
 
    # Ensure the output directory exists
    os.makedirs(os.path.dirname(output_txt), exist_ok=True)
 
    # Analyze the financial data
    result = analyze_financial_data(input_csv)
    if result is None:
        print("Failed to analyze financial data. Please check the error messages above.")
        return
 
    # Unpack the analysis results
    total_months, net_total, average_change, greatest_increase, greatest_decrease = result
 
    # Generate the financial report
    report = generate_financial_report(total_months, net_total, average_change, greatest_increase, greatest_decrease)
 
    # Save and print the report
    save_and_print_report(report, output_txt)
    print(f"\nFinancial analysis results saved to: {output_txt}")
 
# Execute the main function if this script is run directly
if __name__ == "__main__":
    main()