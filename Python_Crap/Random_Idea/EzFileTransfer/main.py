import sys
import getopt

def main(argv):
    listen_address = '0.0.0.0'
    port = 35520
    buffer_size = 4096
    try:
        opts, args = getopt.getopt(argv,"csp:a:b:i:",["port=", "address=", "buffer=", "filein="])
    except getopt.GetoptError:
        print("Use 'python3 main.py -h' for help")
        raise SystemExit
    for opt, arg in opts:
        

if __name__ == '__main__':
    main(sys.argv[1:])

