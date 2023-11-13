# ## Organizador de Arquivos

# 1. Nesse exercício vamos colocar em prática o que aprendemos nas aulas anteriores. 
# 2. O seu desafio é criar um programa em Python que organiza arquivos de acordo com os seguintes tipos de arquivo:
# - exe
# - csv
# - jpg
# - pdf
# - zip

import os

# 1 - diretório raiz do SO
base_path = os.path.expanduser('~')

# 2 - navegando no diretório Downloads
path = os.path.join(base_path, 'Downloads')

cwd = os.chdir(path)

# 3 - list arquivos do diretório
list_files = os.listdir(cwd)
print(list_files)

# 4 - criar pastas
type_files = ['exe', 'csv', 'mkv', 'psd', 'pptx', 'pdf', 'png', 'jpeg', 'zip', 'xlsx','py', 'svg', 'fbx', 'docx', 'gif', 'sfk', 'mp4', 'htm', 'rmskin', 'msi']

for type in type_files:
    if type not in os.listdir():
        os.mkdir(type)
        
# 5 - organizando arquivos
for file in list_files:
    for type in type_files:
        if '.' + type in file:
            old_path = os.path.join(path, file)        
            new_path = os.path.join(path, type, file)
            os.replace(old_path, new_path)

