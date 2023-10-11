# Full Scanning
import boto3

dynamodb = boto3.resource('dynamodb', region_name = 'ap-northeast-2', 
               aws_access_key_id = 'AKIAU5VSEEQTNGWFVV66',
               aws_secret_access_key = '') #heht-sdk secret access key 참고
table = dynamodb.Table('Movies')

results = table.scan()
#print(type(item))  #dict
#print(item.keys())  #'Items', 'Count', 'ScannedCount', 'ResponseMetadata'
#print(results['Count'], results['ScannedCount'])  # 2 2
items = results['Items']
for i in range(len(items)) :        # SELECT * FROM Movies
    print(items[i])