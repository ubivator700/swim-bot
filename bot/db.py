import pymysql
import pymysql.cursors

from mysql.connector import connect, Error


def get_connection():
    connection = pymysql.connect(host="localhost",
                                 user="admin",
                                 password="babyor123",
                                 db="swim_shot",
                                 charset="utf8",
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

def f_connection():
    f_conn = connect(
        host="localhost",
        user="admin",
        password="babyor123",
    )
    return f_conn


def make_db():
    f_conn = f_connection()
    try:
        with f_conn.cursor() as cursor:
            sql = 'CREATE DATABASE IF NOT EXISTS swim_shot'
            cursor.execute(sql)
    finally:
        f_conn.close()

def make_table():
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'CREATE TABLE IF NOT EXISTS swim_bot (\nid INT NOT NULL AUTO_INCREMENT,\n user_id varchar(256),\nposition varchar(256),\nname varchar(256),\nadult varchar(256),\npool varchar(256),\ntype varchar(256),\nage varchar(256),\ntrainer varchar(256),\nphone varchar(256),\nPRIMARY KEY(id)\n);'
            cursor.execute(sql)
    finally:
        connection.close()

#GET
def get_all(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT name, adult, pool, type, age, trainer, phone FROM swim_bot'
            cursor.execute(sql, (user_id))
            form = cursor.fetchone()
    finally:
        connection.close()
    return form

def get_form(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT name, adult, pool, type, age, trainer, phone FROM swim_bot WHERE user_id = %s'
            cursor.execute(sql, (user_id))
            form = cursor.fetchone()
    finally:
        connection.close()
    return form



def get_name(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT name FROM swim_bot WHERE user_id = %s'
            cursor.execute(sql, (user_id))
            name = cursor.fetchone()
    finally:
        connection.close()
    return name['name']


def get_adult(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT adult FROM swim_bot WHERE user_id = %s'
            cursor.execute(sql, (user_id))
            adult = cursor.fetchone()
    finally:
        connection.close()
    return adult['adult']


def get_position(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT position FROM swim_bot WHERE user_id = %s'
            cursor.execute(sql, (user_id))
            pos = cursor.fetchone()
    except:
        position = 'не подписан'
    finally:
        connection.close()
        position = pos['position']
    return position


def get_pool(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT pool FROM swim_bot WHERE user_id = %s'
            cursor.execute(sql, (user_id))
            pool = cursor.fetchone()
    finally:
        connection.close()
    return pool['pool']


def get_type(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT type FROM swim_bot WHERE user_id = %s'
            cursor.execute(sql, (user_id))
            kid_type = cursor.fetchone()
    finally:
        connection.close()
    return kid_type['type']

def get_trainer(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT trainer FROM swim_bot WHERE user_id = %s'
            cursor.execute(sql, (user_id))
            trainer = cursor.fetchone()
    finally:
        connection.close()
    return trainer['trainer']

def get_phone(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT phone FROM swim_bot WHERE user_id = %s'
            cursor.execute(sql, (user_id))
            phone = cursor.fetchone()
    finally:
        connection.close()
    return phone['phone']

def get_age(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'SELECT age FROM swim_bot WHERE user_id = %s'
            cursor.execute(sql, (user_id))
            age = cursor.fetchone()
    finally:
        connection.close()
    return age['age']
    


#SET
def set_trainer(user_id, trainer):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'UPDATE swim_bot SET trainer = %s WHERE user_id = %s'
            cursor.execute(sql, (trainer, user_id))
            connection.commit()
    finally:
        connection.close()
    return

def set_position(user_id, position):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'UPDATE swim_bot SET position = %s WHERE user_id = %s'
            cursor.execute(sql, (position, user_id))
            connection.commit()
    finally:
        connection.close()
    return


def set_name(user_id, name):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'UPDATE swim_bot SET name = %s WHERE user_id = %s'
            cursor.execute(sql, (name, user_id))
            connection.commit()
    finally:
        connection.close()
    return


def set_adult(user_id, adult):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'UPDATE swim_bot SET adult = %s WHERE user_id = %s'
            cursor.execute(sql, (adult, user_id))
            connection.commit()
    finally:
        connection.close()
    return


def set_pool(user_id, pool):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'UPDATE swim_bot SET pool = %s WHERE user_id = %s'
            cursor.execute(sql, (pool, user_id))
            connection.commit()
    finally:
        connection.close()
    return

def set_type(user_id, type):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'UPDATE swim_bot SET type = %s WHERE user_id = %s'
            cursor.execute(sql, (type, user_id))
            connection.commit()
    finally:
        connection.close()
    return


def set_kid_age(user_id, age):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'UPDATE swim_bot SET age = %s WHERE user_id = %s'
            cursor.execute(sql, (age, user_id))
            connection.commit()
    finally:
        connection.close()
    return


def set_phone(user_id, phone):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'UPDATE swim_bot SET phone = %s WHERE user_id = %s'
            cursor.execute(sql, (phone, user_id))
            connection.commit()
    finally:
        connection.close()
    return


#ADD
def add_user(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql1 = 'SELECT * FROM swim_bot WHERE user_id = %s'
            check = cursor.execute(sql1, (user_id))
            connection.commit()

            if check == 0:
                sql2 = 'INSERT INTO swim_bot (user_id, position) VALUES (%s, %s)'
                cursor.execute(sql2, (user_id, 'nachat'))
                connection.commit()
    finally:
        connection.close()
    return


#DELETE
def delete_user(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'DELETE FROM swim_bot WHERE user_id = %s'
            cursor.execute(sql, (user_id))
            connection.commit()
    finally:
        connection.close()
    return

def delete_props(user_id):
    connection = get_connection()
    try:
        with connection.cursor() as cursor:
            sql = 'DELETE name, adult, pool, type, age, trainer, phone FROM swim_bot WHERE user_id = %s'
            cursor.execute(sql, (user_id))
            connection.commit()
    finally:
        connection.close()
    return
