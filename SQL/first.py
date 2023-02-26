import sqlite3 as sq

with sq.connect('test.db') as con:
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
                id INTEGER, 
                full_name INTEGER,
                salary INTEGER, 
                position TEXT,
                rating INTEGER
                )""")
    # cur.execute("DROP TABLE users")
    # cur.execute("UPDATE users SET position = 'Разработчик' WHERE id = 1")



    
    def add_staff():
        print('Заполните следующие поля.')
        id = input('id: ')
        full_name = input('Полное имя: ')
        salary = input('Зарплата: ')
        position = input('Должность: ')
        rating = input('Коф. успешности: ')
        
        cur.execute("INSERT INTO users VALUES({0}, '{1}', {2}, '{3}', {4})".format(id, full_name, salary, position, rating))
        



    def get_by_id():
        id = input('Введите id сотрудника: ')
        cur.execute("SELECT full_name, salary, position, rating FROM users WHERE id = {0}".format(id))
        for result in cur:
            print(f'''
full_name - {result[0]}
salary - {result[1]}
position - {result[2]}
rating - {result[3]}
''')




    def del_staff ():
        del_id = input('Введите id сотрудника: ')
        cur.execute('DELETE FROM users WHERE id = {0}'.format(del_id))




    def get_best_staff():
        cur.execute('SELECT full_name, salary, position, rating FROM users WHERE rating > 50')
        for res in cur:
            print(f'''
full_name - {res[0]}
rating - {res[3]}
''')




    def add_bonus():
        cur.execute('UPDATE users SET salary = salary*1.2 WHERE rating > 50')
    
    # add_staff()      # Новый сотрудник
    # get_by_id()      # Информация по id
    # del_staff()      # Удаление сотрудника
    # get_best_staff() # Рейтинг выше 50
    # add_bonus()      # +20% зарплаты
