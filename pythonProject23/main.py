# database.py
import sqlite3

DATABASE_NAME = "warehouse.db"


def initialize_db():
    """
    Создаёт таблицу категорий, если она ещё не существует.
    """
    try:
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS categories (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    description TEXT
                )
            ''')
            conn.commit()
    except sqlite3.Error as err:
        print(f"Ошибка инициализации БД: {err}")


def create_category(name, description=None):
    """
    Добавляет новую категорию в базу данных.

    Параметры:
      name: Название категории (строка, не пустая).
      description: Описание категории (строка, может быть пустой).

    Возвращает:
      id добавленной записи или None в случае ошибки.
    """
    name = name.strip()
    if not name:
        return None

    try:
        with sqlite3.connect(DATABASE_NAME) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO categories (name, description) VALUES (?, ?)",
                (name, description)
            )
            conn.commit()
            return cursor.lastrowid
    except sqlite3.Error as err:
        print(f"Ошибка при добавлении категории: {err}")
        return None


# Инициализация БД при запуске модуля
if __name__ == "__main__":
    initialize_db()