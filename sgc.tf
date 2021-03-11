resource "aws_security_group" "sgc-teste" {
  name        = "sgc-teste"
  description = "terraform create"
  vpc_id      = "vpc-0c98fd52fbbc3a3a1"

  ingress {
    description = "TLS from VPC"
    from_port   = 0
    to_port     = 0
    protocol    = "tcp"
    cidr_blocks = [ "10.0.0.0/8", "11.0.0.0/8", "192.168.5.0/24", "192.168.10.0/24", "192.168.15.0/24", "172.28.0.0/16"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "SGC-Teste"
  }
}