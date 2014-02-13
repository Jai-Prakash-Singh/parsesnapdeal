import subprocess

def main():
     output = subprocess.check_output(['python', 'code1.py'])
     output2 = subprocess.check_output(['python', 'code2.py'])


if __name__=="__main__":
    main()
