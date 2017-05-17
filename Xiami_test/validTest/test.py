import json
import os


if __name__ == "__main__":
    for line in open('songJ.json'):
        try:
            str = json.loads(line)
        except ValueError:
            print('error line:' + line)