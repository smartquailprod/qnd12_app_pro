import os

AWS_ACCESS_KEY=os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY=os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME='qnd12-staticfiles'
AWS_S3_ENDPOINT_URL="https://sfo3.digitaloceanspaces.com/"
AWS_S3_OBJECT_PARAMETERS={
    "CacheControl": "max-age=86400", 
    "ACL": "public-read"
}

AWS_LOCATION="https://qnd12-staticfiles.sfo3.digitaloceanspaces.com"
#STATIC_URL = f'https://{AWS_S3_ENDPOINT_URL}/static/'
DEFAULT_FILE_STORAGE="qnd12_app_pro.settings.cdn.backends.MediaRootS3BotoStorage"
STATICFILES_STORAGE="qnd12_app_pro.settings.cdn.backends.StaticRootS3BotoStorage"