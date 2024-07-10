import boto3
import json
from dotenv import load_dotenv
import os

load_dotenv()

# SQS configuration
sqs = boto3.client('sqs', region_name='us-east-1')
queue_url = os.getenv('SQS_URL')

def load_movies(file_path):
    with open(file_path, 'r') as file:
        movies = json.load(file)
        for movie in movies:
            response = sqs.send_message(
                QueueUrl=queue_url,
                MessageBody=movie['Title']
            )
            print("Sent {} to SQS, MessageID: {}".format(movie['Title'], response['MessageId']))

if __name__ == "__main__":
    load_movies('movies.json')
