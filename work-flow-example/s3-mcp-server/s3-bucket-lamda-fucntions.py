import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    """
    event example:
    {
        "bucket_name": "my-bucket-name",
        "status": "Enabled"  # or "Suspended"
    }
    """
    
    bucket_name = event.get("bucket_name")
    status = event.get("status")  # "Enabled" or "Suspended"
    
    if not bucket_name or status not in ["Enabled", "Suspended"]:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "Invalid input. Provide 'bucket_name' and status ('Enabled' or 'Suspended')."})
        }
    
    try:
        s3.put_bucket_versioning(
            Bucket=bucket_name,
            VersioningConfiguration={
                'Status': status
            }
        )
        
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": f"S3 bucket versioning for '{bucket_name}' set to '{status}'."
            })
        }
    
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps({"error": str(e)})
        }