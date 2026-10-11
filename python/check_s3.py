import boto3

# Loud our AWS CLI profile
session = boto3.Session(profile_name="cloud-lab")

# Create an S3 client
s3 = session.client("s3")

# Request a list of S3 buckets
response = s3.list_buckets()

# Display each bucket name
for bucket in response["Buckets"]:
    print(bucket["Name"])

# Select the S3 bucket we want to audit
bucket_name = "grc-cloud-lab-1afbb4f001dd19f5c3dabdacba"

# Request the bucket's versioning configuration
versioning = s3.get_bucket_versioning(Bucket=bucket_name)

# Extract the versioning status
status = versioning.get("Status", "Disabled")

# Display the result
print("Versioning status:", status)

if status== "Enabled":
    print("Control S3-001: PASS")
else:
    print("Control S3-001: FAIL")

# Retrive the bucket's public access block settings
public_access = s3.get_public_access_block(Bucket=bucket_name)

#Extract the configuration
config = public_access["PublicAccessBlockConfiguration"]

#Check whether all four protections are enabled
if all(config.values()):
    print("Control S3-002: PASS")
else:
    print("Control S3-002: FAIL")