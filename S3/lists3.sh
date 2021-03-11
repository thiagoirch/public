for bucket in $(aws s3api list-buckets|awk '{print $3}')
do
size=$(aws s3 ls --human-readable --summarize $bucket|grep "Total Size"|awk -F ':' '{print $2}')
objects=$(aws s3 ls --human-readable --summarize $bucket|grep "Total Objects"|awk -F ':' '{print $2}')
lstupdt=$(aws s3 ls --human-readable --summarize $bucket|grep ^20|awk '{print $1}'|sort -nr|head -n1)
echo "$bucket%$size%$objects%$lstupdt"
done