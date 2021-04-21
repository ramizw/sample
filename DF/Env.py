import os

#print(os.environ)

#for k, v in os.environ.items():
#    print(f'{k}={v}')

def environmentSetup():

    cd = os.getcwd()
    add = '\Browsers'
    print(cd+add)
    readypath = cd+add

    os.environ['PATH'] = readypath

    env_var = 'PATH'

    if env_var in os.environ:
        print(f'{env_var} value is {os.environ[env_var]}')
    else:
        print(f'{env_var} does not exist')


print(environmentSetup())