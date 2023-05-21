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
    parser = argparse.ArgumentParser(description='Run git commands')
    parser.add_argument('command', type=str)
    parser.add_argument('-b', '--branch', type=str, help='The branch to checkout')

    args = parser.parse_args()

    if args.command == '' or args.command == None:
        print('No command specified')
        return

    if args.command == 'checkout':
        if args.branch == '' or args.branch == None:
            print('No branch specified')
            return

        git_command = f'git checkout {args.branch}'
        output = run_git_command(git_command)

        print(output)
    else:
        print('Invalid command')
        return


if __name__ == "__main__":
    main()
