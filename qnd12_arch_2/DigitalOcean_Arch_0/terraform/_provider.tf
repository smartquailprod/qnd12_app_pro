


variable "digitalocean_token" {
  description = "Digital Ocean Token:qnd12"
  default     = "dop_v1_7e25980f3f9e9797846a6a8b479de102bb982d65ba39ed6a3108e980a5ea37b4"
}

variable "spaces_access_id" {
  description = "Digital Ocean Spaces Acees ID"
  default     = "DO0064XX2WKMXAWNB3NT"
}
variable "spaces_secret_key" {
  description = "Digital Ocean Spaces Secret Key"
  default     = "m4oyT+RU72iYp7wjOXIYQ7MM5ZgFjiU81QlNhj6WXUw"
}

terraform {
  required_version = ">= 0.14.0"  
  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean"
    }
  }
}

# Configure the DigitalOcean Provider

provider "digitalocean" {
  token = var.digitalocean_token
  spaces_access_id  = var.spaces_access_id
  spaces_secret_key = var.spaces_secret_key
}



