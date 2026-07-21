# SMS-GPT

SMS-GPT is a Python-based SMS command system that allows you to interact with different services through SMS messages.

Currently supported commands include AI requests through OpenRouter. The project is designed to be extended with more SMS-based commands such as weather, automation, and other utilities.

## Features

- Receive and process SMS commands
- PIN-protected command execution
- AI responses through OpenRouter
- Extendable command system
- Simple polling-based SMS handling

## Project Structure

```
SMS-GPT/
├── main.py
├── commands.py
├── LibreSMS.py
├── openrouter_h.py
├── requirements.txt
├── .env
└── README.md
```

## Requirements

- Python 3.10+
- A configured LibreSMS account
- An OpenRouter API key

## Setup

### 1. Setup LibreSMS

SMS-GPT requires LibreSMS to send and receive messages.

Follow the LibreSMS documentation first:

https://github.com/fictus/LibreSMS

Configure your LibreSMS instance and obtain:

- Base URL
- API token

These values are required in the `.env` file.

### 2. Clone the repository

```bash
git clone https://github.com/PaperMug001/SMS-GPT
cd SMS-GPT
```

### 3. Install dependencies

Install the required Python packages:

```bash
pip install -r requirements.txt
```

Using a virtual environment is recommended but not required:

```bash
python -m venv venv
```

Activate it:

Windows:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
source venv/bin/activate
```

### 4. Configure environment variables

Create a file named `.env` in the project directory:

```env
BASE=your_libresms_base_url
TOKEN=your_libresms_token
OPENROUTER_KEY=your_openrouter_api_key
PIN=your_command_pin
```

Do not share this file publicly.

## Usage

Start the SMS command listener:

```bash
python main.py
```

The service will continuously check for incoming SMS messages and execute valid commands.

## Commands

Commands use the following format:

```
command PIN arguments
```

Example:

```
ai your_pin Explain quantum computing
```

## Available Commands

### AI

Send a message to the AI system.

Format:

```
ai <PIN> <message>
```

Example:

```
ai your_pin Write a Python hello world program
```

### Weather

Weather support is planned but not currently implemented.

Format:

```
wh <PIN>
```

## Security

SMS-GPT uses a PIN system to prevent unauthorized command execution.

The PIN should be stored in `.env`:

```env
PIN=your_command_pin
```

Keep your `.env` file private and never commit it to a public repository.

## Extending Commands

New commands can be added in `commands.py` and registered in `main.py`.

Example:

```python
elif command == "example":
    handle_example(sender, args, sms)
```

## License

This project is licensed under the MIT License.

See the `LICENSE` file for more information.
