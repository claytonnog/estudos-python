import os
import os.path
import shutil
from pathlib import Path

# Criar path caso nao existe
if not os.path.exists('aulinha_1'):
    os.mkdir('aulinha_1')

os.chdir('aulinha_1')

# criando arquivos - maneira 1
# f = open('aulinha_1/xpto.txt', 'w')
# f.write('')
# f.close()

# criando arquivos - maneira 2
# with open('aulinha_1/xpto.txt', 'w') as f:
# f.write('')

# Criar arquito xpto - maneira 3
Path('xpto.txt').touch()

for el in range(1, 4):
    shutil.copy('xpto.txt', f'xpto_{el}.txt')


# shutil.copy('xpto.txt', 'xpto_1.txt')
# shutil.copy('xpto.txt', 'xpto_2.txt')
# shutil.copy('xpto.txt', 'xpto_3.txt')

# print(os.getcwd())

assert len(os.listdir('.')) == 4

# arquivos_aula = os.listdir('.')
# print(arquivos_aula)




