#!/usr/bin/env python3

import argparse
import os

PARSER = argparse.ArgumentParser(description = "Bootstrap personal config")
PARSER.add_argument(
        "-f",
        "--force",
        action = "store_true",
        help = "overwrite existing config files?",
        dest = "force",
        default = False)

def symlink(src, dest):
    container = os.path.dirname(dest)
    if not os.path.isdir(container):
        os.makedirs(container)
    elif os.path.lexists(dest):
        if os.path.realpath(dest) == src:
            print("{} already set up correctly, skipping...".format(dest))
            return
        elif FLAGS.force:
            os.remove(dest)
        else:
            raise Exception("{} already exists, use -f to overwrite".format(dest))
    print("symlinking {} to {}".format(src, dest))
    os.symlink(src, dest)


def git(config, home):
    symlink(
            "{}/git/gitconfig".format(config),
            "{}/.gitconfig".format(home))
    symlink(
            "{}/git/gitignore_global".format(config),
            "{}/.gitignore_global".format(home))

def tmux(config, home):
    symlink(
            "{}/tmux/tmux.conf".format(config),
            "{}/.tmux.conf".format(home))

def ssh(config, home):
    symlink(
            "{}/ssh/config".format(config),
            "{}/.ssh/config".format(home))

def gpg(config, home):
    symlink(
            "{}/gpg/gpg.conf".format(config),
            "{}/.gnupg/gpg.conf".format(home))
    symlink(
            "{}/gpg/gpg-agent.conf".format(config),
            "{}/.gnupg/gpg-agent.conf".format(home))

def zsh(config, home):
    symlink(
            "{}/zsh/zshrc".format(config),
            "{}/.zshrc".format(home))
    symlink(
            "{}/zsh/zshrc.d".format(config),
            "{}/.zshrc.d".format(home))

def main():
    global FLAGS
    print("Starting boostrap...")
    FLAGS = PARSER.parse_args()

    config = os.path.dirname(os.path.abspath(__file__))
    home = os.environ["HOME"]

    git(config, home)
    tmux(config, home)
    ssh(config, home)
    gpg(config, home)
    zsh(config, home)

    print("done!")

if __name__ == "__main__":
    main()
