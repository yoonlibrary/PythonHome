import pymysql

host = '3.38.181.127'         #EC2 인스턴스 IPv4 주소
port = 3306
user = 'root'
password = 'pythonmysql'
database = 'mycompany'
conn = pymysql.connect(port=port, user=user,                            # keyword argument는 순서가 바뀌어도 됨
                       host=host, password=password, database=database)

cursor = conn.cursor()
sql = "SELECT EMPNO, ENAME, JOB, SAL, DEPTNO FROM EMP WHERE DEPTNO = 20"
cursor.execute(sql)
results = cursor.fetchall()
for emp in results :        #emp : 단수로 뽑아
    print(emp[1], emp[3], sep=',\t')                  #sep : 여러 개의 값을 동시에 뽑을 때
cursor.close()
conn.close()