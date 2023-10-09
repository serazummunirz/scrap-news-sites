import os, json
import boto3
import botocore

import SetEnviron
SetEnviron.SetEnviron()


bucket_name = os.environ['S3_BUCKET_NAME']


s3_client = boto3.client('s3')
s3 = boto3.resource('s3')


def create_bucket():

    try:
        s3_client.create_bucket(
            ACL='private',
            Bucket=bucket_name,
            CreateBucketConfiguration={
                'LocationConstraint': 'us-east-2'
            }
        )
    except botocore.exceptions.ClientError as e:
        print(e)


def create_directory_inside_s3(directory_path):

    def does_directory_exist_or_create(bucket_name, directory_path):
        s3_client = boto3.client('s3')
        
        response = s3_client.list_objects_v2(Bucket=bucket_name, Prefix=directory_path)

        if 'Contents' in response:
            return True
        else:
            return False


    if does_directory_exist_or_create(bucket_name, directory_path):
        print(f"The directory '{directory_path}' exists in the bucket '{bucket_name}'.")
    else:
        print("Creating...")
        bucket = s3.Bucket(bucket_name)
        directory_name = directory_path
        bucket.put_object(Key=directory_name)



def upload_file_to_s3(local_file_path, s3_file_path):

    s3_key = s3_file_path

    try:
        s3_client.upload_file(local_file_path, bucket_name, s3_key)
        print(f"File '{local_file_path}' uploaded to S3 bucket '{bucket_name}' with key '{s3_key}'.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")