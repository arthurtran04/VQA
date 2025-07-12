# Visual Question Answering using BLIP model

## Introduction



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

- VQA Application using BLIP model from Salesforce
- Using Gradio UI

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

<img width="600rem" alt="Terminal" src="https://github.com/user-attachments/assets/f38485bb-8630-45bf-affc-e1a173f19e87"/>

The UI:

<img width="600rem" alt="Webpage" src="https://github.com/user-attachments/assets/6d013928-b0b4-4c13-b03c-6d617e692646"/>

Upload your photo in the left box and click **Submit** button, the application will generate the image caption in the right box:

<img width="600rem" alt="Example" src="https://github.com/user-attachments/assets/e39f8825-fc4d-42aa-9429-3941c2eb6014"/>

To stop the application, use `Ctrl + C` in the Terminal

## Demo

My demo on Hugging Face Spaces: [link](https://huggingface.co/spaces/josephtran04/image-captioning)

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
