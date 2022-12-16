import os

import sqlalchemy
from dotenv import load_dotenv
from sqlalchemy import create_engine

load_dotenv()
### drop the old tables that do not start with production_
def droppingFunction_limited(dbList, db_source):
    for table in dbList:
        if table.startswith('production_') == False:
            db_source.execute(f'drop table {table}')
            print(f'dropped table {table}')
        else:
            print(f'kept table {table}')

def droppingFunction_all(dbList, db_source):
    for table in dbList:
        db_source.execute(f'drop table {table}')
        print(f'dropped table {table} succesfully!')
    else:
        print(f'kept table {table}')

MYSQL_HOSTNAME = os.getenv("MYSQL_HOSTNAME_localdb")
MYSQL_USER = os.getenv("MYSQL_USER_localdb")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD_localdb")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE_localdb")

connection_string = f'mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOSTNAME}:3306/{MYSQL_DATABASE}'
connection_string

db_localdb = create_engine(connection_string)


### show tables from databases
tableNames_localdb = db_localdb.table_names()


# reoder tables: production_patient_conditions, production_patient_medications, production_medications, production_patients, production_conditions
# tableNames_localdb = [
#                     'patients','patient_conditions','patient_medications','patient_treatments_procedures',
#                     'social_determinants','treatments_procedures','conditions','medications','patient_social_determinants'
# ]
# ### delete everything 
#droppingFunction_all(tableNames_localdb, db_localdb)

table_accounts = """
CREATE TABLE IF NOT EXISTS `accounts` (
	`id` int(11) NOT NULL AUTO_INCREMENT,
  	`username` varchar(50) NOT NULL,
  	`password` varchar(255) NOT NULL,
  	`email` varchar(100) NOT NULL,
    `account_type` varchar(50) NOT NULL,
    `mrn` varchar(50) NULL,
    `date_created` datetime NULL,
    `last_login` datetime NULL,
    PRIMARY KEY (`id`)
);
"""
table_patient_photos = """
CREATE TABLE IF NOT EXISTS `patient_photos` (
    `id` int(11) NOT NULL AUTO_INCREMENT,
    `mrn` varchar(50) NULL,
    `photo_data` longblob NOT NULL,
    `photo_data_rendered` longblob NOT NULL,
    PRIMARY KEY (`id`)
);
"""
db_localdb.execute(table_accounts)
db_localdb.execute(table_patient_photos)
#db_localdb.execute("INSERT INTO accounts(id, username,password, email, account_type) VALUES (1, 'admin', 'admin', 'admin@admin.com', 'admin')")

### show tables from databases
tableNames_localdb = db_localdb.table_names()
print(tableNames_localdb)