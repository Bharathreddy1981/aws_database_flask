import pymysql
def salt():

    z = pymysql.connect(
        host="database-1.cfmudpl0e2d7.ap-south-1.rds.amazonaws.com",
        user="admin",
        passwd = "bharath**",
        db = "transction_prod"
    )
    y = z.cursor()
    w = "select * from transction"
    y.execute(w)
    bha = y.fetchall()

    return bha

