# SAP Document Information Extraction Automation

This repository automates the extraction of information from PDF documents using SAP's Document Information Extraction (DOX) service. The script uploads PDF files from a folder, sends them to the SAP DOX service, and retrieves structured data

## Features

- Automates PDF document upload to SAP DOX service
- Retrieves structured data from uploaded documents
- Processes all PDF files in a designated folder
- Configurable via a `config.json` file and environment variables

## Prerequisites

- Python 3.x
- An SAP DOX Document Information Extraction service account with valid API credentials

## Installation

1. **Clone the repository:**

    ```
    git clone https://github.com/ngpinjie/sap-dox-extractor.git
    cd sap-dox-extractor
    ```

2. **Install dependencies:**

    Install the necessary Python packages using `pip`:

    ```
    pip install -r requirements.txt
    ```

3. **Configuration:**

    - Create a `config.json` file in the root directory with the following format:

      ```
      {
        "sap_dox_url": "<service-url>",
        "client_id": "<client-id>",
        "client_secret": "<client-secret>",
        "token_url": "<token-url>"
      }
      ```

    - You can also create a `.env` file to store environment variables for the `client_id` and `client_secret`:

      ```
      CLIENT_ID=your_client_id
      CLIENT_SECRET=your_client_secret
      ```

4. **Place PDF documents:**

    Add the PDF files you want to extract into the `documents/` directory.

## Usage

Run the script to automatically upload the documents and retrieve extracted information:

```
python sap_dox_extractor.py
```
