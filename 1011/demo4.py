# update_item
import boto3, dynamodbinfo

table = dynamodbinfo.dynamodb.Table('Movies')
table.update_item(
    Key={
        'Code' : '20050112', 'Name' : 'Batman Begins'
    },
    UpdateExpression='SET Director = :val',      # : 대입한다는 뜻(파스칼 언어) #val이라는 값을 Director에 넣겠다는 뜻
    ExpressionAttributeValues={
        ':val': 'James Francis Cameron'          # val의 값은 'James Francis Cameron'
    }          
)