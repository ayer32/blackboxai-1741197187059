import os

def analyze_logs(log_file):
    """Analyze the specified log file and return relevant information."""
    if not os.path.exists(log_file):
        return f"Log file {log_file} does not exist."

    analysis_results = []
    with open(log_file, 'r') as file:
        for line in file:
            # Example analysis: Check for error messages
            if "ERROR" in line:
                analysis_results.append(line.strip())
    
    return analysis_results

# Example usage
if __name__ == "__main__":
    log_file = "path/to/logfile.log"  # Example log file path
    results = analyze_logs(log_file)
    print("Analysis Results:")
    for result in results:
        print(result)
