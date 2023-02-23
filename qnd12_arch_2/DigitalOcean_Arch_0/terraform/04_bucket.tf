resource "digitalocean_spaces_bucket" "qnd12-staticfiles" {
  name   = "qnd12-staticfiles"
  region = "sfo3"
  acl = "public-read"
}

