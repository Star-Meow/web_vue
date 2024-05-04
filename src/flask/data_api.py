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
        for i in result['q_ans']:
            if i == result['q_ans'][-1]:
                q_ans = q_ans + str(i)
            else:
                q_ans = q_ans + ',' + str(i)
        try:
            cursor.execute("INSERT INTO form_ans (id, gender, old, trygame, q_ans, t_ans1, t_ans2) VALUES(?,?,?,?,?,?,?)",(result['ID'], result['gender'], result['old'], result['trygame'], q_ans, result['ans'][0], result['ans'][1]))
            connection.commit()
            print(result['ID'], result['gender'], result['old'], result['trygame'], q_ans, result['ans'][0], result['ans'][1])
            print("成功送出")
        except sqlite3.Error as e:
            print(f"插入错误: {e}")

#      # 提交更改
