import psycopg2
#from content_filtering import fetch_query

c = psycopg2.connect("dbname=huwbbackupdb user=postgres password=amaryllis")
cur = c.cursor()

#TODO Collaborative set regels moet aangepast wordend


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



def collaborative(profilid):
    'Recommend products based on similar profilid'

    #Query that needs to
    userSegment = []
    userProdid = []
    userCategory = []
    userSubCategory = []
    userSubSubCategory =[]
    userTargetAudience = []

    create_table = '''
        --Query to drop and create table content-filtering
        Drop table if exists collaborative_filtering ;

        Create table collaborative_filtering(
        product_id varchar
        ) ; '''

    getEigenschappenUserId= ''' 
                    select  profiles.segment , prodid, products.category,products.subcategory, products.subsubcategory, products.targetaudience 
                    from profiles, products, profiles_previously_viewed 
                    where profiles.id = profid and prodid = products.id and profid='{}';;
                     '''


    #-----------------------------------------------------------------------------------------------------------------------------


    res_EigenschappenUserId = fetch_query(c,getEigenschappenUserId.format(profilid))
    print(res_EigenschappenUserId)
    res_EigenschappenUserId = res_EigenschappenUserId[0]

    userSegment.append(res_EigenschappenUserId[0])
    userProdid.append(res_EigenschappenUserId[1])
    userCategory.append(res_EigenschappenUserId[2])
    userSubCategory.append(res_EigenschappenUserId[3])
    userSubSubCategory.append(res_EigenschappenUserId[4])
    userTargetAudience.append(res_EigenschappenUserId[5])



    get_productsID = '''
                select distinct  prodid ,  count(*)
                from profiles, products, profiles_previously_viewed 
                where profid = profiles.id and profiles.segment = '{}' and products.category = '{}' 
                and products.subcategory = '{}'and products.subsubcategory = '{}' 
                and products.targetaudience = '{}' and prodid != '{}'
                Group by profiles_previously_viewed.prodid
                Order by count(*) DESC
                Limit  4;
            '''


    res_productID = fetch_query(c, get_productsID.format(userSegment[0], userCategory[0], userSubCategory[0],
                                                          userSubSubCategory[0], userTargetAudience[0], userProdid[0]))
    if res_productID ==[]:
        get_productsID_2 = '''
                        select distinct  prodid ,  count(*)
                        from profiles, products, profiles_previously_viewed 
                        where profid = profiles.id and profiles.segment = '{}' and products.category = '{}'  
                        and products.targetaudience = '{}' and prodid != '{}'
                        Group by profiles_previously_viewed.prodid
                        Order by count(*) DESC
                        Limit  4;
                    '''

        res_productID = fetch_query(c, get_productsID_2.format(userSegment[0], userCategory[0], userTargetAudience[0],userProdid[0]))

        if res_productID== []:
            get_productsID_3 = '''
                select distinct  prodid   count(*)
                from profiles, profiles_previously_viewed
                where profid = profiles.id and profiles.segment = '{}' and prodid != '{}'  
                Group by profiles_previously_viewed.prodid
                Order by count(*) DESC
                Limit  4;
                        '''

            res_productID = fetch_query(c, get_productsID_3.format(userSegment[0], userProdid[0]))
            print(res_productID)

        else:
            print(res_productID)
    else:
        print(res_productID)


#-----------------------------------------------------------------------------
    try:
        cur.execute(create_table)
        print('Table colaborative_filtering is created')
    except:
        print('Failed to execute')

    # insert product_ids in to table collaborative-filtering
    for i in res_productID:
        try:
            cur.execute('Insert into collaborative_filtering  values(\'{}\')'.format(i[0]))
            print('Succesfully inserted')
        except:
            print('error')
    c.commit()

    cur.close()
    c.close()


#-------------------------------------------------------------------------------------

collaborative('5a394475ed29590001038e43')
#collaborative('5a39402ba825610001bb6dc1')

testId ='5a394b78ed295900010396a5'


