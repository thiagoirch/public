for bucket in $(aws s3api list-buckets --query Buckets[*].Name --output text); do

  echo "$bucket"

  aws s3api list-multipart-uploads --bucket "$bucket" --query Uploads[*].[Key,UploadId,Initiated,Initiator.DisplayName] --output text  | while read key id date user; do

   [[ "$key" == "None" ]] #&& continue

    echo "Press enter to abort s3://$bucket/$key (initiated $date by $user)"

    read < /dev/tty

    aws s3api abort-multipart-upload --bucket "$bucket" --key "$key" --upload-id "$id"

  done

done
