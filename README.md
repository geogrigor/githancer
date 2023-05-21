# Githancer

Githancer is a Python-based command line tool that wraps the standard "git" commands and adds additional features to enhance your Git workflow.

## Features

- Auto stashes uncommitted changes and checks out to a new branch
- Reapplies the stash when switching back to the original branch
- Simplifies and automates common Git operations

## Installation

Before installing Githancer, make sure you have Python 3.x and Git installed on your system.

1. Clone the Githancer repository
```
git clone https://github.com/geogrigor/githancer.git
```
2. Change into the Githancer directory
```
cd githancer
```
3. Install githancer using pip
```
pip3 install .
```
4. Add your python bin directory to your PATH (only if it is not already added)
    - Run `python3 -m site --user-base`
    - Add the above output to your $PATH


## Usage

Githancer provides a checkout command to simplify the process of stashing uncommitted changes and checking out to a new branch.

To auto stash changes and check out a new branch, use the following command:
```
githancer checkout -b <branch-name>
```

Once you swith back to the original branch, githancer will automatically reapply the stash created earlier, restoring your uncommitted changes.

## Authors

- [@geogrigor](https://www.github.com/geogrigor)

## License

This project is licensed under the [MIT License](https://choosealicense.com/licenses/mit/). Feel free to use, modify, and distribute Githancer according to the terms of the license.