for bucket in $(aws s3api list-buckets --query "Buckets[].Name" --output text); do

    aws s3api put-bucket-lifecycle-configuration --bucket ${bucket} --lifecycle-configuration file://s3-3days.json

done
