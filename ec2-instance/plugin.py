import boto3
from cloudify.decorators import operation

service_name = 'ec2'

@operation
def start(*args, **_):

    ctx = _['ctx']
    aws_props = ctx.node.properties['aws_config']
    instance_id = ctx.node.properties['aws_instance_id']
    conn = AWSClinet(service_name, aws_props['region_name'],
                       aws_props['aws_access_key_id'], aws_props['aws_secret_access_key'])

    if ctx.operation.retry_number == 0:
        conn.client.start_instances(InstanceIds=[instance_id])

    # Diving deep into the response dict to get instance state object
    state = conn.client.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]['State']
    if state['Name'] != 'active':
        return ctx.operation.retry(message='Waiting for the instance to become Active',
                                   retry_after=30)
    return


@operation
def stop(*args, **_):
    ctx = _['ctx']
    aws_props = ctx.node.properties['aws_config']
    instance_id = ctx.node.properties['aws_instance_id']
    conn = AWSClinet(service_name, aws_props['region_name'],
                       aws_props['aws_access_key_id'], aws_props['aws_secret_access_key'])

    if ctx.operation.retry_number == 0:
         conn.client.stop_instances(InstanceIds=[instance_id])

    # Diving deep into the response dict to get instance state object
    state = conn.client.describe_instances(InstanceIds=[instance_id])['Reservations'][0]['Instances'][0]['State']
    if state['Name'] != 'stopped':
        return ctx.operation.retry(message='Waiting for the instance to be stopped',
                                   retry_after=30)

    return


class AWSClinet():

    def __init__(self, service_name, region_name, aws_access_key_id, aws_secret_access_key):
        self.client = boto3.client(service_name=service_name, region_name=region_name,
                              aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
