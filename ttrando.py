#!python3

import json
import os.path
import sys
import argparse

default_conf = os.path.join(
    os.path.expanduser("~"),
    '.ttrando.conf'
)

def write_config(filename=default_conf, data=None):
    if data == None:
        print("Config file not found - writing new config file to ~/.ttrando.conf")
        data={}
    with open(filename, "w") as json_file:
        json.dump(data, json_file, indent=4, sort_keys=True)

def load_conf(filename=default_conf):
    if os.path.exists(filename):
        if os.path.isfile(filename):
            with open(filename) as json_file:
                data = json.load(json_file)
                return data
        else:
            print("config file {} is a directory and cannot be read.".format(filename))
            sys.exit(1)
    else:
        write_config(filename)
        return load_conf(filename)

def cli_action(func):
    func.cli_action = True
    return func

class TTRandoCLI:
    """
    Class representing the CLI interface for ttrando

    class methods with the `@cli_action` decorator
    are executed from the CLI via `ttrando [action]`
    """
    def __init__(self):
        self.parser = argparse.ArgumentParser(
            prog='ttrando',
            description='CLI Utility for Tabletop RPG Randomizer'
        )
        self.actions = [entry for entry in dir(self) if hasattr(getattr(self,entry),'cli_action')]
        self.parser.add_argument('action', help='action to take -- choice of ({})'.format("|".join(self.actions)))

        self.config = load_conf()

    def _run(self):
        args = self.parser.parse_args(sys.argv[1:2])

        if hasattr(self, args.action):
            action_call = getattr(self, args.action)
            if hasattr(action_call, 'cli_action'):
                return action_call()
        print('Action "{}" not recognized'.format(args.action))
        self.parser.print_help()
        return 1

    @cli_action
    def run(self):
        parser = argparse.ArgumentParser(
            prog='ttrando run',
            description='run ttrando'
        )
        args = parser.parse_args(sys.argv[2:])
        print("Valid!")
        return 0

def main():
    return TTRandoCLI()._run()

if __name__ == "__main__":
    sys.exit(main())
