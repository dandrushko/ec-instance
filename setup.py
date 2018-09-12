from setuptools import setup


setup(

    # Do not use underscores in the ec2-instance name.
    name='ec2-instance-start-stop',

    version='0.1',
    author='Dmitriy Andrushko',
    author_email='dandrushko@mirantis.com',
    description='Small ec2-instance to suspend resume EC2 instances',

    # This must correspond to the actual packages in the ec2-instance.
    packages=['ec2-instance'],

    license='GPL2',
    zip_safe=False,
    install_requires=[
        # Necessary dependency for developing plugins, do not remove!
        "cloudify-common>=4.4",
        "cloudify-plugins-common>=4.3.3",
        "boto3"
    ],
    test_requires=[
        "cloudify-common>=4.4"
    ]
)