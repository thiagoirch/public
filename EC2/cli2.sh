#/bin/sh
dir="/tmp/dev/AWSCLI/fonte"
echo "Deseja Limpar o Cache? (n=cancela, qualquer outro continua)"
read resposta
if [ resposta == "n" ]; then exit; fi
echo "Limpando listas"
> sa-east-1.log
> us-east-1.log
echo "Limpando $dir"
rm -fr $dir/*
echo "Gerando listas"
aws ec2 describe-instances --query 'Reservations[*].Instances[].[InstanceId]' --region sa-east-1 > sa-east-1.log
L1=$(cat sa-east-1.log|wc -l)
echo "Lista 1 sa-east-1 $L1 registros"
aws ec2 describe-instances --query 'Reservations[*].Instances[].[InstanceId]' --region us-east-1 > us-east-1.log
L2=$(cat us-east-1.log|wc -l)
echo "Lista 2 us-east-1 $L2 registros"
inicio=$(($L1+$L2))
echo "Total de registros $inicio"

for iNstanceId in $(cat sa-east-1.log)
do
    aws ec2 describe-instances --instance-ids $iNstanceId --output json --region sa-east-1 > $dir/$iNstanceId.json 

    atual=$(ls $dir|wc -l)
    clear
    echo "Progresso $atual/$inicio"
done 

for iNstanceId in $(cat us-east-1.log)
do
    aws ec2 describe-instances --instance-ids $iNstanceId --output json --region us-east-1 > $dir/$iNstanceId.json 

    atual=$(ls $dir|wc -l)
    clear
    echo "Progresso $atual/$inicio"
done
echo "Processo finalizado"