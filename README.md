# Paradrop

[![Join the chat at https://gitter.im/damouse/Paradrop](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/damouse/Paradrop?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Documentation Status](https://readthedocs.org/projects/paradrop/badge/?version=latest)](https://readthedocs.org/projects/paradrop/?badge=latest)


Virtualized wireless routers. 

Work in progress. For now, assume everything here is subject to change. 

## Installation
Instructions to follow. 

### Virtualenv
virtualenv is a tool that allows developers to manage environments, dependancies and more for python programs. In this case its used both as a management tool and a packageing tool (along with pex.)

We may choose to go with this as part of the build process since it doesn't require building the python package, but perhaps not. 

To load the current virtualenv, use 
    source [envdir]/bin/activate

To deactivate, use
    deactivate

To install something like twisted (which we are going to need...) be sure to have python developer tools already installed:
    sudo apt-get install python-dev

## Contributing
All contributions must follow [PEP8](https://www.python.org/dev/peps/pep-0008/) and have relevant tests. Please document as needed. 

## Miscellanious Help


Installation: 
  wget http://releases.ubuntu.com/15.04/ubuntu-15.04-snappy-amd64-generic.img.xz
  unxz ubuntu-15.04-snappy-amd64-generic.img.xz

Launching:
  kvm -m 512 -redir :8090::80 -redir :8022::22 ubuntu-15.04-snappy-amd64-generic.img

Connect to local instance:
  ssh -p 8022 ubuntu@localhost

Build a Snap and push it to local
  snappy build .
  snappy-remote --url=ssh://localhost:8022 install ./hello-world_1.0.17_all.snap

For the helloworld example, calling things. Name of snap, command in bin.
  hello-world.echo
