import os
import time
import datetime
import subprocess

# MySQL database details
db_name = 'ingest_data_terminal'

# Backup directory
backup_dir = '/home/gandalf/DataEngineer/PORTFOLIO-SQL/backupsql/'

# Current date and time
timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')

# Backup filename
backup_filename = f'{db_name}_backup_{timestamp}.sql'

# MySQL dump command
mysql_dump_cmd = f'mysqldump --defaults-extra-file=mysql_config.cnf {db_name} > {backup_dir}{backup_filename}'

# Run the MySQL dump command
subprocess.call(mysql_dump_cmd, shell=True)
