from barijat.utils.db_util import db


async def add_content(message_id, content):
    sql_str = '''
        INSERT INTO 
            contents 
            (message_id, content) 
        VALUES 
            (:message_id, :content)
    '''
    values = {'message_id': message_id, 'content': content}
    async with db.transaction():
        await db.execute(sql_str, values)
        lastrowid = await db.fetch_val('SELECT LAST_INSERT_ID()')
    return lastrowid
