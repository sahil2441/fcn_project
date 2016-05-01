
import json
import sys

def indent():
    file = open('logs')
    parsed = json.load(file)

    # create new file
    # print the generated machine code into new file

    filename =  'logs_json'
    f = open(filename, 'w')
    print >>f , parsed
    f.close()

if __name__ == '__main__':
    indent()