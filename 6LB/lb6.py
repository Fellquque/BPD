import sqlite3

def bd_students():
    conn = sqlite3.connect(':memory:')
    db = conn.cursor()
    db.execute('CREATE TABLE students (st_id INTEGER, name TEXT, faculty TEXT, rating REAL)')

    students_data = [
        (2004, 'Миколай Якушин', 'ІТ', 98.5),
        (2005, 'Андрій Мельник', 'ІТ', 74.2),
        (2006, 'Тетяна Мороз', 'Економіка', 89.1),
        (2007, 'Надія Дідух', 'Менеджмент', 91.4)
    ]
    db.executemany('INSERT INTO students VALUES (?,?,?,?)', students_data)

    print("="*50)
    print("        База данних студентів        ")
    print("="*50)
    print(" Оберіть необхідний модуль для роботи:                      ")
    print(" > [raw]   - Модуль прямого пошуку                          ")
    print(" > [safe]  - Модуль захищеної фільтрації                    ")
    print(" > [exit]  - Завершити сеанс зв'язку                        ")
    print("="*50)

    while True:
        action = input("\nВкажіть назву модуля: ").strip().lower()

        if action == 'raw':
            search_term = input("Введіть ПІБ студента: ")
            sql_query = "SELECT * FROM students WHERE name = '" + search_term + "'"

            print(f"\n[SQL ЗАПИТ]: {sql_query}")
            
            try:
                rows = db.execute(sql_query).fetchall()
                if rows:
                    print("-" * 60)
                    for r in rows: print(f"ID: {r[0]} | ПІБ: {r[1]} | Ф-т: {r[2]} | Рейтинг: {r[3]}")
                else: print("Інформація за вказаними критеріями відсутня.")
            except Exception as e:
                print(f"ПОМИЛКА СИНТАКСИСУ SQL: {e}")

        elif action == 'safe':
            search_term = input("Введіть ПІБ студента (Protected Mode): ")

            print(f"\n[SAFE SQL]: SELECT * FROM students WHERE name = ?")
            print(f"[ПАРАМЕТР]: '{search_term}'")
            
            rows = db.execute("SELECT * FROM students WHERE name = ?", (search_term,)).fetchall()
            if rows:
                print("-" * 60)
                for r in rows: print(f"ID: {r[0]} | ПІБ: {r[1]} | Ф-т: {r[2]} | Рейтинг: {r[3]}")
            else: print("Результатів не знайдено (Доступ заблоковано системою захисту).")

        elif action == 'exit':
            print("До побачення!"); break
        else:
            print(f"Модуль '{action}' не знайдено. Будь ласка, введіть 'raw', 'safe' або 'exit'.")

if __name__ == "__main__":
    bd_students()