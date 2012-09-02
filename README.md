pystatus
========

Server monitoring tool.

## Requirements

- Linux
- Python 2.4 or higher
- Flask (server)
- psutil (client)

## Installation

Install on both:

```
sudo apt-get install python python-dev python-pip
```

Client side only:

```
sudo pip install psutil
```

Server side only:

```
sudo pip install flask
```

If you are getting any GCC/compile errors, check to make sure you have python-dev and build-essential installed.