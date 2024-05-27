import psycopg2
from contextlib import closing
#try:
    # пытаемся подключиться к базе данных
#    conn = psycopg2.connect(dbname='tdb2', user='tuser', password='tpassword', host='tip')
#except:
    # в случае сбоя подключения будет выведено сообщение в STDOUT
#    print('Can`t establish connection to database')
with closing(psycopg2.connect(dbname='tdb2', user='tuser', password='tpassword', host='tip')) as conn:
    with conn.cursor() as cursor:
        cursor.execute('select words, Dictionary.translate, description, Terms.translate from Dictionary inner join Terms on Dictionary.id = Terms.words_id')
        for row in cursor:
            print(row)

