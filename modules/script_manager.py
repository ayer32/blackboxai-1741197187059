import os

SCRIPTS_DIR = "scripts"

def create_script(script_name, content):
    """Create a new script file with the given content."""
    if not os.path.exists(SCRIPTS_DIR):
        os.makedirs(SCRIPTS_DIR)
    
    script_path = os.path.join(SCRIPTS_DIR, f"{script_name}.py")
    with open(script_path, 'w') as file:
        file.write(content)
    
    return f"Script '{script_name}' created successfully."

def list_scripts():
    """List all available scripts."""
    if not os.path.exists(SCRIPTS_DIR):
        return []
    
    return [f for f in os.listdir(SCRIPTS_DIR) if f.endswith('.py')]

def load_script(script_name):
    """Load the content of a script."""
    script_path = os.path.join(SCRIPTS_DIR, f"{script_name}.py")
    if not os.path.exists(script_path):
        return None
    
    with open(script_path, 'r') as file:
        return file.read()

def execute_script(script_name):
    """Execute a script."""
    script_path = os.path.join(SCRIPTS_DIR, f"{script_name}.py")
    if not os.path.exists(script_path):
        return "Script not found."
    
    exec(open(script_path).read())
    return f"Script '{script_name}' executed successfully."

# Example usage
if __name__ == "__main__":
    print(create_script("example_script", "print('Hello, World!')"))
    print(list_scripts())
    print(load_script("example_script"))
    print(execute_script("example_script"))
