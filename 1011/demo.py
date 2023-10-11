import boto3

boto3.resource('dynamodb', region_name = 'ap-northeast-2', 
               aws_access_key_id = 'AKIAU5VSEEQTNGWFVV66',
               aws_secret_access_key = '') #heht-sdk secret access key 참고

client = boto3.client('dynamodb')
list_tables = client.list_tables()  # dict
#print(list_tables.keys())
#print(len(list_tables['TableNames']))

response = client.create_table(
    AttributeDefinitions=[
        {
            'AttributeName' : 'Code',
            'AttributeType' : 'S'
        },
        {
            'AttributeName' : 'Name',
            'AttributeType' : 'S'
        }
    ],
    TableName='Movies',
    KeySchema=[
        {
            'AttributeName' : 'Code',
            'KeyType' : 'HASH'
        },
        {
            'AttributeName' : 'Name',
            'KeyType' : 'RANGE'
        }
    ],
    Tags=[
        {
            'Key': 'Name',
            'Value': 'Movies'
        },
    ],
    TableClass='STANDARD',
    DeletionProtectionEnabled=True,             # 삭제 방지
    BillingMode='PROVISIONED',
    ProvisionedThroughput={
        'ReadCapacityUnits': 5,
        'WriteCapacityUnits': 5
    },
)