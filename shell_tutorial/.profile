# ~/.profile: executed by the command interpreter for login shells.
# This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login
# exists.
# see /usr/share/doc/bash/examples/startup-files for examples.
# the files are located in the bash-doc package.

# the default umask is set in /etc/profile; for setting the umask
# for ssh logins, install and configure the libpam-umask package.
#umask 022

# if running bash
if [ -n "$BASH_VERSION" ]; then
    # include .bashrc if it exists
    if [ -f "$HOME/.bashrc" ]; then
	. "$HOME/.bashrc"
    fi
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/bin" ] ; then
    PATH="$HOME/bin:$PATH"
fi

# set PATH so it includes user's private bin if it exists
if [ -d "$HOME/.local/bin" ] ; then
    PATH="$HOME/.local/bin:$PATH"
fi
# KIWA
if [ -d "$HOME/Projects/KIWA" ]; then
    export PYTHONPATH="$HOME/Projects/KIWA"
fi
export http_proxy="http://TFSSetup%40ger.muehlbauer.de:hallohal@proxy-roding.ger.muehlbauer.de:8080/"
export https_proxy="http://TFSSetup%40ger.muehlbauer.de:hallohal@proxy-roding.ger.muehlbauer.de:8080/"
export no_proxy="ado.muehlbauer.de,127.0.0.1,ro-soft3-srv.ger.muehlbauer.de"
