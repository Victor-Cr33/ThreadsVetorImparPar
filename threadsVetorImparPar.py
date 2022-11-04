import threading 
from threading import Thread
import time

vetor = [1,2,3,4,5,6,7,8,9,10]


def verificarNumPar():
  
  for i in range (0,10):
    print(f"{threading.current_thread().name} Buscando numero Par")
    if(vetor[i]%2 ==0):
     print( "par:", vetor[i])
    time.sleep(2)

def verificarNumImpar():
  
  for i in range (0,10):
    print(f"{threading.current_thread().name} Buscando numero Impar")
    if(vetor[i]%2):
     print( "impar:", vetor[i])
    time.sleep(2)

if __name__ == "__main__":

  print(f"{threading.current_thread().name} Iniciando")

  print(f"{threading.current_thread().name} Criando Threads")
  threads=[]
  
  threadPar = Thread(target=verificarNumPar)
  threadImpar = Thread(target=verificarNumImpar)
  threadPar.start()
  threadImpar.start()
  threads.append(threadPar)
  threads.append(threadImpar)
  
  for i in threads:
    i.join()
    print(f"{threading.current_thread().name} Finalizando..")  
