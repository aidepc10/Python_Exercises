import sqlite3

db_path = 'C:\Users\Aide\Documents\Big Data\BasedeDatos\school.db'


def contact_database(self,query,query_input):
    conn = sqlite3.connect(db_path)
    conn.text_factory = str
    with conn:
        cursor = conn.cursor()
        cursor.execute(query, query_input)
        return cursor.fetchall()


def get_all_students(self):
    query = 'SELECT * from student'
    query_input = ()
    return self.contact_database(query,query_input)

