import json
import os
import socket
import boto3

HOME = "C:/temp/Dev/AWS/EBS"
region_list = ["us-east-1", "sa-east-1"]
Pasta = os.listdir("{}/fonte".format(HOME))
ec2log = str("{}/ebs.txt".format(HOME))

Total = []
open(ec2log, 'w').close()
for region in region_list:
    
    ec2 = boto3.setup_default_session(region_name=region)
    ec2 = boto3.client('ec2')
    #data = ec2.describe_instances(InstanceIds=[ids])
    data = ec2.describe_instances()
    
    
    for Instance in data['Reservations']:
        InsID = (Instance['Instances'][0]['InstanceId'])
        Total.append(InsID) 

    for Instance in data['Reservations']:
        InsID = (Instance['Instances'][0]['InstanceId'])
            
        for SubIns in Instance['Instances']: 
            if 'KeyName' in SubIns:
                KeyP = (SubIns['KeyName'])
            else:
                KeyP = "Não existe"
            
        for SubIns in Instance['Instances']:
            if 'PrivateIpAddress' in SubIns:
                PrivIP = (SubIns['PrivateIpAddress'])
            else:
                PrivIP = "Não Existe"
                
        
        InType = (Instance['Instances'][0]['InstanceType'])
            
        for SubIns in Instance['Instances']: 
            if 'PublicIpAddress' in SubIns:
                PubIP = (SubIns['PublicIpAddress'])
            else:
                PubIP = "Não existe"
                    
        AZ = (Instance['Instances'][0]['Placement']['AvailabilityZone'])
        State = (Instance['Instances'][0]['State']['Name'])
            
        Cliente = "Não Tageado"
        Ambiente = "Não Tageado"
        Nome = "Não Tageado"
        Uso = "Não Tageado"
        Distro = "Não Tageado"
        OSVer = "Não Tageado"
        SO = "Não Tageado"       
        if('Instances' in Instance):
            for Inst in Instance['Instances']:
                if('BlockDeviceMappings' in Inst):
                    for device in Inst['BlockDeviceMappings']:
                        Chave = str(device['Key'])
                        Valor = str(device['Value'])
                        if (Chave == "DeviceName"):
                            Disco = Valor
    linha = (InsID, ' %', Disco,'\n')
            #linha = (PrivIP," ", Nome, '\n')
        
    print(linha)
     #   escrever = open(ec2log, 'a') 
     #   escrever.writelines(linha)
     #   escrever.close()
            
    #        escrever = open('/etc/hosts', 'a') 
    #        escrever.writelines(linha)
    #        escrever.close()
            
    #    inicio = len(Total)
    #    with open(ec2log) as cont:
    #        atual = sum(1 for _ in cont)
    #    progress = atual / inicio * 100
    #    os.system('cls')
    #    print(len(Total))    
    #    print('Processando JSon: {}%'.format(int(progress)))    