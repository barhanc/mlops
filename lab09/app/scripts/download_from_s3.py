import os
import boto3

S3 = boto3.resource("s3")
BUCKET = "mlops-lab9-s3-bucket"


def download_s3_folder(bucket_name: str, s3_folder: str, local_dir: str | None = None) -> None:
    # Source -
    # https://stackoverflow.com/questions/49772151/download-a-folder-from-s3-using-boto3
    # Posted by bjc, modified by community. See post 'Timeline' for change history
    # Retrieved 2025-12-05, License - CC BY-SA 4.0
    """
    Download the contents of a folder directory
    Args:
        bucket_name: the name of the s3 bucket
        s3_folder: the folder path in the s3 bucket
        local_dir: a relative or absolute directory path in the local file system
    """
    bucket = S3.Bucket(bucket_name)
    for obj in bucket.objects.filter(Prefix=s3_folder):
        target = obj.key if local_dir is None else os.path.join(local_dir, os.path.relpath(obj.key, s3_folder))
        if not os.path.exists(os.path.dirname(target)):
            os.makedirs(os.path.dirname(target))
        if obj.key[-1] == "/":
            continue
        bucket.download_file(obj.key, target)


if __name__ == "__main__":
    download_s3_folder(BUCKET, "model", "artifacts")
