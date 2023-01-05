import os

MODULES = open('requirements.txt','r').readlines()
def install(modules):
    for module in modules:
        os.system(f'pip3 install {module}')

if __name__ == "__main__":
    install(MODULES)
