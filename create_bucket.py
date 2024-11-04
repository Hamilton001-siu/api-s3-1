import boto3

def crear_bucket(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket_name']

    # Proceso
    s3 = boto3.client('s3')
    response = s3.create_bucket(Bucket=nombre_bucket)

    # Salida
    return {
        'statusCode': 200,
        'message': f'Bucket {nombre_bucket} creado exitosamente.',
        'response': response
    }
