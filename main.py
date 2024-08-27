import  os
from typing import List
import boto3
from dotenv import load_dotenv

# Carrega as variaveis de ambient do arquivo .env
load_dotenv()

#Configurações da AWS a partir do .env
AWS_ACCESS_KEY_ID: str = os.getenv('AWS_ACESS_KEY_ID')
AWS_SECRET_ACESS_KEY: str = os.getenv('AWS_SECRET_ACCESS_KEY')
AWS_REGION: str = os.getenv('AWS_REGION')
BUCKET_NAME: str = os.getenv('BUCKET_NAME')

# Classes de python
s3_client = boto3.client(
    's3',
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    AWS_SECRET_ACESS_KEY=AWS_SECRET_ACESS_KEY,
    region_name=AWS_REGION
)

## LE OS ARQUIVOS

## JOGA OS ARQUIVOS PRO S3

## DELETA OS ARQUIVOS NO S3

## PIPELINE