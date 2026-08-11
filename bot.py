import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Bot token from environment variable
TOKEN = os.environ.get('BOT_TOKEN')

if not TOKEN:
    logger.error("BOT_TOKEN environment variable not set!")
    raise ValueError("BOT_TOKEN is required")

# Use the WhatsApp image as the promotional image
# You need to upload this image to a hosting service and get the URL
# For now, I'll show you how to use it as a local file
IMAGE_PATH = "WhatsApp Image 2026-08-11 at 19.19.31.jpeg"  # Local file
# OR use a hosted URL:
# IMAGE_URL = "https://your-image-hosting-url.com/paisa-base-promo.jpg"

# Configuration
REGISTER_URL = "https://wallet.paisa-base.com/register?inviteCode=phar6p"
CHANNEL_URL = "https://t.me/+oTUFYl-kubM1OTU1"
SUPPORT_CONTACT = "@jetlee261"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message with the promotional image and welcome message."""
    user = update.effective_user
    
    # Create inline keyboard
    keyboard = [
        [InlineKeyboardButton("📝 Register Now", callback_data='register')],
        [InlineKeyboardButton("📢 Join Official Channel", callback_data='channel')],
        [InlineKeyboardButton("💬 Customer Support", callback_data='support')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Welcome message
    welcome_message = (
        f"🚀 Welcome to Paisa Base, {user.first_name}!\n\n"
        f"Explore the available options below 👇\n\n"
        f"📝 Register and get started\n"
        f"📢 Join our official channel for updates\n"
        f"💬 Contact customer support for assistance\n\n"
        f"Please select an option below: ⬇️"
    )
    
    try:
        # Send the promotional image using local file
        with open(IMAGE_PATH, 'rb') as photo:
            await update.message.reply_photo(
                photo=photo,
                caption="💎 Paisa Base - Maximize Your Earnings!\n\n"
                        "📈 4.5% ON INR\n"
                        "💰 USDT 108\n"
                        "⚡ FAST SALES\n"
                        "🕐 24/7 Customer Care\n"
                        "🔓 Set Your Own Limit",
                reply_markup=reply_markup
            )
    except FileNotFoundError:
        logger.error(f"Image file not found: {IMAGE_PATH}")
        # Fallback: try to use URL if available
        try:
            IMAGE_URL = "https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/WhatsApp%20Image%202026-08-11%20at%2019.19.31.jpeg"
            await update.message.reply_photo(
                photo=IMAGE_URL,
                caption="💎 Paisa Base - Maximize Your Earnings!\n\n"
                        "📈 4.5% ON INR\n"
                        "💰 USDT 108\n"
                        "⚡ FAST SALES\n"
                        "🕐 24/7 Customer Care\n"
                        "🔓 Set Your Own Limit",
                reply_markup=reply_markup
            )
        except Exception as e:
            logger.error(f"Error sending image from URL: {e}")
            await update.message.reply_text(welcome_message, reply_markup=reply_markup)
            return
    except Exception as e:
        logger.error(f"Error sending image: {e}")
        await update.message.reply_text(welcome_message, reply_markup=reply_markup)
        return
    
    # Send welcome message with buttons
    await update.message.reply_text(welcome_message, reply_markup=reply_markup)

async def button_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Handle button presses."""
    query = update.callback_query
    await query.answer()
    
    choice = query.data
    
    if choice == 'register':
        keyboard = [
            [InlineKeyboardButton("🔗 Open Registration", url=REGISTER_URL)],
            [InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text=f"📝 **Register at Paisa Base**\n\n"
                 f"Click the button below to start your registration:\n\n"
                 f"🔗 {REGISTER_URL}\n\n"
                 f"Use invite code: **phar6p**",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    elif choice == 'channel':
        keyboard = [
            [InlineKeyboardButton("📢 Join Channel", url=CHANNEL_URL)],
            [InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text=f"📢 **Paisa Base Official Channel**\n\n"
                 f"Stay updated with the latest news, announcements, and exclusive offers!\n\n"
                 f"Click the button below to join:",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    elif choice == 'support':
        keyboard = [
            [InlineKeyboardButton("💬 Contact Support", url="https://t.me/jetlee261")],
            [InlineKeyboardButton("🔙 Back to Menu", callback_data='menu')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text=f"💬 **Customer Support**\n\n"
                 f"Contact our support team for any assistance:\n\n"
                 f"📱 {SUPPORT_CONTACT}\n\n"
                 f"We're available 24/7 to help you!",
            reply_markup=reply_markup,
            parse_mode='Markdown'
        )
    
    elif choice == 'menu':
        # Return to main menu
        keyboard = [
            [InlineKeyboardButton("📝 Register Now", callback_data='register')],
            [InlineKeyboardButton("📢 Join Official Channel", callback_data='channel')],
            [InlineKeyboardButton("💬 Customer Support", callback_data='support')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            text=f"🚀 Welcome to Paisa Base!\n\n"
                 f"Explore the available options below 👇\n\n"
                 f"📝 Register and get started\n"
                 f"📢 Join our official channel for updates\n"
                 f"💬 Contact customer support for assistance\n\n"
                 f"Please select an option below: ⬇️",
            reply_markup=reply_markup
        )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    help_text = (
        "🤖 **Paisa Base Bot Help**\n\n"
        "Available commands:\n"
        "/start - Start the bot and see options\n"
        "/help - Show this help message\n\n"
        "You can also use the buttons to navigate through the bot."
    )
    await update.message.reply_text(help_text, parse_mode='Markdown')

def main() -> None:
    """Start the bot."""
    # Create the Application
    application = Application.builder().token(TOKEN).build()
    
    # Register command handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    
    # Register callback query handler for buttons
    application.add_handler(CallbackQueryHandler(button_callback))
    
    # Start the Bot
    logger.info("Bot is starting with Paisa Base promotional image...")
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == '__main__':
    main()
