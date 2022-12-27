import os

MODULES = ['typer', 'requests', 'typing', 'json']

def install(modules):
    for module in modules:
        os.system(f'pip3 install {module}')

if __name__ == "__main__":
    install(MODULES)
