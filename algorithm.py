import psycopg2

c = psycopg2.connect("dbname=huwbbackupdb user=postgres password=amaryllis")
cur = c.cursor()


def fetch_query(query):
    lst = []
    cur.execute(query)
    records = cur.fetchall()
    for i in records:
        return i
def contant_based(profilid):

    query = 'select prodid from profiles_previously_viewed where profid = {};'.format(profilid)
    prodid= fetch_query(query)

    for id in prodid:
        query2 = 'select category,brand from products where id = \'{}\';'.format()
        cat_brand = fetch_query(query2)
   # print(cat_brand)
    query3= 'select id from products where category = \'{}\' and brand=\'{}\''.format(cat_brand[0],cat_brand[1])
    cur.execute(query3)
    prod_ids = cur.fetchmany(size=4)
    print(id, cat_brand,prod_ids)

    for i in prod_ids:
        print(i)
#query om de data toe te voegen in tabel recommendation
    #cur.execute("Insert into recommendation  values ('{}','{}','{}','{}','{}','{}','{}')").format(profilid, cat_brand[0],cat_brand[1],prod_ids[0][0],prod_ids[1][0],prod_ids[2][0],prod_ids[3][0])

    print('Inserted')



profilid= "'5a39f402ed295900010413d3'"
profilid2 = "'5a394b78ed295900010396a5'"
contant_based(profilid2)


