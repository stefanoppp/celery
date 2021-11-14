import argparse
import pickle
import socket


parser = argparse.ArgumentParser()
parser.add_argument("-h", "--host",default='localhost')
parser.add_argument("-p", "--puerto", default=5050)
parser.add_argument("-o", "--operacion", help="(suma, resta, div, pow, mult)")
parser.add_argument("-n", "--n1", dest="n1")
parser.add_argument("-m", "--n2", dest="n2")
args = parser.parse_args()

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HEADER=1024
HOST = args.host
PUERTO = args.puerto
ADDR = ((HOST, PUERTO))
socket.connect(ADDR)

if __name__ == "__main__":
    msg = [args.operacion, args.n1, args.n2]
    message_send = pickle.dumps(msg)
    socket.sendall(message_send)
    data = socket.recv(HEADER)
    resultado = pickle.loads(data)
    print("Resultado: " + str(resultado))
    socket.close()