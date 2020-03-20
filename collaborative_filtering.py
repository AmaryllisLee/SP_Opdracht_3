import psycopg2


c = psycopg2.connect("dbname=huwbbackupdb user=postgres password=amaryllis")
cur = c.cursor()

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


