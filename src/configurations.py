import os


class DBConfigurations:
    postgres_username = os.getenv("POSTGRES_USERNAME")
    postgres_password = os.getenv("POSTGRES_PASSWORD")
    postgres_port = int(os.getenv("POSTGRES_PORT", 5432))
    postgres_db = os.getenv("POSTGRES_DB")
    postgres_server = os.getenv("POSTGRES_SERVER")
    sql_alchemy_db_url = f"postgresql://{postgres_username}:{postgres_password}@{postgres_server}:{postgres_port}/{postgres_db}"
