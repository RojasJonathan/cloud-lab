output "evidence_bucket_name" {
  description = "Name of the audit evidence bucket"
  value = aws_s3_bucket.grc_lab.bucket
}
