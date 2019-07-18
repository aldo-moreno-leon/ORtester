## About ORtester

ORtester is a tool designed to detect open redirects vulnerabilities on websites. It helps penetration testers and bug hunters find open redirect bugs through a scan supported by a list of payloads.

## Screenshot
![Alt text](https://github.com/Geek-Pwn/ORtester/blob/master/banner.PNG?raw=true)

## Installation
git clone https://github.com/Leonmugen/ORtester.git

## Dependencies
ORtester use requests python module.
```
sudo pip install -r requirements.txt
```

## Usage
| Short form | Long form | Description |
| --- | --- | --- |
| -u | --url | URL to fuzz |
| -f | --file | File with the list of payloads |
| -h | --help | Show the help message |

## Examples
* To scan an URL:
```
python ortester.py -u https://www.example.com/redirect.php?url= -f payloads.list
```
```
python ortester.py --url https://www.example.com/redirect.php?url= --file payloads.list
```

## Version
Current version is 0.1
