#Dit bestand is gebruikt om verschillende code te proberen

'''
def fetch_query(query):
    lst = []
    cur.execute(query)
    records = cur.fetchall()
    for i in records:
        return i
    cur.close()
'''


'''
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
    c.commit()
    cur.close()

'''

'''
-- top 3 combination category and brand that users has previously_viewed
Select distinct  category, brand,count(*) 
from profiles_previously_viewed,products 
where prodid = products.id
Group by category, brand 
Order by count(*) DESC
limit 3;

---result:
--Baby & kind , Pampers
--Gezond & verzorging, schwarzkopf
-- Gezond & verzorging , Gillete
'''

'''
select distinct  prodid , count(*)
from profiles_previously_viewed,products
where prodid = products.id
And category = 'Baby & kind' And brand = 'Pampers'
group by profiles_previously_viewed.prodid
Order by count(*) DESC;

'''

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

'''
#def collaborative_filtering(profilid):
query = 'select segment from profiles where id = \'5a3a3d91ed295900010450d2\';'
cur.execute(query)
records = cur.fetchall()
for el in records:
    for seg in el:
        print(seg)

#Select ids die dezelfde segment heeft als profilid
query2 = "select id from profiles where segment = '{}';".format(seg)
cur.execute(query2)
res = cur.fetchmany(size=4)
print(res)


profile_list = []
for i in res:
    for j in i:
        profile_list.append(j)
        continue
print(profile_list)

rec_prod_id = []
for prof_id in profile_list:
    query3 = 'select prodid from profiles_previously_viewed where profid =\'{}\''.format(prof_id)
    cur.execute(query3)
    res2 = cur.fetchall()
    for result in res2:
        for prod in result:
            rec_prod_id.append(prod)
print(rec_prod_id)
'''
