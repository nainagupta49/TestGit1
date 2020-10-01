
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='honeypot prototype')
    parser.add_argument('-addr','--address',help='server ip address to use',action='store', required=True)
    parser.add_argument('-portno','--portno',help='server port to use',action='store', required=True)
    args = parser.parse_args()
    honey(args.address,args.portno)
