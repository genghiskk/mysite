logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
        logging.debug('A debug message!')
        logging.info('We processed  records')
        cnx = mysql.connector.connect(user='rbkahn', database='momdb', password='studman1')
        cursor = cnx.cursor()
        query = ("SELECT * FROM polls_todo where todo_id=1")
        cursor.execute(query)
        rows = cursor.fetchall() 
        for row in rows:
            print(row)
            
        cursor.close()
        cnx.close()