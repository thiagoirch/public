region="us-east-1"
for instanceid in $(cat us-east.txt|awk '{print $1}')
do
device=$(cat us-east.txt|grep "$instanceid"|awk '{print $2}')
volid=$(aws ec2 describe-volumes  --region $region --filters Name=attachment.instance-id,Values="$instanceid" Name=attachment.device,Values="$device" --query 'Volumes[*].VolumeId' --output text)
aws ec2 create-tags --region $region --resources "$volid" --tags Key=AWSBackup,Value=BKPUSE1PD1-EC2
echo "$instanceid"
done

region="sa-east-1"
for instanceid in $(cat sa-east.txt|awk '{print $1}')
do
device=$(cat sa-east.txt|grep "$instanceid"|awk '{print $2}')
volid=$(aws ec2 describe-volumes  --region $region --filters Name=attachment.instance-id,Values="$instanceid" Name=attachment.device,Values="$device" --query 'Volumes[*].VolumeId' --output text)
aws ec2 create-tags --region $region --resources "$volid" --tags Key=AWSBackup,Value=BKPSAE1PD1-EC2
echo "$instanceid"
done
