from telegram import Bot
from config import TOKEN, TARGET_GROUP
import asyncio


async def send_api_post_to_group(api_data):
    """
    api_data expected format:
    {
        "image_url": "http://example.com/image.jpg",
        "username": "johndoe",
        "name": "John Doe",
        "email": "john@example.com",
        "timestamp": "2024-05-20 10:00"
    }
    """
    bot = Bot(token=TOKEN)

    caption = (
        f"🚀 **New API Post**\n"
        f"---"
        f"👤 **Name:** {api_data['name']}\n"
        f"📧 **Email:** {api_data['email']}\n"
        f"🆔 **User:** @{api_data['username']}\n"
        f"🕒 **Time:** {api_data['timestamp']}"
    )

    await bot.send_photo(
        chat_id=TARGET_GROUP,
        photo=api_data['image_url'],
        caption=caption,
        parse_mode='Markdown'
    )   