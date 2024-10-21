from barijat.utils.db_util import db


async def add_content(message_id, content):
    sql_str = '''
        INSERT INTO 
            contents 
            (message_id, content) 
        VALUES 
            (:message_id, :content)
    '''

    last_id_str = 'SELECT LAST_INSERT_ID()'

    values = {'message_id': message_id, 'content': content}
    await db.execute(sql_str, values)

    last_id = await db.fetch_one(last_id_str)
    lastrowid = last_id[0]

    return lastrowid
