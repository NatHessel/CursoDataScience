import platform
import getpass
from datetime import  datetime
#control barra para comentar
# print("Nome máquina...............", platform.node())
# print("Arquitetura................", platform.architecture())
# print("Sistema operacional........", platform.system())
# print("Versao do SO...............", platform.release())
# print("Processador ...............", platform.processor())
# print("Versão do Python...........", platform.python_version())
#
# #informacoes de data do server e maquina
# print(datetime.now())
# print(datetime.now().year)
# print(datetime.now().hour)
# print(datetime.now().month)
# print(datetime.now().day)
# print(datetime.now().minute)


usuario = print(getpass.getuser())
senha = print(getpass.getpass("Digite sua senha: ........."))

if usuario=='nathe' and senha == '105806':
    print('Welcome')
else:
     print ('you dont have access')