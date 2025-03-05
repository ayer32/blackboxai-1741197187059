import subprocess

def run_sqlmap(target_url):
    command = ['python', 'path/to/sqlmap/sqlmap.py', '-u', target_url, '--batch']
    result = subprocess.run(command, capture_output=True, text=True)
    return result.stdout
