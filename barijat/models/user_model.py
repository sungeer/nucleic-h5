from barijat.utils.db_util import db


async def get_user_by_phone(phone_number):
    sql_str = '''
        SELECT
            id, name, phone, password_hash, is_admin, created_time
        FROM
            users
        WHERE
            phone = :phone_number
    '''
    values = {'phone_number': phone_number}
    user_info = await db.fetch_one(sql_str, values)
    return user_info

async def get_user_by_id(user_id):
    sql_str = '''
        SELECT
            id, name, phone, is_admin, created_time
        FROM
            users
        WHERE
            id = :user_id
    '''
    values = {'user_id': user_id}
    user_info = await db.fetch_one(sql_str, values)
    return user_info
