from google.cloud import secretmanager
#from listentothis import env

# GCP project in which to store secrets in Secret Manager.
PROJECT_ID = 'listen-to-this-280113'

# ID of the secret to create.
SECRET_ID = 'test-scret'

client = secretmanager.SecretManagerServiceClient()
