import argparse
import subprocess
import datetime


def run_git_command(command):
    process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()

    if error:
        raise Exception('Error occurred while executing command: ', error)
    else:
        return output.decode('utf-8').strip()


def auto_stash():
    current_time = datetime.datetime.now().strftime('%H:%M:%S')
    current_branch = run_git_command('git rev-parse --abbrev-ref HEAD')
    stash_name = f'githancer-auto-stash {current_branch} {current_time}'
    git_command = f'git stash save {stash_name}'
    output = run_git_command(git_command)

    print(output)


def apply_branch_stash(branch):
    stashes = run_git_command('git stash list')
    stash_startswith = f'githancer-auto-stash {branch}'

    for stash in stashes.split('\n'):
        if stash.startswith(stash_startswith):
            target_stash = stash.split(':')[0]
            break

    if target_stash is None:
        return

    stash_output = run_git_command('git stash apply {}'.format(target_stash))
    drop_output = run_git_command('git stash drop {}'.format(target_stash))

    print(stash_output)
    print(drop_output)


def checkout_branch(branch):
    git_command = f'git checkout {branch}'
    output = run_git_command(git_command)

    print(output)


def stash_checkout(branch):
    if branch == '' or branch == None:
        print('No branch specified')
        return

    auto_stash()
    checkout_branch(branch)
    apply_branch_stash(branch)


def main():
    parser = argparse.ArgumentParser(description='Run git commands')
    parser.add_argument('command', type=str)
    parser.add_argument('-b', '--branch', type=str,
                        help='The branch to checkout')

    args = parser.parse_args()

    if args.command == '' or args.command == None:
        print('No command specified')
        return

    if args.command == 'checkout':
        stash_checkout(args.branch)
        return
    else:
        print('Invalid command')
        return


if __name__ == '__main__':
    main()
