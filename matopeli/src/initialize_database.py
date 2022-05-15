from database_connection import get_database_connection


def drop_tables(db):

    db.execute("""
        drop table if exists users;
    """)

def create_tables(db):

    db.execute("""
        create table users (
            score text primary key,
            day text,
            month text,
            year text
        );
    """)

    db.execute("""
        insert into users values (
            0,
            0,
            0,
            0
        );
    """)



def initialize_database():

    db = get_database_connection()

    drop_tables(db)
    create_tables(db)


if __name__ == "__main__":
    initialize_database()