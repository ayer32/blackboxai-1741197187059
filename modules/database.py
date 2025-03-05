import sqlite3

class Database:
    def __init__(self, db_name='netmanethics.db'):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.create_tables()

    def create_tables(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS scans (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                target TEXT NOT NULL,
                result TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS incidents (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                incident_type TEXT NOT NULL,
                description TEXT NOT NULL,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.connection.commit()

    def insert_scan(self, target, result):
        self.cursor.execute('INSERT INTO scans (target, result) VALUES (?, ?)', (target, result))
        self.connection.commit()

    def insert_incident(self, incident_type, description):
        self.cursor.execute('INSERT INTO incidents (incident_type, description) VALUES (?, ?)', (incident_type, description))
        self.connection.commit()

    def get_scans(self):
        self.cursor.execute('SELECT * FROM scans')
        return self.cursor.fetchall()

    def get_incidents(self):
        self.cursor.execute('SELECT * FROM incidents')
        return self.cursor.fetchall()

    def close(self):
        self.connection.close()

# Example usage
if __name__ == "__main__":
    db = Database()
    db.insert_scan("192.168.1.1", "Scan result here")
    print(db.get_scans())
    db.close()
