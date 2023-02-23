#
# Exportamos nuestra key SSH

resource "digitalocean_ssh_key" "qnd12" {
  name       = "qnd12"
  public_key = "${file("id_rsa.pub")}"
}

