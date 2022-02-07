import boto3
import json
ec2 = boto3.client('ec2')
def get_instance_ids():
  all_instances = ec2.describe_instances()
  instance_ids = []
  for reservation in all_instances['Reservations']:
    for instance in reservation['Instances']:
      print("InstanceID",instance['InstanceId'])
      if instance["State"]["Name"]=="running":
        instance_ids.append(instance['InstanceId'])
  return instance_ids
                  
def handler(event, context):
    instance_ids = get_instance_ids()
    if len(instance_ids) != 0:
      ec2.stop_instances(InstanceIds=instance_ids)
    response = "Successfully stopped instances: " + str(instance_ids)
    return {'statusCode': 200,'body': json.dumps(response)}