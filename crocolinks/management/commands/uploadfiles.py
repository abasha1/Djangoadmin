from django.core.management.base import BaseCommand, CommandError
from crocolinks.models import CrocoLink
from datetime import datetime
import os
import shutil
import boto3
import logging
from botocore.config import Config
import requests
from botocore.exceptions import ClientError, NoCredentialsError
import time
from twisted.internet import task, reactor
##mysqlimport
import mysql.connector
from pathlib import Path
from os import path
###AWS INFO####
access_key = '#'
access_secret = '#'
bucket_name = '#'
bucket_name2= '#'
client = boto3.client('s3')
list_objects_bucket = client.list_objects(Bucket=bucket_name)
# print(list_objects_bucket)


class Command(BaseCommand):
    help = 'Linkebis aploadi'

    def handle(self, *args, **options):

        # mydb = mysql.connector.connect(host="localhost", user="newuser",database="cointrack",passwd="password")
        # mycursor = mydb.cursor()
        ####Connet To S3 Service
        client_s3= boto3.client(
            's3',
            region_name="eu-west-2",
            aws_access_key_id=access_key,
            aws_secret_access_key=access_secret
        )

        counter = 0
        s3_resource = boto3.resource("s3", region_name="eu-west-2")
        #upload files to S3 Bucker
        data_file_folder = r"//10.0.#/Sh#ed/123"
        t1 = time.strftime('%Y-%m-%d %H:%M:%S')
         
        try:
            #bucket_name = "S3_Bucket_Name" #s3 bucket name
            data_file_folder = r"//10.0.#/Sh#d/1#3/" # local folder for upload

            my_bucket = s3_resource.Bucket(bucket_name)
            my_bucket2= s3_resource.Bucket(bucket_name2)

            for path, subdirs, files in os.walk(data_file_folder):
                path = path.replace("\\","/")
                directory_name = path.replace(data_file_folder,"")
                Destination_dir= "//10.0.#/Sh#r#d/gad#n#bi/"
                Dest_dir_xelmeored="//10.0.#/Sha#ed/Xelme#i#ebi/"
                for file in files:
                    if os.path.isfile(Destination_dir+file)==False:
                
                        
                        now = datetime.now()
                        my_bucket.upload_file(os.path.join(path, file),file)#directory_name+'/'+file)  ###bucketze Uploadi
                        my_bucket2.upload_file(os.path.join(path, file),file)
                        t1 = time.strftime('%Y-%m-%d %H:%M:%S')
                        print('Uploading file {0}...'.format(file))
                        print(path)
                        print(t1)
                        CrocoLink.objects.create(title=file, link="#"+file)
                        counter+=1
                        #shutil.move(path+"/"+file, Destination_dir)
                        print(file)
                        shutil.move((path+"/"+file), os.path.join(Destination_dir,file))
                    else:
                        if os.path.isfile(Destination_dir+file)==True: #### Tu ukve ertxel gadatanili iqneb sxva foldershi gadaitans ro ar gadaawero
                            now = datetime.now()
                            my_bucket.upload_file(os.path.join(path, file),file)#directory_name+'/'+file)  ###bucketze Uploadi
                            my_bucket2.upload_file(os.path.join(path, file),file)
                            t1 = time.strftime('%Y-%m-%d %H:%M:%S')
                            print('Uploading file {0}...'.format(file))
                            print(path)
                            print(t1)
                            CrocoLink.objects.create(title=file, link="#"+file)
                            #shutil.move(path+"/"+file, Destination_dir)
                            print(file)
                            counter+=1
                            shutil.move((path+"/"+file), os.path.join(Dest_dir_xelmeored,file))
            print(counter)
            requests.get("https://api.telegram.org/##ext=ადმინპანელში დაემატა - {} ახალი".format(counter))



        except Exception as err:
            print(err)
