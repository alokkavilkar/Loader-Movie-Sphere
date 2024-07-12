"""
Loader Module
Module for Loader package.
"""
import json
import os
from dotenv import load_dotenv
import boto3

load_dotenv()

# SQS configuration
sqs = boto3.client('sqs', region_name='us-east-1')
queue_url = os.getenv('SQS_URL')

def load_movies(file_path):
    """
    Load movies from a JSON file and send each movie title to an SQS queue.
    Args:
        file_path (str): The path to the JSON file containing movie data.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            movies = json.load(file)
            for movie in movies:
                response = sqs.send_message(
                    QueueUrl=queue_url,
                    MessageBody=movie['Title']
                )
                print(f"Sent {movie['Title']} to SQS, MessageID: {response['MessageId']}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as general_e:
        # print(f"An error occurred: {general_e}")
        pass


if __name__ == "__main__":
    load_movies('movies.json')
