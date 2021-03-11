#/bin/sh
aws ec2 describe-instances --query 'Reservations[*].Instances[].[InstanceId]' --region sa-east-1 > InstanceId.txt
aws ec2 describe-instances --query 'Reservations[*].Instances[].[InstanceId]' --region us-east-1 >> InstanceId.txt


