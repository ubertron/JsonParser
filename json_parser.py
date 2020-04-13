#!/usr/bin/env python

import os
import json


class JsonParser:
    def __init__(self):
        self.data = None

    def decode(self, json_path, fmt=True):
        if os.path.isfile(json_path):
            with open(json_path) as f:
                self.data = json.load(f)
            if fmt:
                self.format_data()
        else:
            self.data = None

    def format_data(self):
        for key, value in self.data.items():
            print(f'Key: {key}\tValue: {value}')


if __name__ == '__main__':
    JsonParser().decode('services.json')
