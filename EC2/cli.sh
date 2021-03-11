REGION="sa-east-1"
for INSTANCE_ID in $(aws ec2 describe-instances --query 'Reservations[*].Instances[].[InstanceId]')
do
Name=$(aws ec2 describe-tags --region $REGION --filter "Name=resource-id,Values=$INSTANCE_ID" --output=text | sed -r 's/TAGS\t(.*)\t.*\t.*\t(.*)/\1="\2"/'|grep "Name="|awk -F '=' '{print $2}')
Ambiente=$(aws ec2 describe-tags --region $REGION --filter "Name=resource-id,Values=$INSTANCE_ID" --output=text | sed -r 's/TAGS\t(.*)\t.*\t.*\t(.*)/\1="\2"/'|grep "Environment="|awk -F '=' '{print $2}')
Cliente=$(aws ec2 describe-tags --region $REGION --filter "Name=resource-id,Values=$INSTANCE_ID" --output=text | sed -r 's/TAGS\t(.*)\t.*\t.*\t(.*)/\1="\2"/'|grep "Customer="|awk -F '=' '{print $2}')
PrivateIP=$(aws ec2 describe-instances --instance-ids $INSTANCE_ID|grep PRIVATEIPADDRESSES|awk '{print $4}')
PulblicIP=$(aws ec2 describe-instances --instance-ids $INSTANCE_ID|grep ASSOCIATION|awk '{print $4}'|head -n1)
STATE=$(aws ec2 describe-instances --instance-ids $INSTANCE_ID|grep STATE|awk '{print $3}'|head -n1)
if [ $STATE = "running" ]
then if [ $(nmap 10.0.31.171|grep 3389|wc -l) = 1 ]
    then SO="Windows"
    elif [ $(nmap 10.0.31.171|grep 22|wc -l) = 1 ]
        then SO="Linux"
        
    fi
fi
echo "$INSTANCE_ID, $Name, $STATE, $Ambiente, $Cliente, $SO, $PrivateIP, $PublicIP"
done