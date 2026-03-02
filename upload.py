import boto3
import ignore.creds as creds


def upload(img_loc, out_name):
    #info to access aws s3
    access_key = creds.access_key
    secret_key = creds.secret_key
    bucket_name = "awsc-image-watermarker"
    region = "eu-north-1"


    s3_client = boto3.client(
        service_name='s3',
        region_name=region,
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key

    )

    response = s3_client.upload_file(img_loc,bucket_name,out_name)
    if(response != None):
        print(f"upload file response: {response}")

