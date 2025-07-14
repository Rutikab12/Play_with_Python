#!/bin/bash

gcloud beta data-fusion instances list --location=europe-west1 --format="value(apiEndpoint)"
export AUTH_TOKEN=$(gcloud auth print-access-token)
export REGION=europe-west1
export CDAP_ENDPOINT=$(gcloud beta data-fusion instances list --location=europe-west1 --format="value(apiEndpoint)")
export ns=$1
export file_names=$(grep '^[[:space:]]*- ' config.yaml | sed 's/^[[:space:]]*- //')
export source_path="./Pipeline"
export destination_path="./Pipeline2Deploy"

mkdir $destination_path

for file_name in $file_names; do

  source_file="$source_path/$file_name"
  destination_file="$destination_path/$file_name"

  cp "$source_file" "$destination_file"
  
  if [ $? -eq 0 ]; then
    echo "Moved $file_name to $destination_path successfully."
  else
    echo "Failed to move $file_name."
  fi
done

for pipeline in ./$destination_path/*
do
    pipelineName=$(basename $pipeline .json)
    echo -e "\n${pipelineName}"
    curl -X DELETE -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/$1/apps/${pipelineName}"
    curl -X PUT -T "${pipeline}" -H "Authorization: Bearer ${AUTH_TOKEN}" "${CDAP_ENDPOINT}/v3/namespaces/$ns/apps/${pipelineName}"
done


