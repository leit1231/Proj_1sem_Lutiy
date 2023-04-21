import sqlite3 as sq

def req_sel():
    with sq.connect('opt_base.db') as con:
        cur = con.cursor()
        #1
        cur.execute("SELECT title, description FROM tovar")
        result = cur.fetchall()
        print(result)
        #2
        cur.execute("SELECT title, adress FROM market")
        result = cur.fetchall()
        print(result)
        #3
        cur.execute("SELECT id, application_date FROM store_applications")
        result = cur.fetchall()
        print(result)
        #4
        cur.execute("SELECT tovar.title, number_stock.quantity FROM tovar INNER JOIN number_stock ON tovar.id = number_stock.id_tovar")
        result = cur.fetchall()
        print(result)
        #5
        cur.execute("SELECT tovar.title, number_stock.quantity FROM tovar INNER JOIN number_stock ON tovar.id = number_stock.id_tovar ORDER BY quantity DESC")
        result = cur.fetchall()
        print(result)
        #6
        cur.execute("SELECT compound.id_appl, tovar.title FROM tovar INNER JOIN compound ON tovar.id = compound.id_tovar ORDER BY id_appl")
        result = cur.fetchall()
        print(result)
        #7
        cur.execute("SELECT tovar.title, number_stock.quantity FROM tovar INNER JOIN number_stock ON tovar.id = number_stock.id_tovar WHERE quantity < 70")
        result = cur.fetchall()
        print(result)
        #8
        cur.execute("SELECT store_applications.id, market.title, store_applications.application_date FROM market INNER JOIN store_applications ON market.id = store_applications.id_market WHERE application_date = '2023-09-30' ")
        result = cur.fetchall()
        print(result)
        #9
        cur.execute("SELECT compound.quantity, market.title FROM market INNER JOIN store_applications ON market.id = store_applications.id_market INNER JOIN compound ON store_applications.id = compound.id_appl WHERE quantity<70")
        result = cur.fetchall()
        print(result)

def req_upd():
    with sq.connect('opt_base.db') as con:
        cur = con.cursor()
        #1
        # cur.execute("UPDATE number_stock SET quantity = 50 WHERE id=4")
        #2
        # cur.execute("UPDATE tovar SET title='Докторская колбаса' WHERE id=8")
        #3
        # cur.execute("UPDATE compound SET quantity=78 WHERE id=2")
        #4
        # cur.execute("UPDATE market SET adress='ул. Аксайская, 6/1' WHERE id = 1")
        #5
        # cur.execute("UPDATE store_applications SET application_date='2023-09-06' WHERE id_market=9")
        #6
        # cur.execute("UPDATE number_stock SET quantity = 123 WHERE id<5")
def req_del():
    with sq.connect('opt_base.db') as con:
        cur = con.cursor()
        #1
        # cur.execute("DELETE FROM store_applications WHERE id = 6")
        # 2
        # cur.execute("DELETE FROM number_stock WHERE id_tovar NOT IN (SELECT id_tovar FROM compound)")
        # 3
        # cur.execute("DELETE FROM store_applications WHERE id_market in (SELECT id FROM market WHERE adress LIKE 'ул.Ленина%')")
        # 4
        # cur.execute("DELETE FROM compound WHERE id_tovar IN (SELECT id_tovar FROM number_stock WHERE quantity = 0)")
        # 5
        # cur.execute("DELETE FROM market WHERE id in (SELECT id_market FROM store_applications WHERE application_date > '2023-09-30')")
        # 6
        # cur.execute("DELETE FROM compound WHERE id in (SELECT id FROM number_stock WHERE quantity = 0)")
        # 7
        # cur.execute("DELETE FROM number_stock WHERE quantity = 0")
        # 8
        # cur.execute("DELETE FROM compound WHERE id_appl in (SELECT id FROM store_applications WHERE application_date > '2023-09-30')")


# req_upd()
# req_del()