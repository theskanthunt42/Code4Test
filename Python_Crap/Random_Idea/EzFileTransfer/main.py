import sys
import argparse
import socket
import tqdm
import json

def 

def main():
    listen_address = '0.0.0.0' #Default address to listen on
    destination_address = '127.0.0.1' #Default address to connect
    port = 35520 #Default port
    buffer_size = 4096 #Idk is this really need to care about much anyway?
    mode = 'server'
    file_location = ''
    file_stats = False
    parser = argparse.ArgumentParser()
    parser.add_argument('-m', '--mode', type=str, help='Selecting modes bewteen "client" or "server".')
    parser.add_argument('-p', '--port', type=int, help='Customize the port for use(Default: 35520)')
    parser.add_argument('-a', '--address', type=str, help='The IPv4 address to listen on/connect to\nIf this leave blank the address will be 127.0.0.1')
    parser.add_argument('-b', '--buffer', type=int, help='Buffer size when sending files(Default: 4096)')
    parser.add_argument('-i', '--input-file', type=str, help='The file to send when using as client mode.')
    args = parser.parse_args()
    

if __name__ == '__main__':
    main()

