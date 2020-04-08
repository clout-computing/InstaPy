import csv
from instapy import InstaPy
from instapy import smart_run
from instapy import set_workspace
from instapy.util import web_address_navigator

from io import BytesIO
import boto3
import boto3.session
from botocore.exceptions import ClientError

cred = boto3.Session().get_credentials()
s3_client = boto3.client('s3')

influencer_list = []

with open('art_influencers.csv', mode='r', encoding='utf-8-sig') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    type=""
    for row in csv_reader:

        if len(row) == 0 or row[0] == "":
            line_count += 1
        elif row[0] == "CELEBRITY":
            type="CELEBRITY"
        elif row[0] == "GALLERIST":
            type="GALLERIST"
        elif row[0] == "CURATOR":
            type="CURATOR"
        elif row[0] == "MUSEUM":
            type="MUSEUM"
        elif row[0] == "ADVISOR":
            type="ADVISOR"
        elif row[0] == "COLLECTOR":
            type="COLLECTOR"
        elif row[0] == "CRITIC":
            type="CRITIC"
        elif row[0] == "OTHER":
            type="OTHER"
        else:
            handle = row[0].replace('@', '')
            tup = (handle, type)
            influencer_list.append(tup)
            print("credentials are {}".format(tup))
        line_count += 1

print(influencer_list)


# for cred_tup in credentials_list:
    
#     try:

#         try:
#             response = s3_client.get_object(Bucket='clarus-bot-data', Key='{username}/{username}_cookie.pkl'.format(username=cred_tup[0]))

#             if response:
#                 continue

#         except Exception as e:
#             print("no cookie! Making one...")

#         session = InstaPy(username=cred_tup[0],
#                     password=cred_tup[1],
#                     headless_browser=True,
#                     nogui=True)

#         with smart_run(session):
#             # activity

#             try:
#                 cookie_name = "{0}{1}_cookie.pkl".format(session.logfolder, session.username)
#                 # with open("{0}{1}_cookie.pkl".format(session.logfolder, session.username), "r") as cookie:
#                 # bucket = s3_client.create_bucket(Bucket='clarus-bot-data/{}'.format(session.username))
#                 response = s3_client.upload_file(cookie_name, "clarus-bot-data", "{0}/{1}_cookie.pkl".format(session.username, session.username))
#             except ClientError as e:
#                 logging.error(e)
#     except Exception as e:
#         print("error! Continuing... {}".format(e))