from databases import Database

from barijat.configs import settings

db_user=settings.db_user
db_passwd=settings.db_passwd
db_host=settings.db_host
db_port=settings.db_port
db_name = settings.db_name

DATABASE_URL = f'mysql+aiomysql://{db_user}:{db_passwd}@{db_host}:{db_port}/{db_name}'

db = Database(
    DATABASE_URL,
    min_size=5,  # 连接池的最小连接数
    max_size=10,  # 连接池的最大连接数
    pool_recycle = 1800,  # 最大生命周期
)
