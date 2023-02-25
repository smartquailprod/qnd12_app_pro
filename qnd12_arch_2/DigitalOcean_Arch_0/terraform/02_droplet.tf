#
# Creamos el droplet


resource "digitalocean_droplet" "QND12" {
  image     = "ubuntu-22-04-x64"
  name      = "QND12"
  region    = "sfo3"
  size      = "s-2vcpu-2gb"
  user_data = "${file("docker.yaml")}"
  ssh_keys  = ["${digitalocean_ssh_key.qnd12.fingerprint}"]
}

resource "digitalocean_project" "nethousing" {
  name        = "nethousing"
  description = "Proyecto NetHousing"
  purpose     = "Web Application"
  environment = "Development"
  resources   = [digitalocean_droplet.nethousing.QND12]
}
