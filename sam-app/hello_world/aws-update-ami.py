#! /usr/bin/python3

import argparse
import sys
import boto3
import logging

REGION = "eu-west-1"

logger = logging.getLogger('AMIs')
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.DEBUG)


def help(args = None):

    parser = argparse.ArgumentParser()

    parser.add_argument("--role",                                  
                        help="name the role that we do", default="vy-administrator")
    parser.add_argument("--profile",                               
                        help="user profile", required='True')

    return parser.parse_args()

def session(profile, client_type):
    logger.debug('INFO: (session) Assuming role in account: {}'.format(profile))
    ses = boto3.Session(profile_name=profile)
    return ses.client(client_type)

def update(Options):
    print("update")

def main():

    Options = help(sys.argv[1:])
   
    user = session(Options.profile, 'cloudformation')

    response = user.describe_stacks(StackName='appstack-tst')

    print(response)
    
main()


