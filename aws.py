import boto3
from botocore.client import Config

ACCESS_KEY_ID = "AKIAZNN5NBT7VXAFB64K"
ACCESS_SECRET_KEY = "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"
BUCKET_NAME = "flask121"

data = open("baba.jpg", 'rb')

s3 = boto3.resource(
    "s3",
    aws_access_key_id=ACCESS_KEY_ID,
    aws_secret_access_key=ACCESS_SECRET_KEY,
    config=Config(signature_version="s3v4")
)
s3.Bucket(BUCKET_NAME).put_object(Key="baba.jpg", Body=data)

print("Done")

