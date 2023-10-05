import pymysql

# 1. Connect (참고 : host는 EC2 인스턴스 IPv4 주소)

conn, cursor = None, None
try : 
    conn = pymysql.connect(host='3.38.181.127', port=3306, user='root', password='pythonmysql')
    
# 2. cursor (conn이라는 세션에 cursor라는 버스가 왔다갔다 하는 형태)
    cursor = conn.cursor()
# 3. SQL Statement
    sql = "SELECT NOW()"
    cursor.execute(sql)
# 4. fetch
    result = cursor.fetchone()
    print(result)
except Exception as err:
    print(err)
finally :
# 5. close
    cursor.close()
    conn.close()