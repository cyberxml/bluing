# bluing ---- A powerful Bluetooth scanner

## WTAF

Something is up with bluescan/bluing. 

The pypi projects for bluing, bthci, and pyclui are all quarantined. The bluing main branch uses a Makefile that calls out to the author's home directories. Some of the early internal components (hci -> bthci and ui -> pyclui) were spun off into their own projects. Those projects are not on github and the files in pypi are obfuscated.

This code is cloned from bluing v0.1.0. It builds and installs. I don't know yet what functionality is missing. I will attempt to add features from the more recent builds of bluing.

Latest import: v0.4.1

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

## Usage

```
root@ubuntu2204:/tmp/bluing# bluing -h
bluing v0.4.1

A powerful Bluetooth scanner.

Author: Sourcell Xu from DBAPP Security HatLab.

License: GPL-3.0

Usage:
    bluing (-h | --help)
    bluing (-v | --version)
    bluing [-i <hci>] -m br [--inquiry-len=<n>]
    bluing [-i <hci>] -m br --lmp-feature BD_ADDR
    bluing [-i <hci>] -m le [--scan-type=<type>] [--timeout=<sec>] [--sort=<key>]
    bluing [-i <hci>] -m le --ll-feature [--timeout=<sec>] --addr-type=<type> BD_ADDR
    bluing -m le --adv [--channel=<num>]
    bluing [-i <hci>] -m sdp BD_ADDR
    bluing [-i <hci>] -m gatt [--include-descriptor] --addr-type=<type> BD_ADDR
    bluing [-i <hci>] -m vuln [--addr-type=<type>] BD_ADDR

Arguments:
    BD_ADDR    Target Bluetooth device address. FF:FF:FF:00:00:00 means local 
               device.

Options:
    -h, --help              Display this help.
    -v, --version           Show the version.
    -i <hci>                HCI device used for subsequent scans. [default: The first HCI device]
    -m <mode>               Scan mode, support BR, LE, SDP, GATT and vuln.
    --inquiry-len=<n>       Inquiry_Length parameter of HCI_Inquiry command. [default: 8]
    --lmp-feature           Scan LMP features of the remote BR/EDR device.
    --scan-type=<type>      Scan type used for scanning LE devices, active or 
                            passive. [default: active]
    --timeout=<sec>         Duration of the LE scanning, but may not be precise. [default: 10]
    --sort=<key>            Sort the discovered devices by key, only support 
                            RSSI now. [default: rssi]
    --adv                   Sniff advertising physical channel PDU. Need at 
                            least one micro:bit.
    --ll-feature            Scan LL features of the remote LE device.
    --channel=<num>         LE advertising physical channel, 37, 38 or 39). [default: 37,38,39]
    --include-descriptor    Fetch descriptor information.
    --addr-type=<type>      Type of the LE address, public or random.

```

## References

https://pypi.org/project/bluescan/

https://github.com/fO-000/bluing

https://pypi.org/project/bluing/

https://pypi.org/project/bthci/

https://pypi.org/project/pyclui/
