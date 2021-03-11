import json
import os
import socket
import boto3

region_list = ["sa-east-1", "us-east-1"]

def check_port (ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    Linux = sock.connect_ex((ip, 22))
    Windows = sock.connect_ex((ip, 3389))
    if Windows == 0:
        so_port = "Windows"
    else:
        so_port = "Indefinido"
    if Linux == 0:
        so_port = "Linux"
    else:
        so_port = "Indefinido"
    return so_port

for region in region_list:
    
    ec2 = boto3.setup_default_session(region_name=region)
    ec2 = boto3.client('ec2')
    data = ec2.describe_instances()

    for Instance in data['Reservations']:
        InsID = (Instance['Instances'][0]['InstanceId'])
            
        for SubIns in Instance['Instances']: 
            if 'KeyName' in SubIns:
                KeyP = (SubIns['KeyName'])
            else:
                KeyP = "Não existe"
            
        PrivIP = (Instance['Instances'][0]['PrivateIpAddress'])
            
        for SubIns in Instance['Instances']: 
            if 'PublicIpAddress' in SubIns:
                PubIP = (SubIns['PublicIpAddress'])
            else:
                PubIP = "Não existe"
                    
        AZ = (Instance['Instances'][0]['Placement']['AvailabilityZone'])
        State = (Instance['Instances'][0]['State']['Name'])
            
        for SubIns in Instance['Instances']: 
            if 'Platform' in SubIns:
                SO = (SubIns['Platform'])
            else:
                if State == "running":
                    SO = check_port(PrivIP)
                else:
                    SO = "SO não encontrado"
                    
        if('Instances' in Instance):
            for Inst in Instance['Instances']:
                if('Tags' in Inst):
                    for tag in Inst['Tags']:
                        Chave = str(tag['Key'])
                        Valor = str(tag['Value'])
                        if (Chave == "Customer"):
                            Cliente = Valor
                        elif (Chave == "Name"):
                            Nome = Valor
                        elif (Chave == "Environment"):
                            Ambiente = Valor
                        elif (Chave == "ServerUse"):
                            Uso = Valor
                        else:                              
                            Cliente = "Não Tageado"
                            Nome = "Não Tageado"
                            Ambiente = "Não Tageado"
                            Uso = "Não Tageado"
            
            
#            linha = (InsID, ' %', Nome, ' %', Cliente, ' %', Ambiente, ' %', Uso, ' %', State, ' %', SO, ' %', AZ, ' %', PrivIP, ' %', PubIP, ' %', KeyP,'\n')
           
#            escrever = open(ec2log, 'a') 
#            escrever.writelines(linha)
#            escrever.close()
            
#            inicio = len(Pasta)
#            with open(ec2log) as cont:
#                atual = sum(1 for _ in cont)
#            progress = atual / inicio * 100
#            os.system('clear')
            
#            print('Processando JSon: {}%'.format(int(progress)))
    print (InsID, '%', Nome, '%', Cliente, '%', Ambiente, '%', Uso, '%', State, '%', SO, '%', AZ, '%', PrivIP, '%', PubIP, '%', KeyP)