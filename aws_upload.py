import os
import boto3

def upload_file(testfile,bucketname, filename):
    print('Uploading {0} to Amazon S3 bucket{1}.'.format(testfile, bucketname))
    client.meta.client.upload_file(testfile, bucketname,filename)
    print('Uploading {0} to Amazon S3 bucket{1} complete.'.format(testfile,bucketname))

os.environ['AWS_CONFIG_FILE'] = 'aws_config.ini'

client = boto3.resource('s3')
'''
response = client.create_bucket(ACL='private',
                                Bucket='wagersparkhackathon2',
                                CreateBucketConfiguration={'LocationConstraint':'us-west-1'
                                }
)
'''
path = os.getcwd()
bucket_name = 'wagersparkhackathon2'
filename = "_aave_interestrate_output.xlsx"
upload_file(path+"/data/"+filename,bucket_name,filename)
filename= "_aave_interestrate_eth_output.csv"
upload_file(path+"/data/"+filename,bucket_name,filename)
filename="_aave_interestrate_dai_output.csv"
upload_file(path+"/data/"+filename,bucket_name,filename)
filename="_aave_interestrate_wbtc_output.csv"
upload_file(path+"/data/"+filename,bucket_name,filename)
filename="_aave_interestrate_usdt_output.csv"
upload_file(path+"/data/"+filename,bucket_name,filename)
filename="_aave_interestrate_usdc_output.csv"
upload_file(path+"/data/"+filename,bucket_name,filename)





