import psycopg2
#from content_filtering import fetch_query

c = psycopg2.connect("dbname=huwbbackupdb user=postgres password=amaryllis")
cur = c.cursor()

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

    segment_prodid = ''' 
                      --Get the segment of user and the product ids where the user has previously viewed.  
                     select segment, prodid 
                     from profiles , profiles_previously_viewed 
                     where profid = profiles.id And profid ='{}'
                     '''


    get_profid = '''
            -- Get the profile_ids which has the same segment and viewed the same product as the 'profilid'
            select profid from profiles_previously_viewed, profiles where segment = '{}' AND prodid = '{}';
    '''

    res_seg_prof = fetch_query(c,segment_prodid.format(profilid))
    print(res_seg_prof)
    r = res_seg_prof[0]

    userSegment = r[0]
    userProdid = r[1]


    profids_ids = []
    result_profids = fetch_query(c, get_profid.format(userSegment, userProdid))
    for id in result_profids:
        profids_ids.append(id[0])
    print(len(profids_ids))

    recommended_prodids = []
    for profid in profids_ids:
        getProd = 'select prodid from profiles_previously_viewed where profid = {}; '.format(profid)
        recom_prod = fetch_query(c, getProd)
        print(recom_prod)
        '''
        if recom_prod == userProdid:
            continue
        else:
        '''

collaborative('5a394475ed29590001038e43')




