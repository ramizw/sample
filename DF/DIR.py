import os

cd = os.getcwd()
add = '\Browsers'
print(cd+add)

for k, v in os.environ.items():
    print(f'{k}={v}')