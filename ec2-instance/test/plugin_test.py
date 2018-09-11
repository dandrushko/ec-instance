import unittest
import os

from cloudify.test_utils import workflow_test



class TestPlugin(unittest.TestCase):

    @workflow_test('test_blueprint.yaml',
        resources_to_copy=[(os.path.join('../../', 'plugin.yaml'), 'plugin/')],
                      inputs={
                      'aws_access_key_id': '',
                      'aws_secret_access_key': '',
                      'ec2_region_name': '',
                      'aws_instance_id': '',
                      'service_name': 'ec2'
                  })
    def test_aws_instance(self, cfy_local):

        #raw_input("Press any key")
        cfy_local.execute('install', task_retries=1)
        raw_input("Press any key")


