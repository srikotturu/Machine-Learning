### **Install Node.js**

1. Download and import the Nodesource GPG key

```sh
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
```

2. Create deb repository

```sh
NODE_MAJOR=18
echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
```

> ***Optional***: ``NODE_MAJOR`` can be changed depending on the version you need.
>
> ```sh
> NODE_MAJOR=16
> NODE_MAJOR=18
> NODE_MAJOR=20
> ```

3. Run Update and Install

```sh
sudo apt-get update
sudo apt-get install nodejs -y
```



## Implementation

To set up and run this Node.js web application, follow these steps:

### 1. Install Node.js

If you haven't already, you need to install Node.js. You can download it from the official website: [Node.js Download](https://github.com/nodesource/distributions#nodejs).

* Download and import the Nodesource GPG key

```sh
sudo apt-get update
sudo apt-get install -y ca-certificates curl gnupg
sudo mkdir -p /etc/apt/keyrings
curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | sudo gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg
```

* Create deb repository

```sh
NODE_MAJOR=18
echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | sudo tee /etc/apt/sources.list.d/nodesource.list
```

> ***Optional***: ``NODE_MAJOR`` can be changed depending on the version you need.
>
> ```sh
> NODE_MAJOR=16
> NODE_MAJOR=18
> NODE_MAJOR=20
> ```

* Run Update and Install

```sh
sudo apt-get update
sudo apt-get install nodejs -y
```


### 2. Initialize Your Project

To set up your project and create/update the `package.json` file:

```bash
npm init -y
```

### 3. Update Package.json Scripts

Update your `package.json` file to include the following scripts:

```json
"scripts": {
    "install": "pip install -r requirements.txt",
    "crawl": "python3 crawl.py",
    "embed": "python3 embed.py"
}
```

These scripts are used to install Python dependencies, crawl a website, and create embeddings.

### 4. Install Python Dependencies

Install Python dependencies from `requirements.txt`:

```bash
npm run install
```

### 5. Crawl the Website

Crawl a website, execute the following command:

```bash
npm run crawl
```

### 6. Create Embeddings

Generate embeddings with the following command:

```bash
npm run embed
```

### 7. Start the Web Application

Finally, start the Node.js web application using:

```bash
node server.js
```

Your web application should now be up and running. To access it, open your web browser and go to http://localhost:3000. To stop it, simply press `Ctrl + C` in your terminal.

