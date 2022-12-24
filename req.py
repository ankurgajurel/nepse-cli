import os

MODULES = ['typer', 'requests', 'typing', 'json']

def install(modules):
    for module in modules:
        os.system(f'pip3 install {module}')

def main():
    install(MODULES)

if __name__ == "__main__":
    install(MODULES)
