variable "region" {
  default = "us-east-1"
}

variable "name" {
  description = "Name of the Application"
  default = "thiago_teste"
}

variable "ami" {
  default = "ami-0885b1f6bd170450c"
}

variable "instance_type" {
  default = "t2.micro"
}

variable "customer" {
  default = "Infraestrutura"
}

variable "subnet" {
  default = "subnet-052309068b8f27fed"
}

variable "keyname" {
    default = "mc1keylinuxvirginia"
  
}