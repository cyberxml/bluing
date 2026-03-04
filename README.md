# bluing ---- A powerful Bluetooth scanner

## WTAF

Something is up with bluescan/bluing. 

The pypi projects for bluing, bthci, and pyclui are all quarantined. The bluing main branch uses a Makefile that calls out to the author's home directories. Some of the early internal components (hci -> bthci and ui -> pyclui) were spun off into their own projects. Those projects are not on github and the files in pypi are obfuscated.

This code is cloned from bluing v0.1.0. It builds and installs. I don't know yet what functionality is missing. I will attempt to add features from the more recent builds of bluing.

Latest import: v0.2.0

This code built on Ubuntu 22.04 and Python 3.10.0

## Installation

Requires Python 3.10.0. Maybe not `requires` but that is my current build env. PyBluez did not install from PyPi so build from the repo.

```
git clone https://github.com/cyberxml/bluing
cd bluing
python3.10 -m pip install -r requirements.txt
./install-pybluez.sh
python3.10 setup.py build
python3.10 setup.py install
```


## References

https://pypi.org/project/bluescan/

https://github.com/fO-000/bluing

https://pypi.org/project/bluing/

https://pypi.org/project/bthci/

https://pypi.org/project/pyclui/
