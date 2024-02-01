import sys
import socket
from helper import whois_servers


'''
The whois function takes a domain name as input.

Methodology:

    1. We have a dictionary of WHOIS servers called whois_servers located in /helper/whois_server.py. This dictionary maps top-level domains (TLDs) to their respective WHOIS servers.

    2. The domain name is split into its components, for example, "example.ie.ie" becomes ["example", "ie", "ie"].

    3. We check if the dictionary contains the TLD and its associated WHOIS server.

    4. A connection is established to the WHOIS server on port 43, following the guidelines outlined in RFC 3912.

    5. The response from the server is returned.
'''
def whois(domain):
    servers = whois_servers.whois_servers

    domain_fixes = domain.split('.')
    domain_fixes.pop(0)

    domain_ext = ''

    for dom in domain_fixes:
        domain_ext += dom

    if domain_ext not in servers:
        print('Error while running the script!')
        print('Usage: python /path/to/main.py example.com')

    else:
        HOST = servers[domain_ext]
        PORT = 43

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.connect((HOST, PORT))
                print('Server Connection established successfully!!!')

                s.sendall((domain + "\r\n").encode())

                response = b''
                while True:
                    data = s.recv(1024)
                    if not data:
                        break
                    response += data

                return response.decode()

            except:
                print('Connection refused!!!')


if __name__ == '__main__':
    
    '''
    example usage:
    
        input:
            >>> python main.py example.com
        
        output:
            Server Connection established successfully!!!
            Domain Name: 
            Registry Domain ID:
            Registrar WHOIS Server:
            Registrar URL:
            ....
            ....

    '''
    if len(sys.argv) != 2:
        print('Error while running the script!')
        print('Usage: python /path/to/main.py example.com')

    else:
        domain = sys.argv[1]

        domain_fixes = domain.split('.')

        if domain_fixes[1] == 'www':
            print('Error while running the script!')
            print('Usage: python /path/to/main.py example.com')

        else:
            whois_result = whois(domain)
            print(whois_result)
