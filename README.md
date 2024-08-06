# Cloudflare E-mail Routing Tool

## Overview

The Cloudflare E-mail Routing Tool is a simple utility to manage and route e-mails using [Cloudflare E-mail Routing Service](https://www.cloudflare.com/pt-br/developer-platform/email-routing/). This tool is designed to streamline the process of creating e-mail addresses within your Cloudflare-managed domains.

## Dependencies

- Python 3.10+
- Poetry
- [Cloudflare account](https://www.cloudflare.com/)

## How to Run

1. Ensure you have Python 3.10+ installed.
2. Install Poetry if you haven't already:
   ```bash
   pip install poetry
   ```
3. Clone the repository and navigate to the project directory.
4. Install the project dependencies using Poetry:
   ```bash
   poetry install
   ```
5. Run the main script with the desired service:
   ```bash
   poetry run python emailrouting/main.py "Desired service"
   ```

## Configuration

1. Copy the `.env.example` file to create your own `.env` file:
   ```bash
   cp .env.example .env
   ```

2. Open the `.env` file and fill in the required values based on your Cloudflare account and desired configuration. Here is an example:
   ```env
   CLOUDFLARE_API_TOKEN=your_cloudflare_api_token
   CLOUDFLARE_ZONE_ID=your_cloudflare_zone_id
   ```

## Output

The script will create an e-mail address and output a confirmation message. For example:

```
E-mail created: meu-teste@mycloudflaredomain.com
```

## Shell

Useful shell to add to your bash PATH

```
#!/bin/bash
ARG=$1
CURRENT_DIR=$(pwd)
cd /path/to/cloned/project || exit
poetry run python emailrouting/main.py "$ARG"
cd "$CURRENT_DIR" || exit
```

Add it to some place like `/usr/local/bin` with a name like `createemail`. Add execution permission:

```bash
$ sudo chmod +x /usr/local/bin/createemail
```

and then just call from anywhere:

```
$ createemail "The strage service asking my email"
```

## Linting
This project uses `ruff` for linting. To run the linter, use the following command:
```bash
poetry run ruff .
```
