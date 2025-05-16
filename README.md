# PROG8850Week1Installation
install mysql, python

```bash
ansible-playbook up.yml
```

To use mysql:

```bash
mysql -u root -h 127.0.0.1 -p
```

To shut down:

```bash
ansible-playbook down.yml
```

This is a reproducible mysql setup

---

## Question Answer

### Question 1: Understanding Database Automation
#### 1.1) Explain database automation and its significance in modern data management. Highlight the role of automation in handling large volumes of data efficiently and securely.

A: Database automation is the use of tools that run database jobs by themselves. Jobs can be backups, schema updates, or health checks. The jobs run on a set schedule or when an event fires, so people do not enter commands by hand. Because the jobs run the same way each time, large data sets stay safe and steady. Scripts can encrypt dump files, stream them to cloud storage, and log every step. This helps a team move database quickly while keeping audit trails.

#### 1.2) Analyze the benefits of automating database tasks, including reduced errors, increased reliability, faster deployments, and cost efficiency. Support your analysis with real-world examples or case studies where possible.

A: Benefits of automating database tasks.
1. Reduced errors – A script does not forget steps or mistype a command. For example, backup jobs send fresh snapshots to Amazon S3 each day at Netflix, so engineers no longer risk skipped dumps when traffic peaks. 
2. Increased reliability – Pipeline tasks run even at night. If one run fails, alert hooks tell the on-call engineer at once.
3. Faster deployments – GUI or cli lets developers push schema changes many times a day with a one-click deploy or timer operation, so features reach users sooner. 
4. Cost efficiency – Fewer manual hours and fewer outages cut labor bills and cloud over-provisioning.

### Question 2: Scripting for Database Automation

#### 2.1) Python Scripting for Database Backup Automation

[backup_script.py](./backup_script.py), logic:

1. Reads connection values from environment vars. (system vars or docker environment configuration)
2. Builds a folder named `backups` if it is missing.
3. Creates a filename like `ray_backup_20250516_093045.sql`; the timestamp keeps each dump unique.
4. Runs `mysqldump` with `subprocess.run`.
5. Writes the dump to disk and prints the dump file path.


#### 2.2) Python Scripting for Database Change Deployment

[deploy_changes_script](./deploy_changes_script.py): logic

1. Opens a `.sql` file that lists one or more commands, such as `ALTER TABLE users ADD COLUMN age INT;`.

2. Connects to `MySQL` with the `mysql-connector-python` driver.

3. Starts a transaction.

4. Runs each statement in order.

5. Commits if all succeed; rolls back on the first error and stops.

6. Prints a clear message so a CI job can read success or failure.
