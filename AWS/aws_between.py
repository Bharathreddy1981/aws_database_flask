
import pymysql
def mirchi(num,value):
    k=value.split('-')
    x=k[0]
    z=k[1]

    a=num.split('-')
    m=a[0]
    n=a[1]

    connect = pymysql.connect(
                host="database-1.cfmudpl0e2d7.ap-south-1.rds.amazonaws.com",
                user="admin",
                passwd = "bharath**",
                 db = "transction_prod"
    )
    cursor= connect.cursor()

    w = "select * from transction where product_id between "+ str(m) +" and "+ str(n) +" and mobile between "+ str(x) +" and "+ str(z) +""


    #w="select * from employeenames where id >= '" + str(x) +"' and id <= '" + str(z) +"'"

    print(w)
    cursor.execute(w)
    bha = cursor.fetchall()
    li = []
    for i in bha:
        k={"product_id":i[0],"product_name":i[1],"amount":i[2],"mobile":i[3]}

        li.append(k)

    return li

