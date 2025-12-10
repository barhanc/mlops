variable "bucket_name_prefix" {
  type        = string
  default     = "lab-terraform-bucket"
  description = "Prefix for the S3 bucket name."
}

variable "region" {
  type        = string
  default     = "us-east-1"
  description = "AWS region."
}

variable "random_suffix" {
  type        = string
  description = "Random suffix for the S3 bucket name to ensure uniqueness."
}

variable "lifecycle_days" {
  type        = number
  default     = 90
  description = "Number of days before objects are transitioned to the specified storage class."
}

variable "lifecycle_storage_class" {
  type        = string
  default     = "GLACIER"
  description = "The storage class to which objects will transition after the specified number of days."
}
