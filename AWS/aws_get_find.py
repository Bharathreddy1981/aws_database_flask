import pymysql
def bat(value):
    get_value=value
    connect = pymysql.connect(
                host="database-1.cfmudpl0e2d7.ap-south-1.rds.amazonaws.com",
                user="admin",
                passwd = "bharath**",
                 db = "transction_prod"
    )
    cursor= connect.cursor()
    w = "select * from transction where product_id='"+ str(get_value) +"'"
    cursor.execute(w)
    bha = cursor.fetchall()


    for i in bha:
        k={"product_id":i[0],"product_name":i[1]," amount":i[2],"mobile":i[3]}


    return k


