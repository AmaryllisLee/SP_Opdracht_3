import psycopg2

#Connect to SQL dabase
c = psycopg2.connect("dbname=huwbbackupdb user=postgres password=amaryllis")




def fetch_query(conn, query):
    'Execute query and return result'
    cur = conn.cursor()
    cur.execute(query)
    fetched = cur.fetchall()
    cur.close()
    try:
        return fetched
    except:
        print('Query does not exist')


def content_filtering():
    'Generate 4 product_id based on set rules for recommendation'

#Queries that needs to

    create_table = '''
    --Query to drop and create table content-filtering
    Drop table if exists content_filtering ;
    
    Create table content_filtering(
    product_id varchar
    ) ; '''

    top_cat_brand = '''
    -- top 3 combination category and brand that users has previously_viewed
    Select distinct  category, brand,count(*) 
    from profiles_previously_viewed,products 
    where prodid = products.id
    Group by category, brand 
    Order by count(*) DESC
    limit 1;
    '''

    query_prod_ids = '''
         select distinct  prodid , count(*)
         from profiles_previously_viewed,products
         where prodid = products.id
         And category = '{}' And brand = '{}'
         group by profiles_previously_viewed.prodid
         Order by count(*) DESC
         limit 4;
         '''

# Execute and fetch Queries
    cur =c.cursor()
    try:
        cur.execute(create_table)
        print('Table content-filtering is created')
    except:
        print('Failed to execute')

    try:
        result_cat_brand= fetch_query(c, top_cat_brand)
        print('Query is succesfully execute')
        top_viewed_cat_brand = result_cat_brand[0]

        category = top_viewed_cat_brand[0]
        brand = top_viewed_cat_brand[1]
    except:
        print('Failed to execute')

    try:
        products_ids = []
        result_ids = fetch_query(c,query_prod_ids.format(category, brand))
        for id in result_ids:
            products_ids.append(id[0])
        print(products_ids)
    except:
        ('Failed to execute')

    # insert product_ids in to table content-filtering
    for i in products_ids:
        try:
            cur.execute('Insert into content_filtering values(\'{}\')'.format(i))
            print('Succesfully inserted')
        except: print('error')
    c.commit()

    cur.close()
    c.close()


















# Controle
test_profilid = "'5a39f402ed295900010413d3'"
profilid2 = "'5a394b78ed295900010396a5'"
content_filtering()


