
import pymysql
def bus(data,num):
    name=data["product_name"]

    amount=data["amount"]

    id=num

    z = pymysql.connect(
        host="database-1.cfmudpl0e2d7.ap-south-1.rds.amazonaws.com",
        user="admin",
        passwd = "bharath**",
        db = "transction_prod"
        )
    y = z.cursor()

    w="update transction set product_name='"+str(name)+"', amount='"+str(amount)+"' where product_id='"+str(id)+"'"
    y.execute(w)

    z.commit()
    return data


