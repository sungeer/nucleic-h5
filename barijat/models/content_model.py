from barijat.utils import common
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
        lastrowid = await common.get_lastrowid(db)
    return lastrowid
