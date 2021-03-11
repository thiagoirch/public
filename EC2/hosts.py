import json
import os
import socket
import boto3

HOME = "c:/temp/Dev/AWSCLI"
region_list = ["us-east-1", "sa-east-1"]
Pasta = os.listdir("{}/fonte".format(HOME))
ec2log = str("{}/ec2.txt".format(HOME))

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
            
        #for SubIns in Instance['Instances']: 
        #    if 'Platform' in SubIns:
        #        SO = (SubIns['Platform'])
        #    else:
        #        if State == "running":
        #            SO = check_port(PrivIP)
        #        else:
        #            SO = "SO não encontrado"
        Cliente = "Não Tageado"
        Ambiente = "Não Tageado"
        Nome = "Não Tageado"
        Uso = "Não Tageado"
        Distro = "Não Tageado"
        OSVer = "Não Tageado"
        SO = "Não Tageado"       
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
                        elif (Chave == "OS"):
                            SO = Valor
                        elif (Chave == "OS-Distr"):
                            Distro = Valor
                        elif (Chave == "OS-Ver"):
                            OSVer = Valor
                            #else:                              
                            #    Cliente = "Não Tageado"
                            #    Nome = "Não Tageado"
                            #    Ambiente = "Não Tageado"
                            #    Uso = "Não Tageado"
            
            
        #linha = (InsID, ' %', Nome, ' %', InType, ' %', Cliente, ' %', Ambiente, ' %', Uso, ' %', State, ' %', SO, ' %', Distro, ' %', OSVer, ' %', AZ, ' %', PrivIP, ' %', PubIP, ' %', KeyP,'\n')
        linha = (PrivIP," ", Nome, '\n')
        
    #    escrever = open(ec2log, 'a') 
    #    escrever.writelines(linha)
    #    escrever.close()
            
        escrever = open('/tmp/hosts', 'a') 
        escrever.writelines(linha)
        escrever.close()
            
        inicio = len(Total)
        with open(ec2log) as cont:
            atual = sum(1 for _ in cont)
        progress = atual / inicio * 100
        os.system('clear')
        print(len(Total))    
        print('Processando JSon: {}%'.format(int(progress)))    