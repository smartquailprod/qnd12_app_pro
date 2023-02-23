#
# Creamos el droplet

resource "digitalocean_project" "NetHousing" {
  name        = "NetHousing"
  description = "Proyecto de producción."
  purpose     = "Web Application"
  environment = "Development"
}

resource "digitalocean_droplet" "QND12" {
  image     = "ubuntu-22-04-x64"
  name      = "QND12"
  region    = "sfo3"
  size      = "s-2vcpu-2gb"
  user_data = "${file("docker.yaml")}"
  ssh_keys  = ["${digitalocean_ssh_key.qnd12.fingerprint}"]
}
