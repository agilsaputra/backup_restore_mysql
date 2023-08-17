import os
import time
import datetime
import subprocess

# MySQL database details
db_user = 'admin1'
db_password = '818642'
db_name = 'ingest_data_terminal'

# Backup directory
backup_dir = '/home/gandalf/DataEngineer/PORTFOLIO_SQL/backupsql/'

# Current date and time
timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M')

# Backup filename
backup_filename = f'{db_name}_backup_{timestamp}.sql'

# MySQL dump command
mysql_dump_cmd = f'mysqldump -u {db_user} -p{db_password} {db_name} > {backup_dir}{backup_filename}'

# Run the MySQL dump command
subprocess.call(mysql_dump_cmd, shell=True)
