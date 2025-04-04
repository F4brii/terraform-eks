variable "aws_region" {
  description = "AWS region"
  type        = string
}

variable "tags" {
  description = "Tags to assign to the role"
  type        = map(string)
  default     = {}
}