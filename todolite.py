import sqlite3

if __name__ == '__main__':

    sql = "SELECT id, todo FROM task WHERE urgent=1"

    conn = sqlite3.connect("todolist.db")

    cursor = conn.cursor()
    cursor.execute(sql)

    results = cursor.fetchall()

    # print results

    for row in results:
        print "Todo: %s" % row[1]

    conn.close()