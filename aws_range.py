import pymysql
def powder(data):
    k=data.split('-')
    x=k[0]
    z=k[1]

    connect = pymysql.connect(
                host="database-1.cfmudpl0e2d7.ap-south-1.rds.amazonaws.com",
                user="admin",
                passwd = "bharath**",
                 db = "transction_prod"
    )
    cursor= connect.cursor()

    w = "select * from transction where product_id between "+ str(x) +" and "+ str(z) +""
    #w="select * from employeenames where id >= '" + str(x) +"' and id <= '" + str(z) +"'"
    print(w)
    cursor.execute(w)
    bha = cursor.fetchall()


    li=[]
    for i in bha:

        m={"product_id":i[0],"product_name":i[1],"amount":i[2],"mobile":i[3]}

        li.append(m)

    return li

