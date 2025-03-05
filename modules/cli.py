import argparse
from gui import start_application, perform_network_scan, analyze_logs, generate_report
from modules.sqlmap_integration import run_sqlmap

def main():
    parser = argparse.ArgumentParser(description='NetManEthics CLI')
    subparsers = parser.add_subparsers(dest='command')

    # Command to start the application
    start_parser = subparsers.add_parser('start', help='Start the NetManEthics application')

    # Command to perform a network scan
    scan_parser = subparsers.add_parser('scan', help='Perform a network scan')
    scan_parser.add_argument('--ip', type=str, help='IP address or range to scan')

    # Command to analyze logs
    log_parser = subparsers.add_parser('analyze_logs', help='Analyze logs')
    log_parser.add_argument('--log_file', type=str, help='Path to the log file')

    # Command to generate a report
    report_parser = subparsers.add_parser('generate_report', help='Generate a report')
    report_parser.add_argument('--report_type', type=str, help='Type of report to generate')

    # Command to run SQLMap
    sqlmap_parser = subparsers.add_parser('sqlmap', help='Run SQLMap against a target URL')
    sqlmap_parser.add_argument('--url', type=str, required=True, help='Target URL for SQLMap')

    args = parser.parse_args()

    if args.command == 'start':
        start_application()
    elif args.command == 'scan':
        if args.ip:
            perform_network_scan(args.ip)
        else:
            print("Please provide an IP address or range to scan.")
    elif args.command == 'analyze_logs':
        if args.log_file:
            analyze_logs(args.log_file)
        else:
            print("Please provide the path to the log file.")
    elif args.command == 'generate_report':
        if args.report_type:
            generate_report(args.report_type)
        else:
            print("Please specify the type of report to generate.")
    elif args.command == 'sqlmap':
        if args.url:
            output = run_sqlmap(args.url)
            print(output)
        else:
            print("Please provide a target URL for SQLMap.")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()
