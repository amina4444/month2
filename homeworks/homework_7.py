import sqlite3
from os import name
from pprint import pprint


def create_table(conn):
    conn.execute("DROP TABLE IF EXISTS students")
    conn.execute("""
    CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    author TEXT,
    publication_year INTEGER,
    genre TEXT,
    number_of_pages INTEGER,
    number_of_copies INTEGER
    )
    """)
def insert_books(conn, name, author, publication_year, genre, number_of_pages, number_of_copies):
    conn.execute("""
    INSERT INTO books (name, author, publication_year, genre, number_of_pages, number_of_copies)
    VALUES (?,?,?,?,?,?) """,
    (name, author, publication_year, genre, number_of_pages, number_of_copies)
    )
    conn.commit()

def get_books_by_author(conn,author):
    result = conn.execute("SELECT * FROM books WHERE author = ? ORDER BY name ASC", (author,))
    return result.fetchall()

if __name__ == "__main__":
    connection = sqlite3.connect('books.db')
    create_table(conn=connection)
    insert_books(connection,"Клатбище домашних животных","Стивен Кинг", 1983,"horror",400,243434 )
    insert_books(connection,'Преступление и наказание', 'Фёдор Достоевский', 1866, 'Классика', 576, 10)
    insert_books(connection,'1984', 'Джордж Оруэлл', 1949, 'Антиутопия', 320, 25 )
    insert_books(connection,'Маленький принц', 'Антуан де Сент-Экзюпери', 1943, 'Сказка', 96, 50 )
    insert_books(connection,'Гарри Поттер и философский камень', 'Дж.К. Роулинг', 1997, 'Фэнтези', 309, 100 )
    insert_books(connection, 'Дюна', 'Фрэнк Герберт', 1965, 'Научная фантастика', 600, 20)
    insert_books(connection, 'Великий Гэтсби', 'Фрэнсис Скотт Фицджеральд', 1925, 'Роман', 180, 8)
    insert_books(connection,'Алхимик', 'Пауло Коэльо', 1988, 'Притча', 160, 40 )
    insert_books(connection, 'Sapiens: Краткая история человечества', 'Юваль Ной Харари', 2011, 'Научпоп', 512, 30)
    insert_books(connection, 'Мастер и Маргарита', 'Михаил Булгаков', 1967, 'Роман', 480, 15)


    books_by_author = get_books_by_author(conn=connection,author='Стивен Кинг')
    pprint(books_by_author)

    connection.close()

