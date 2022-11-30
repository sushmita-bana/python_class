import csv,pymysql
sql_conn=pymysql.connect(user='root',password='sushmit@saatvik2204',host='localhost',database='emp_info')
sql_cu=sql_conn.cursor()
#sql_cu.execute('create table personal_info_ph_7 (name varchar(25),age varchar(25),pnone_no varchar(20),city varchar(25))')
#sql_cu.execute('create table personal_info_ph_8 (name varchar(25),age varchar(25),pnone_no varchar(20),city varchar(25))')
#sql_cu.execute('create table personal_info_ph_9 (name varchar(25),age varchar(25),pnone_no varchar(20),city varchar(25))')
with open('emp_info.csv','r') as a:
    b=csv.reader(a)
    c=list(b)
    #ph_7=[]
    #ph_8=[]
    #ph_9=[]
    for column in range(1,len(c)):
        d=c[column]
        
        for i in d[2]:
            if i[0]=='7':
                #ph_7.append(d)
                
                sql_cu.execute("insert into personal_info_ph_7 (name,age,pnone_no,city) values('%s','%s','%s','%s')"%(d[0],d[1],d[2],d[3]))
                pass
                break
            elif i[0]=='8':
                #ph_8.append(d)
                sql_cu.execute("insert into personal_info_ph_8 (name,age,pnone_no,city) values('%s','%s','%s','%s')"%(d[0],d[1],d[2],d[3]))
                break
            else:
                #ph_9.append(d)
                sql_cu.execute("insert into personal_info_ph_9 (name,age,pnone_no,city) values('%s','%s','%s','%s')"%(d[0],d[1],d[2],d[3]))
                break
   
   
sql_conn.commit()
sql_conn.close()
