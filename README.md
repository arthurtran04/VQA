# Visual Question Answering

## Introduction

VQA is a Python-based project that implements Visual Question Answering using the BLIP model. This repository enables users to input an image and a related question, leveraging advanced machine learning techniques to generate accurate answers by understanding both the visual content and the textual query.

## Table of Contents

- [Introduction](#introduction)
- [Prerequirements](#prerequirements)
- [Project Structure](#project-structure)
- [Model](#model)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Demo](#demo)
- [License](#license)

## Prerequirements

- ![Python 3.9](https://img.shields.io/badge/Python-3.9-blue) or above: [Download here](https://python.org/downloads)

## Project Structure

```
VQA/
├── .gitignore
├── app.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Model

- [Salesforce/blip-vqa-base](https://huggingface.co/Salesforce/blip-vqa-base)

## Features

Answer questions related to a image uploaded by user.

## Installation

To install this project, open your Terminal and follow these steps:

1. Clone the repository:

    ```sh
    $ git clone https://github.com/arthurtran04/VQA.git
    ```

2. Change the directory to `VQA`:

    ```sh
    $ cd "$(find . -type d -name "VQA")"
    ```

3. Create a Python virtual environment `.venv` and install the required dependencies:

    ```sh
    $ python3 -m venv .venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

## Usage

To start the application, run the `app.py` file:

   ```sh
   $ python app.py
   ```
This application will run locally at `http://127.0.0.1:7860`:

<img width="600rem" alt="Webpage" src="https://github.com/user-attachments/assets/d558c872-d3fb-4b9d-86cc-b32821928a63" />
"/>

Upload your image and enter a question then click **Submit** button, the application will generate the answer in the right box:

<img width="600rem" alt="Example" src="https://github.com/user-attachments/assets/48ce222a-352f-4ed3-96c8-1aa8f99b752d"/>

To stop the application, use `Ctrl + C` in the Terminal

## Demo

My demo on Hugging Face Spaces: [link](https://huggingface.co/spaces/josephtran04/VQA)

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
