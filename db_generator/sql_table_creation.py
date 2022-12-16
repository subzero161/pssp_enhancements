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
tableNames_localdb = [
                    'patients','patient_conditions','patient_medications','patient_treatments_procedures',
                    'social_determinants','treatments_procedures','conditions','medications','patient_social_determinants'
]
# ### delete everything 
#droppingFunction_all(tableNames_localdb, db_localdb)

### show tables from databases
tableNames_localdb = db_localdb.table_names()
print(tableNames_localdb)


table_patients = """
create table if not exists patients (
    id int auto_increment,
    mrn varchar(255) default null unique,
    first_name varchar(255) default null,
    last_name varchar(255) default null,
    zip_code varchar(255) default null,
    dob varchar(255) default null,
    gender varchar(255) default null,
    contact_mobile varchar(255) default null,
    contact_home varchar(255) default null,
    PRIMARY KEY (id) 
); 
"""
table_patient_conditions = """
create table if not exists patient_conditions (
    id int auto_increment,
    mrn varchar(255) default null,
    icd10_code varchar(255) default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES patients(mrn) ON DELETE CASCADE,
    FOREIGN KEY (icd10_code) REFERENCES conditions(icd10_code) ON DELETE CASCADE
); 
"""
table_patient_medications = """
create table if not exists patient_medications (
    id int auto_increment,
    mrn varchar(255) default null,
    med_ndc varchar(255) default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES patients(mrn) ON DELETE CASCADE,
    FOREIGN KEY (med_ndc) REFERENCES medications(med_ndc) ON DELETE CASCADE
); 
"""
table_patient_treatments_procedures = """
create table if not exists patient_treatments_procedures (
    id int auto_increment,
    mrn varchar(255) default null,
    cpt varchar(255) default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES patients(mrn) ON DELETE CASCADE,
    FOREIGN KEY (cpt) REFERENCES treatment_procedures(cpt) ON DELETE CASCADE
); 
"""
table_social_determinants = """
create table if not exists social_determinants (
    id int auto_increment,
    loinc varchar(255) null unique,
    description varchar(255) default null,
    PRIMARY KEY (id) 
); 
"""
table_medications = """
create table if not exists medications (
    id int auto_increment,
    med_ndc varchar(255) default null unique,
    med_human_name varchar(255) default null,
    med_is_dangerous varchar(255) default null,
    PRIMARY KEY (id)
); 
"""
table_conditions = """
create table if not exists conditions (
    id int auto_increment,
    icd10_code varchar(255) default null unique,
    icd10_description varchar(255) default null,
    PRIMARY KEY (id) 
); 
"""
table_treatments_procedures = """
create table if not exists treatment_procedures (
    id int auto_increment,
    cpt varchar(255) null unique,
    description varchar(255) default null,
    PRIMARY KEY (id)
); 
"""
table_patient_social_determinants = """
create table if not exists patient_social_determinants (
    id int auto_increment,
    mrn varchar(255) default null,
    loinc varchar(255) default null,
    PRIMARY KEY (id),
    FOREIGN KEY (mrn) REFERENCES patients(mrn) ON DELETE CASCADE,
    FOREIGN KEY (loinc) REFERENCES social_determinants(loinc) ON DELETE CASCADE
); 
"""
db_localdb.execute(table_patients)
db_localdb.execute(table_patient_conditions)
db_localdb.execute(table_patient_medications)
db_localdb.execute(table_patient_treatments_procedures)
db_localdb.execute(table_social_determinants)
db_localdb.execute(table_medications)
db_localdb.execute(table_conditions)
db_localdb.execute(table_treatments_procedures)
db_localdb.execute(table_patient_social_determinants)



# get tables from db_localdb
localdb_tables = db_localdb.table_names()
print (localdb_tables)