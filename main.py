"""Main gcloud function entry point"""

import base64
from google.cloud import secretmanager
import google.auth

# GCP project in which to store secrets in Secret Manager.
PROJECT_ID = 'listen-to-this-280113'

# ID of the secret to create.
SECRET_ID = 'test-scret'


client = secretmanager.SecretManagerServiceClient()


def hello_pubsub(event, context):
    """Triggered from a message on a Cloud Pub/Sub topic.
    Args:
         event (dict): Event payload.
         context (google.cloud.functions.Context): Metadata for the event.
    """
    print("From github! 2")
    print("event: ", event)
    print("context: ", context)

    credentials, project = google.auth.default()
    print("creds:", credentials)
    print("proj:", project)

    secret_name = client.secret_version_path(PROJECT_ID, SECRET_ID, "latest")
    response = client.access_secret_version(secret_name)
    payload = response.payload.data.decode('UTF-8')
    print('Plaintext: {}'.format(payload))

    pubsub_message = base64.b64decode(event['data']).decode('utf-8')
    print(pubsub_message)
