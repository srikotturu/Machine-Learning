## Implementation (Command Line Based & Web Based)

### Ubuntu Terminal Setup
To run this project on an Ubuntu system, follow these steps:

#### 1. Install Python 3.10's virtual environment package, if not installed already
```bash
$ sudo apt install python3.10-venv
```
#### 2. Create a Python virtual environment named 'venv'
```bash
$ python3 -m venv venv
```
#### 3. Activate the virtual environment
```bash
$ . venv/bin/activate
```
#### 4. Install the required Python packages listed in 'requirements.txt'
```bash
$ pip install -r requirements.txt
```
#### 5. Crawl data from webpages, run:
```bash
$ python3 crawl.py
```
#### 6. Embed the crawled data, run:
```bash
$ python3 embed.py
```
#### 7. Run the system, run:
```bash
$ python3 app.py
```
or

```bash
$ flask run
```
#### To deactivate the virtual environment, run:
```bash
$ deactivate
```
