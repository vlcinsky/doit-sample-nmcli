import os


DOIT_CONFIG = {
    "default_tasks": ["_list"],
    "verbosity": 2,
}


class Configuration(object):
    """Provide data and methods needed before tasks are actually set up."""
    def __init__(self, connection_file):
        self.connection_file = connection_file
        self.connections = []
        self.reread_connection_file()  # sets self.connections

    def reread_connection_file(self):
        """Read text file with each line having one connection name."""
        fname = self.connection_file
        if not os.path.exists(fname):
            return []
        with open(fname, "r") as f:
            names = [line.strip() for line in f if line]
        self.connections = names

    def warn_if_empty_connectinos(self):
        if not self.connections:
            msg = "WARNING: File {self.connection_file} not found."
            print(msg.format(self=self))
            print("To create one, call subcommand: init")
            print("Feel free to shorten the connection list.")

CFG = Configuration(".connections")
CFG.warn_if_empty_connectinos()


def task__list():
    return {
        "actions": [
            "echo === Short list of subcommands:",
            "doit list",
            "echo === For complete list use subcommand: list --all",
        ],
    }


def task_init():
    """(re)create file .connections listing connection names to use"""
    return {
        "actions": ["nmcli c|cut -f1 -d ' '|tail -n +2 - >%(targets)s"],
        "targets": [CFG.connection_file],
        "clean": True,
    }

def task_status():
    """List currently active network connections."""
    return {
        "actions": ["nmcli c |grep -v -- --"],
    }

def task_available():
    """List all available configured connections."""
    return {
        "actions": ["nmcli c"],
    }

def task_up():
    """Set given connection up."""

    for connection in CFG.connections:
        yield {
            "name": connection,
            "actions": ["nmcli c up %s" % connection],
        }
    msg = "This tasks must be called with specific connection name."
    yield {
        "name": None,
        "doc": "Set given connection up (specific connection name required).",
        "actions": ["echo %s" % msg]
    }


def task_down():
    """Set given connection down."""
    for connection in CFG.connections:
        yield {
            "name": connection,
            "actions": ["nmcli c down %s" % connection],
        }

def task_radio():
    """Report status of network radio devices"""
    return {
        "actions": ["nmcli radio"]
    }

def task_radioon():
    """Set network radio device on"""
    radios = ["wifi", "wwan"]
    for radio in radios:
        yield {
            "name": radio,
            "actions": ["nmcli radio %s on" % radio]
        }

def task_radiooff():
    """Set network radio device off."""
    radios = ["wifi", "wwan"]
    for radio in radios:
        yield {
            "name": radio,
            "actions": ["nmcli radio %s off" % radio]
        }
