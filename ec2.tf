resource "aws_instance" "sgc-teste" {
  ami           = var.ami
  instance_type = var.instance_type
  key_name = var.keyname
  subnet_id = var.subnet
  tags = {
      Name = var.name
      Customer = var.customer
  }
  security_groups = [aws_security_group.sgc-teste.id]
  root_block_device {
    volume_size = 40
    delete_on_termination = true
  }
  
}


