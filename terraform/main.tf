resource "aws_s3_bucket" "grc_lab" {
  bucket_prefix = "grc-cloud-lab-"

  tags = {
    Project     = "Cloud GRC Lab"
    Environment = "Lab"
  }
}

# Control 1: Block public access
resource "aws_s3_bucket_public_access_block" "grc_lab" {
  bucket = aws_s3_bucket.grc_lab.id

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

# Control 2: Enable versioning
resource "aws_s3_bucket_versioning" "grc_lab" {
  bucket = aws_s3_bucket.grc_lab.id

  versioning_configuration {
    status = "Enabled"
  }
}

# Control 3: Encryption at rest
resource "aws_s3_bucket_server_side_encryption_configuration" "grc_lab" {
  bucket = aws_s3_bucket.grc_lab.id

  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}
