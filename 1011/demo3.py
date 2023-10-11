# Index Scanning
import boto3, dynamodbinfo

table = dynamodbinfo.dynamodb.Table('Movies')
#1. Using get_item
result = table.get_item(
    Key={
        'Code' : '20050112', 'Name' : 'Batman Begins'
    }
)
#print(type(result)) #dict
#print(result.keys()) #'Item', 'ResponseMetadata'
print(result['Item'])