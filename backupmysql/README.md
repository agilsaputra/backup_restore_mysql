#### 🚀 backup database mysql mengunakan python dan cron dilinux (saya menggunakan linux mint [debian base])🚀 🧑‍💻

- install python ```sudo apt-get install python3```
- install cron ``` sudo apt install cron ```
- download file python ```backup.py```dan ```mysql_config.cnf```di repo ini. Mysql_config nantinya digunakan untuk menaruh user dan password ketika melakukan live backup berhubung ini di localhost sy upload
- keterangan mysql_config.cnf
  ```
  [client]
  user=user_database_kalian
  password=password_database_kalian
  ```
- setelah itu configurasi file python ```backup.py```
  
  ```
  import os
  import time
  import datetime
  import subprocess

  ''' definisikan database yg kalian buat kedalam variable yaitu sy menggunakan db_name (bebas kalian bisa menggunaka 
  data/data_db/database)'''
  
  db_name = 'nama_database_kalian'

  ''' definisikan patch file output backup ke dalam variable
  '''
  
  backup_dir = '/lokasi/file/kalian/'

  ''' masukan waktu ke dalam variable Y=year m=month d=day h=hour m=minute s=second. Saya tidak memakai detik hanya sampe     
  menit saja tanda pemisah juga bisa di ubah dari - ke / atau \ atau + atau _ terserah kalian 
  '''
  
  timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M') 

  ''' tentukan nama output file ouput backup database dengan memanggil variable db_name dan timesamp
  '''
  
  backup_filename = f'{db_name}_backup_{timestamp}.sql' 

  ''' backup database dengan mysqldump. --mysql_config.cnf yaitu config user dan password yg kalian buat     
  td. {backup_dir} memangil database yang akan di backup, panggil variable {backup_dir} adalah lokasi output di 
  pc/server kalian, dan variable {backup_filename} nama output backup database
  '''
  
  mysql_dump_cmd = f'mysqldump --defaults-extra-file=mysql_config.cnf {db_name} > {backup_dir}{backup_filename}'
  
  ''' 
  jalankan dengan subprocess
  '''
  
  subprocess.call(mysql_dump_cmd, shell=True)
  ```
 - setelah itu buka terminal dan ketik ```crontab -e```
 - syntax contab yaitu
   ```
   * * * * * /bin/python3 /path/folder/kalian/berdasarkan/filepython/yang_dibuat/backup.py
   ```
 - ```* * * * *``` yaitu waktu setiap 1 menit akan melakukan backup database kalian bisa lihat di [crontab guru](https://crontab.guru/)
 - setelah itu ctrl + o untuk simpan dan ctrl + x untuk keluar
 - buka folder backup kalian
   ![Screenshot from 2023-08-18 21-56-07](https://github.com/agilsaputra/backup_restore_mysql/assets/22126819/959476f1-f31c-4644-a290-3ff9cefdcca6)

