import json
import os
import socket
import boto3

region_list = ["us-east-1", "sa-east-1"]

for region in region_list:
    client = boto3.client('autoscaling',region_name=region)
    data = client.describe_auto_scaling_groups()
    for ASG in data['AutoScalingGroups']:
        #ASGNAME = str(Instance['AutoScalingGroups'][0]['AutoScalingGroupName'])
        ASGNAME = (ASG['AutoScalingGroupName'])
        #LCNAME = (ASG['LaunchConfigurationName'])
        if 'LaunchConfigurationName' in ASG:
                LCNAME = (ASG['LaunchConfigurationName'])
        else:
                LCNAME = "Não Encontrado LC"
        print(ASGNAME, LCNAME)
