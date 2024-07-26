from config import connect_db


def create_table_users():
    database = connect_db()
    cursor = database.cursor()
    cursor.execute('''
        DROP TABLE IF EXISTS users;
        CREATE TABLE IF NOT EXISTS users(
            user_id INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            user_fio TEXT,
            user_phone TEXT,
            telegram_id BIGINT NOT NULL UNIQUE
        ); 
    ''')
    database.commit()
    database.close()


def add_data_user(user_fio, user_phone, telegram_id):
    database = connect_db()
    cursor = database.cursor()
    cursor.execute('''
        INSERT INTO users(user_fio, user_phone, telegram_id)
        VALUES(%s, %s, %s)
    ''', (user_fio, user_phone, telegram_id))
    database.commit()
    database.close()


# create_table_users()


def search_tg_user(tg_id):
    database = connect_db()
    cursor = database.cursor()
    cursor.execute('''
        SELECT user_id FROM users WHERE telegram_id = %s
    ''', (tg_id, ))
    return cursor.fetchone()


def create_table_requests_users():
    database = connect_db()
    cursor = database.cursor()
    cursor.execute('''
        DROP TABLE IF EXISTS requests_users;
        CREATE TABLE IF NOT EXISTS requests_users(
            request_user INTEGER GENERATED ALWAYS AS IDENTITY PRIMARY KEY,
            city_name TEXT,
            temp TEXT,
            min_temp TEXT,
            max_temp TEXT,
            feels_temp TEXT,
            datetime_request TEXT,
            user_id INTEGER REFERENCES users(user_id),
            correctly BOOLEAN
        );
    ''')
    database.commit()
    database.close()


# create_table_requests_users()


def add_data_request_user(city_name, temp, min_temp, max_temp, feels_temp, datetime_request, user_id):
    database = connect_db()
    cursor = database.cursor()
    cursor.execute('''
        INSERT INTO requests_users(city_name, temp, min_temp, max_temp, feels_temp, datetime_request, user_id)
        VALUES(%s, %s, %s, %s, %s, %s, %s);
    ''', (city_name, temp, min_temp, max_temp, feels_temp, datetime_request, user_id))
    database.commit()
    database.close()


def update_table_correctly(new_value, datetime_request, user_id):
    database = connect_db()
    cursor = database.cursor()
    cursor.execute('''
        UPDATE requests_users
        SET correctly = %s
        WHERE datetime_request = %s AND user_id = %s
    ''', (new_value, datetime_request, user_id))
    database.commit()
    database.close()


def get_requests(user_id):
    database = connect_db()
    cursor = database.cursor()
    cursor.execute('''
        SELECT * FROM requests_users WHERE user_id = %s
        ORDER BY request_user;
    ''', (user_id, ))
    data = cursor.fetchall()
    database.close()
    return data


def delete_requests(user_id):
    database = connect_db()
    cursor = database.cursor()
    cursor.execute('''
        DELETE FROM requests_users WHERE user_id = %s;
    ''', (user_id, ))
    database.commit()
    database.close()

