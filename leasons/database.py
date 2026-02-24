import sqlite3

def create_tables(conn):
    conn.execute("DROP TABLE IF EXISTS students")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS students (
      student_id INTEGER PRIMARY KEY AUTOINCREMENT,
      name TEXT,
      age INTEGER,
      city TEXT
    )
    """)
def add_student(conn,name, age, city):
    conn.execute("""
    INSERT INTO students(name,age,city) VALUES
    (?,?,?)
    """,
    (name, age, city)
    )
    conn.commit()



if __name__ == "__main__":
    connection = sqlite3.connect("database.db")
    create_tables(connection)
    add_student(connection, "igor", 30, 'bishkek')
    add_student(connection, "james", 40, 'kang')
    connection.close()
