variable "regions" {
  type        = list(string)
  default     = ["us-east-1", "us-west-2"]
  description = "List of AWS regions to create buckets in."
}

variable "bucket_name_prefix" {
  type        = string
  default     = "multi-region-bucket"
  description = "Prefix for the S3 bucket name."
}
