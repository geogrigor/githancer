import argparse
import subprocess

def run_git_command(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        raise Exception("Error occurred while executing command: ", error)
    else:
        return output.decode("utf-8")


def main():
   print('Bleh')


if __name__ == "__main__":
    main()