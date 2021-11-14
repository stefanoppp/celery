import socketserver
import argparse
import pickle
import threading

from operaciones import *

parser = argparse.ArgumentParser()
parser.add_argument("-p", "--puerto", dest = "puerto")
parser.add_argument("-h", "--host")
args = parser.parse_args()
HOST=args.host
PUERTO=args.puerto
HEADER=1024

class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        connected = True
        while connected:
            data = self.request.recv(HEADER)
            if data == "quit":
                break
            msj_loaded = pickle.loads(data)
            if msj_loaded[0] == 'resta':
                resultado=resta.delay(msj_loaded[1],msj_loaded[2])
            if msj_loaded[0] == 'suma':
                resultado=suma.delay(msj_loaded[1],msj_loaded[2])
            if msj_loaded[0] == 'mult':
                resultado=mult.delay(msj_loaded[1],msj_loaded[2])
            if msj_loaded[0] == 'pow':
                resultado=power.delay(msj_loaded[1],msj_loaded[2])
            if msj_loaded[0] == 'div':
                resultado=division.delay(msj_loaded[1],msj_loaded[2])
            
            else:
                exit()
        message_send = pickle.dumps(resultado.get())
        self.request.sendall(message_send)


class ThreadTCP(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__":


    msj_loadedServer=((HOST,PUERTO))

    server = ThreadTCP(msj_loadedServer,TCPHandler)

    with server:
        host, puerto = server.server_address
        thread = threading.Thread(target=server.serve_forever)
        thread.daemon = True
        thread.start()

        print(host,puerto)
        server.shutdown() 