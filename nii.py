import os
import sys
import enc
import dec

args = sys.argv
rds = ['-e', '-d']

def layout_help():
    help_content = '''
    Novel_In_Image v0.2

    Usage: python {} [[-e|-d filename]|-h|-i]

    -e : Encode the file
    -d : Decode the file
    -h : View this help page
    -i : Install the dependencies
    '''.format(sys.argv[0])
    print(help_content)
    return

def install_dependencies():
    os.system('pip install pillow')
    os.system('pip3 install pillow')
    return

def raise_err():
    help_content = '''
    Unknown argument: "{}"

    Type "python {} -h" to see the usage.
    '''.format(sys.argv[1], sys.argv[0])
    print(help_content)
    return

if __name__ == '__main__':
    if len(args) == 1 or (len(args) == 2 and args[1] == '-h'):
        layout_help()
    elif len(args) == 2 and args[1] == '-i':
        install_dependencies()
    elif len(args) == 3 and args[1] in rds:
        if args[1] == rds[0]:
            enc.main(args[2])
        else:
            dec.main(args[2])
    else:
        raise_err()
