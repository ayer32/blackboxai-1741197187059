# Setup Instructions for NetManEthics

## Development Environment Setup

### 1. Install Prerequisites
- **Python**: Ensure you have Python installed. Download it from [python.org](https://www.python.org/downloads/).
- **Git**: Install Git from [git-scm.com](https://git-scm.com/downloads/).

### 2. Clone the Repository
Open your terminal (Command Prompt or PowerShell) and run the following command to clone the repository:
```bash
git clone https://github.com/yourusername/NetManEthics.git
cd NetManEthics
```

### 3. Set Up a Virtual Environment (Optional but Recommended)
Create a virtual environment to manage dependencies:
```bash
python -m venv venv
```
Activate the virtual environment:
```bash
.\venv\Scripts\activate
```

### 4. Install Required Libraries
Run the following command to install the necessary libraries:
```bash
pip install scapy tkinter nmap paramiko matplotlib
```

### 5. Database Configuration
#### 1. Install SQLite
SQLite is included with Python's standard library, so you typically don't need to install it separately.

#### 2. Create the Database File
Create a new SQLite database file:
```bash
touch netmanethics.db
```

#### 3. Update `database.py`
Ensure that the `modules/database.py` file is set up to connect to the SQLite database. Example:
```python
import sqlite3

class Database:
    def __init__(self, db_name='netmanethics.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            )
        ''')
        self.connection.commit()

    def close(self):
        self.connection.close()
```

#### 4. Initialize the Database
Create an instance of the `Database` class in `main.py`:
```python
from modules.database import Database

def main():
    db = Database()  # This will create the database and tables if they don't exist
    db.close()  # Close the database connection when done
```

#### 5. Run the Application
Run your application:
```bash
python main.py
```

#### 6. Verify Database Creation
Use a SQLite browser or run:
```bash
sqlite3 netmanethics.db
.tables
```

### 6. Open the Project in VSCode
- Launch Visual Studio Code.
- Open the cloned project folder (`NetManEthics`) in VSCode.

### 7. Configure the Project
- Ensure that the Python interpreter is set to the virtual environment you created.

### 8. Run the Application
To run the application, execute the following command in the terminal:
```bash
python main.py
```

### 9. Running Tests (Optional)
To run the tests, you can use the following command:
```bash
python -m unittest discover -s tests
```

### 10. Create a .gitignore File
If you haven't already, create a `.gitignore` file in your project directory to exclude unnecessary files. Add the following lines:
```
__pycache__/
*.pyc
*.pyo
*.pyd
*.db
*.log
venv/
```

### 11. Commit Your Changes
After making changes to your project, you can commit them using:
```bash
git add .
git commit -m "Your commit message"
```

### Conclusion
You have now set up and configured the NetManEthics project on your local Windows machine using VSCode. If you encounter any issues or need further assistance, please refer to the documentation or reach out for help.
