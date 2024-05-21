import sqlite3, random, datetime
from time import sleep

db_config = {
    'database': 'form.db' 
}

def tryconnection():
    global connection, cursor
    while True:
        try:
            connection = sqlite3.connect(**db_config)
            cursor = connection.cursor()

            print("成功連接至DB！")
            break
        except sqlite3.Error as e:
            print(f"連接錯誤: {e}")
            print("reconneciton...")
            sleep(5)


def inputdb(result):
    tryconnection()
    if result:
        q_ans = ''
        sum = [0]*3
        for index, i in enumerate(result['q_ans']): 
            if index == len(result['q_ans'])-1:
                q_ans = q_ans + str(i)
            else:
                q_ans = q_ans  + str(i) + ','

            if index < 5:
                sum[0] = int(sum[0])+i
            elif 5 < index < 10:
                sum[1] = int(sum[1])+i
            elif 10 < index < 15:
                sum[2] = int(sum[2])+i

        x = sum.index(max(sum))
        tp = ''
        if x == 0:
            tp = 'M'
        elif x == 1:
            tp = 'A'
        elif x == 2:
            tp = 'D'
        print(x)
        print(tp)
        try:
            cursor.execute("INSERT INTO form_ans (id, gender, old, trygame, q_ans, t_ans1, t_ans2, type) VALUES(?,?,?,?,?,?,?,?)",(result['ID'], result['gender'], result['old'], result['trygame'], q_ans, result['ans'][0], result['ans'][1], tp))
            connection.commit()
            print(result['ID'], result['gender'], result['old'], result['trygame'], q_ans, result['ans'][0], result['ans'][1],tp)
            print("成功送出")
        except sqlite3.Error as e:
            print(f"插入错误: {e}")

def MAD():
    tryconnection()
    TYPES = ['M', 'A', 'D']
    connection = sqlite3.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT type, COUNT(*) FROM form_ans GROUP BY type")
    result = cursor.fetchall()
    print()

    stats = {t: 0 for t in TYPES}


    for row in result:
        if row[0] in stats:
            stats[row[0]] = row[1]

    m = cursor.execute("SELECT * FROM form_ans WHERE type = ?", ("M",))
    ans = m.fetchall()
    t = ''
    c = 0
    
    lst = []
    for i,j in enumerate(ans):
        sc = 0
        t = ans[i][4]
        t = t.split(",")
        for k in range(5):
            sc += int(t[k])

    
        data = {
        "id": ans[i][0],
        "score": sc
        }
        lst.append(data)
        c +=1
    print(c)
        
    connection.close()
    return stats,lst