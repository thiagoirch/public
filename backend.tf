provider "aws" {
    region = var.region
    shared_credentials_file = "/home/thiagoirch/.aws/credentials"
    profile = "default"
}
