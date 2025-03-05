import subprocess

def add_firewall_rule(rule):
    """Add a firewall rule using iptables."""
    try:
        subprocess.run(['iptables'] + rule.split(), check=True)
        return "Rule added successfully."
    except subprocess.CalledProcessError as e:
        return f"Error adding rule: {e}"

def remove_firewall_rule(rule):
    """Remove a firewall rule using iptables."""
    try:
        subprocess.run(['iptables', '-D'] + rule.split(), check=True)
        return "Rule removed successfully."
    except subprocess.CalledProcessError as e:
        return f"Error removing rule: {e}"

def list_firewall_rules():
    """List current firewall rules."""
    try:
        output = subprocess.check_output(['iptables', '-L'], universal_newlines=True)
        return output
    except subprocess.CalledProcessError as e:
        return f"Error listing rules: {e}"

# Example usage
if __name__ == "__main__":
    print(list_firewall_rules())  # List current rules
    print(add_firewall_rule("-A INPUT -p tcp --dport 80 -j ACCEPT"))  # Example to add rule
    print(remove_firewall_rule("-A INPUT -p tcp --dport 80 -j ACCEPT"))  # Example to remove rule
