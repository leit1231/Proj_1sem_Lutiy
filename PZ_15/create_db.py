# 2
import sqlite3 as sq

def create_db():
    with sq.connect('opt_base.db') as con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS tovar 
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR,
            description VARCHAR,
            unit VARCHAR
            )""")
        cur.execute("""CREATE TABLE IF NOT EXISTS market 
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title VARCHAR,
            adress VARCHAR,
            number VARCHAR
            )""")
        cur.execute("""CREATE TABLE IF NOT EXISTS store_applications 
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            application_date DATE,
            id_market INTEGER,
            FOREIGN KEY (id_market) REFERENCES market(id) ON DELETE CASCADE ON UPDATE CASCADE
            )""")
        cur.execute("""CREATE TABLE IF NOT EXISTS number_stock 
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quantity INTEGER,
            id_tovar INTEGER,
            FOREIGN KEY (id_tovar) REFERENCES tovar(id) ON DELETE CASCADE ON UPDATE CASCADE
            )""")
        cur.execute("""CREATE TABLE IF NOT EXISTS compound 
        (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            quantity INTEGER,
            id_tovar INTEGER,
            id_appl INTEGER,
            FOREIGN KEY (id_tovar) REFERENCES tovar(id) ON DELETE CASCADE ON UPDATE CASCADE,
            FOREIGN KEY (id_appl) REFERENCES store_applications(id) ON DELETE CASCADE ON UPDATE CASCADE
            )""")

def filling_table():
    info_tovar = [
        (1, 'Молоко', 'Молоко парное, высокой жирности', 'литры'),
        (2, 'Морквовь', 'Сладкая морковка', 'килограммы'),
        (3, 'Капуста', 'Сладкая, хрустящая капуста', 'килограммы'),
        (4, 'Мука', 'Мука высшего сорта', 'упаковки'),
        (5, 'Свекла', 'Сладкая вкусная свекла', 'килограммы'),
        (6, 'Творог', 'Натуральный творог', 'килограммы'),
        (7, 'Йогурт', 'Персиковый йогурт', 'упаковки'),
        (8, 'Колбаса', 'Докторская колбаса', 'упаковки'),
        (9, 'Сыр', 'Сливочный сыр', 'килограммы'),
        (10, 'Хлеб', 'Свежий хлеб', 'штуки')
    ]
    info_market = [
        (1, 'Светофор', 'ул.Большая Садовая, 43', '+7(800)-555-35-35'),
        (2, 'Магнит', 'пл.К Маркса, 12', '+7(904)-335-35-35'),
        (3, 'Ашан', 'ул.Ленина, 205-а', '+7(850)-505-45-35'),
        (4, 'Фасоль', 'Ворошиловский пр., 105 е', '+7(800)-455-39-95'),
        (5, 'Пятёрочка', 'ул. Зоологическая, 30', '+7(910)-985-11-55'),
        (6, 'КБ', 'Змиевский пр-д, 16', '+7(878)-904-88-09'),
        (7, 'Эдельвейс', 'ул. Страны Советов, 19', '+7(878)-228-78-78'),
        (8, 'Гофманшоп', 'ул. Лелюшенко, 4', '+7(928)-123-45-67'),
        (9, 'Перекрёсток', 'ул. Добровольского, 30', '+7(850)-643-87-98'),
        (10, 'Лента', 'Пойменная ул., 1', '+7(900)-213-67-05')
    ]
    info_store_applications = [
        (1,'2023-03-12', 7),
        (2, '2023-07-22', 8),
        (3, '2023-09-30',10),
        (4, '2023-10-21',3),
        (5,'2023-03-15',1),
        (6,'2023-02-19',9),
        (7,'2023-09-30',4),
        (8,'2023-11-27',2),
        (9,'2023-12-31',6),
        (10,'2023-09-30',5)
    ]
    info_number_stock = [
        (1,100,5),
        (2,78,7),
        (3,54,8),
        (4,0,1),
        (5,123,6),
        (6,76,3),
        (7,23,2),
        (8,90,4),
        (9,67,10),
        (10,99,9)
    ]
    info_compound = [
        (1,30,6, 2),
        (2,13,9, 4),
        (3,45,7, 6),
        (4,87,8, 9),
        (5,95,1, 7),
        (6,33,3, 8),
        (7,56,2, 10),
        (8,76,4, 3),
        (9,77,4, 5),
        (10,12,10, 1)
    ]
    with sq.connect('opt_base.db') as con:
        cur = con.cursor()
        cur.executemany("INSERT INTO tovar VALUES (?, ?, ?, ?)", info_tovar)
        cur.executemany("INSERT INTO market VALUES (?, ?, ?, ?)", info_market)
        cur.executemany("INSERT INTO store_applications VALUES (?, ?, ?)", info_store_applications)
        cur.executemany("INSERT INTO number_stock VALUES (?, ?, ?)", info_number_stock)
        cur.executemany("INSERT INTO compound VALUES (?, ?, ?, ?)", info_compound)
