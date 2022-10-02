import os
import sys

from django.shortcuts import render
from django.conf import settings
from django.contrib.auth import get_user_model

import rest_framework
from rest_framework.views import APIView
# Create your views here.

from psycopg2 import connect
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT



def save_db_settings_to_file(db_settings):
    path_to_store_settings = os.path.join(settings.BASE_DIR,'database_settings')
    if (not os.path.isdir(path_to_store_settings)):
         os.makedirs(path_to_store_settings)

    newDbString = """
DATABASES['%(id)s'] = {
'ENGINE': 'django.db.backends.postgresql_psycopg2',
'NAME': '%(NAME)s',                      
'PASSWORD': 'postgres',                
'HOST': 'localhost',                     
'PORT': '5432',                    
}
    """ % db_settings
    file_to_store_settings = os.path.join(path_to_store_settings, db_settings['id'] + ".py")

    file = open(file_to_store_settings,'w') 
 
    file.write(newDbString)
    file.close() 



class CreateUser(APIView):
    permission_classes=[rest_framework.permissions.AllowAny]
    def get(self,request,id,format=None):
       
        u=get_user_model().objects.create_user(username=id,password='asdf1234')

        con = None
        con = connect(user='postgres', host = 'localhost', password='postgres')

        db_name='db'+str(id)
        con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
        cur = con.cursor()
        cur.execute('CREATE DATABASE ' + db_name)
        cur.close()
        con.close()

        from django.conf  import settings
        database_id = db_name#just something unique
        newDatabase = {}
        newDatabase["id"] = database_id
        newDatabase['ENGINE'] = 'django.db.backends.postgresql_psycopg2',

        newDatabase['NAME'] = db_name
        newDatabase['USER'] = 'postgres'
        newDatabase['PASSWORD'] = 'postgres'
        newDatabase['HOST'] = 'localhost'
        newDatabase['PORT'] = 5432
        settings.DATABASES[database_id] = newDatabase

        from django.core.management import call_command
        # call_command('../manage.py makemigrations --database='+db_name)
        # call_command('../manage.py migrate --database='+db_name)

        call_command('makemigrations')
        call_command('migrate','--database='+db_name)

        # import subprocess
        # command = 'python3 manage.py makemigrations && python3 manage.py migrate --database='+db_name
        # proc = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        # stdout, stderr = proc.communicate(command)
        save_db_settings_to_file(newDatabase) #this is for step 2)



class CreateSth(APIView): # just for creating test user.
    # permission_classes=[rest_framework.permissions.IsAuthenticated]
    def get(self,request,format=None):
        get_user_model().objects.create_user(username='kadauser',password='asdf1234')
