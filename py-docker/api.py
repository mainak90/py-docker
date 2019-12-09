import requests
import logging
import os.path
import json
import base64
import link_header
import collections
from .errors import TagNotFound, RepoNotFound
from .registry import Registry

class API(object):
    def __init__(self, host, insecure=False, config_file="~/docker/config.json"):
        logging.debug("Creating new registry api: host=%s, insecure=%s, config_file=%s", host, insecure, config_file)
        self.registry = Registry(host, insecure)

        self.config_file = config_file
        if self.config_file:
            config_file_path = os.path.expanduser(config_file)
            try:
                with open(config_file_path, 'r') as f:
                    config_file = json.loads(f.read())
                    try:
                        auth = config_file["auths"]["host"]["auth"]
                        self.user, self.password = base64.b64decode(auth).split(":", 1)
                    except KeyError:
                        pass
            except IOError as e:
                logging.warning("Error while openning docker config file %s", e)

    def Base(self):
        return self.Base(self.registry)

    def Catalog(self):
        return self.Catalog(self.registry)

    def Tags(self, name):
        return self.Tags(self.registry, name)

    def Manifest(self, name, reference):
        return self.Manifest(self.registry, name, reference)

    def Blob(self, name, digest):
        return self.Blob(self.registry, name, digest)


