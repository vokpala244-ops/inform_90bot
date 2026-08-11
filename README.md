# Paisa Base Telegram Bot

A Telegram bot for Paisa Base that provides registration, channel updates, and customer support.

## Features

- Display promotional image on start
- Registration button with invite code
- Official channel join button
- Customer support contact button
- Interactive inline keyboard navigation

## Deployment on Railway

1. Fork this repository to your GitHub account
2. Create a new project on Railway
3. Connect your GitHub repository
4. Add environment variable:
   - `BOT_TOKEN`: Your Telegram bot token

## Environment Variables

- `BOT_TOKEN`: Telegram bot token from @BotFather

## Local Development

1. Clone the repository
2. Create a virtual environment
3. Install dependencies: `pip install -r requirements.txt`
4. Set environment variable: `export BOT_TOKEN=your_token`
5. Run the bot: `python bot.py`

## Bot Commands

- `/start` - Start the bot and see options
- `/help` - Show help message
