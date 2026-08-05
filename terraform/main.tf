resource "aws_s3_bucket" "evidence" {
  bucket_prefix = "cloud-grc-evidence-"

  tags = {
    Project     = "Cloud GRC Platform"
    Environment = "Lab"
  }
}
