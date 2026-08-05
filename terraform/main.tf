resource "aws_s3_bucket" "evidence" {
  bucket_prefix = "cloud-grc-evidence-"

  tags = {
    Project     = "Cloud lab"
    Environment = "Lab"
  }
}
