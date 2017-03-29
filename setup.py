from setuptools import setup

setup(
    name='stack-deploy',
    version='0.1',
    scripts=['stack-deploy'],
    install_requires=[
        'appdirs==1.4.0',
        'boto3==1.4.4',
        'botocore==1.5.7',
        'docutils==0.13.1',
        'futures==3.0.5',
        'jmespath==0.9.1',
        'packaging==16.8',
        'pyaml==16.12.2',
        'pyparsing==2.1.10',
        'python-dateutil==2.6.0',
        'PyYAML==3.12',
        's3transfer==0.1.10',
        'six==1.10.0',
        'termcolor==1.1.0' ]
)

