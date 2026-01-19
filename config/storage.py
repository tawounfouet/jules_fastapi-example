import boto3
from config.settings import settings

def get_s3_client():
    """
    Creates and returns a boto3 S3 client configured for Minio or S3.
    """
    s3 = boto3.client(
        "s3",
        endpoint_url=f"http://{settings.MINIO_ENDPOINT}" if not settings.MINIO_SECURE else f"https://{settings.MINIO_ENDPOINT}",
        aws_access_key_id=settings.MINIO_ACCESS_KEY,
        aws_secret_access_key=settings.MINIO_SECRET_KEY,
        region_name="us-east-1" # Minio default region, often ignored but needed by boto3
    )
    return s3

# Global instance
s3_client = get_s3_client()

def create_bucket_if_not_exists(bucket_name: str):
    try:
        s3_client.head_bucket(Bucket=bucket_name)
    except:
        try:
            s3_client.create_bucket(Bucket=bucket_name)
        except Exception as e:
            print(f"Failed to create bucket {bucket_name}: {e}")
