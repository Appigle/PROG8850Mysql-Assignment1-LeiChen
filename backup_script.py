#!/usr/bin/env python3
"""
Create a MySQL dump with timestamp.
Set MYSQL_USER, MYSQL_ROOT_PASSWORD, MYSQL_DB, MYSQL_HOST, MYSQL_PORT, BACKUP_DIR in the shell.
"""

import os
import subprocess
from datetime import datetime
from pathlib import Path

def make_backup():

    # Retrieve variables from env config
    db   = os.getenv("MYSQL_DB", "ray_backup")
    user = os.getenv("MYSQL_USER", "root")
    pw   = os.getenv("MYSQL_ROOT_PASSWORD", "")
    host = os.getenv("MYSQL_HOST", "localhost")
    port = os.getenv("MYSQL_PORT", "3306")
    out  = Path(os.getenv("BACKUP_DIR", "ray_backups"))
    out.mkdir(parents=True, exist_ok=True)

    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file  = out / f"{db}_{stamp}.sql"

    # MySql dump
    cmd = [
        "mysqldump",
        f"--user={user}",
        f"--password={pw}",
        f"--host={host}",
        f"--port={port}",
        db,
    ]

    # Write dump data to storage file
    with open(file, "w") as dump:
        subprocess.run(cmd, check=True, stdout=dump)

    print(f"Backup saved to {file}")

if __name__ == "__main__":
    make_backup()
