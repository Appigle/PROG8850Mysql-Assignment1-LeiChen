#!/usr/bin/env python3
"""
Run SQL statements from a file inside a single transaction.
Usage: python deploy_changes_script.py path/to/changes.sql
"""

import os
import sys
import mysql.connector as db

def main():
    sql_file = sys.argv[1] if len(sys.argv) > 1 else "changes.sql"
    with open(sql_file, "r") as f:
        sql = f.read()

    conn = db.connect(
        host=os.getenv("MYSQL_HOST", "localhost"),
        port=int(os.getenv("MYSQL_PORT", "3306")),
        user=os.getenv("MYSQL_USER", "root"),
        password=os.getenv("MYSQL_ROOT_PASSWORD", ""),
        database=os.getenv("MYSQL_DB", "test"),
        autocommit=False,
    )

    cur = conn.cursor()
    try:
        for stmt in sql.split(";"):
            stmt = stmt.strip()
            if stmt:
                cur.execute(stmt)
        conn.commit()
        print("Changes applied")
    except db.Error as err:
        conn.rollback()
        print(f"Error: {err}")
        sys.exit(1)
    finally:
        cur.close()
        conn.close()

if __name__ == "__main__":
    main()
