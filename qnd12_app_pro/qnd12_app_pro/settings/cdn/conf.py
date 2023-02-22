import os

AWS_ACCESS_KEY=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME='qnd41-staticfiles'
AWS_S3_ENDPOINT_URL="https://sfo3.digitaloceanspaces.com/"
AWS_S3_OBJECT_PARAMETERS={
    "CacheControl": "max-age=86400", 
    "ACL": "public-read"
}

AWS_LOCATION="https://qnd41-staticfiles.sfo3.digitaloceanspaces.com"
#STATIC_URL = f'https://{AWS_S3_ENDPOINT_URL}/static/'
DEFAULT_FILE_STORAGE="qnd00_app_prod.settings.cdn.backends.MediaRootS3BotoStorage"
STATICFILES_STORAGE="qnd00_app_prod.settings.cdn.backends.StaticRootS3BotoStorage"