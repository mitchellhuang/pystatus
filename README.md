pystatus
========

Server monitoring tool that uses < 10MB of RAM.

## Requirements

- Python 2.4 or higher
- Bottle (server)
- psutil (client)
- simplejson (client)

## Installation

Install on both:

```
sudo apt-get install python python-dev python-pip
```

Client side only:

```
sudo pip install psutil simplejson
```

Server side only:

```
sudo pip install bottle
```

If you are getting any GCC/compile errors, check to make sure you have python-dev and build-essential installed.