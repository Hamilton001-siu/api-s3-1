import boto3

def subir_archivo(event, context):
    # Entrada (json)
    nombre_bucket = event['body']['bucket_name']
    nombre_directorio = event['body']['directorio_name']
    nombre_archivo = event['body']['file_name']  # Nombre del archivo a subir
    ruta_archivo = event['body']['file_path']  # Ruta local del archivo en tu máquina

    # Proceso
    s3 = boto3.client('s3')
    ruta_objeto_s3 = f'{nombre_directorio}/{nombre_archivo}'
    s3.upload_file(ruta_archivo, nombre_bucket, ruta_objeto_s3)

    # Salida
    return {
        'statusCode': 200,
        'message': f'Archivo {nombre_archivo} subido a {nombre_directorio} en el bucket {nombre_bucket}.'
    }
