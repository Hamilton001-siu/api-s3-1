import boto3

def crear_directorio(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket_name']
    nombre_directorio = event['body']['directorio_name'] + '/'

    # Proceso
    s3 = boto3.client('s3')
    # Crear un objeto vacío con el nombre del "directorio"
    s3.put_object(Bucket=nombre_bucket, Key=nombre_directorio)

    # Salida
    return {
        'statusCode': 200,
        'message': f'Directorio {nombre_directorio} creado en el bucket {nombre_bucket}.'
    }
