from enum import Enum
from google.cloud import secretmanager
import google.auth
import json

class Mode(Enum):
    NOTDEFINED = 0
    GCLOUD = 1
    JSON = 2
    GCLOUD_JSON = 3

def defaultFetcher(x):
    raise Exception("Env not setup, cannot load secret" + x)

class Env:
    fetcher = defaultFetcher 
    unused = True
    mode = Mode.NOTDEFINED

    def get(self, secret: str):
        return self.fetcher(secret)

    def setupJson(self, jsonfile: str):        
        self.mode = Mode.JSON
        with open(jsonfile, "r") as read_file:
            data = json.load(read_file)
        
        def fetcher(secret_name):
            return data[secret_name]

        self.fetcher = fetcher

    def setupGCloudJson(self, secret_name: str):
        self.mode = Mode.GCLOUD_JSON
        client = secretmanager.SecretManagerServiceClient()
        _credentials, project = google.auth.default()

        secret_path = client.secret_version_path(project, secret_name, "latest")
        response = client.access_secret_version(secret_path)
        payload = response.payload.data.decode('UTF-8')

        data = json.loads(payload)

        def fetcher(secret_name):
            return data[secret_name]

        self.fetcher = fetcher


    def setupGCloud(self):
        self.mode = Mode.GCLOUD
        client = secretmanager.SecretManagerServiceClient()
        _credentials, project = google.auth.default()
        def fetcher(secret_name):
            secret_path = client.secret_version_path(project, secret_name, "latest")
            response = client.access_secret_version(secret_path)
            payload = response.payload.data.decode('UTF-8')

            return payload
        
        self.fetcher = fetcher

