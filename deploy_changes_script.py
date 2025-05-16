#!/usr/bin/env python3
"""
Run SQL statements from a file inside a single transaction.
Usage: python deploy_changes_script.py [SQL_FILE_PATH] (e.g.: path/to/db_changes.sql)
"""

import os
import sys
import mysql.connector as db

def main():
    # Retrieve the sql_file path, if not provided, use default name db_changes.sql
    sql_file = sys.argv[1] if len(sys.argv) > 1 else "db_changes.sql"
    with open(sql_file, "r") as f:
        sql = f.read()

    # Connect MySQL db
    conn = db.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_PASSWORD", ""),
        database=os.getenv("MYSQL_DB", "test"),
        autocommit=False,
    )

    cur = conn.cursor()
    try:
        # Read the sql command and execute
        for stmt in sql.split(";"):
            stmt = stmt.strip()
            if stmt:
                cur.execute(stmt)
        conn.commit()
        print("db changes has applied")
    except db.Error as err:
        # Sql execution failed and rollback
        conn.rollback()
        print(f"Something wrong: Error: {err}")
        sys.exit(1)
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    main()
