from barijat.utils.db_util import db


async def add_chat(conversation_id, title, user_id):
    sql_str = '''
        INSERT INTO 
            chats 
            (conversation_id, title, user_id) 
        VALUES 
            (:conversation_id, :title, :user_id)
    '''
    values = {
        'conversation_id': conversation_id,
        'title': title,
        'user_id': user_id
    }
    async with db.transaction():
        await db.execute(sql_str, values)
        lastrowid = await db.fetch_val('SELECT LAST_INSERT_ID()')
    return lastrowid

async def get_chats(user_id):
    sql_str = '''
        SELECT
            id, conversation_id, title, created_time
        FROM
            chats
        WHERE
            user_id = :user_id
        LIMIT 100
    '''
    values = {'user_id': user_id}
    chats = await db.fetch_all(sql_str, values)
    return chats

async def get_chat_by_conversation(conversation_id):
    sql_str = '''
        SELECT 
            id, conversation_id, title, created_time
        FROM 
            chats
        WHERE
            conversation_id = :conversation_id
    '''
    values = {'conversation_id': conversation_id}
    chat_info = await db.fetch_one(sql_str, values)  # None or Record as dict
    return chat_info
