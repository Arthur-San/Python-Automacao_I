from pathlib import Path
from datetime import datetime

path = Path('files', 'dados2', 'teste.txt')

# print(path.stat())

stats = path.stat()
second_created = stats.st_ctime

date_created = datetime.fromtimestamp(second_created)
# print(date_created)
date_created_str = date_created.strftime('%Y-%m-%d/%H-%M-%S')
print(date_created_str)