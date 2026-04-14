import uvicorn
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from telegram import Bot
from config import TOKEN, TARGET_GROUP
import io

app = FastAPI()
bot = Bot(token=TOKEN)


@app.post("/new-post")
async def receive_post(
        # 'Form' is used because files and JSON cannot be sent in the same body easily
        # Your other platform must send these as form-data fields
        name: str = Form(...),
        username: str = Form(...),
        email: str = Form(...),
        time: str = Form(...),
        image: UploadFile = File(...)  # This captures the actual image file
):
    # 1. Read the image file content into memory
    try:
        image_content = await image.read()

        # 2. Format the message caption
        caption = (
            f"📸 **New System Submission**\n"
            f"━━━━━━━━━━━━━━━━━━\n"
            f"👤 **Name:** {name}\n"
            f"🆔 **User:** @{username}\n"
            f"📧 **Email:** {email}\n"
            f"🕒 **Time:** {time}"
        )

        # 3. Send the image and details to the Group
        # We use io.BytesIO so we don't have to save the file to the disk
        await bot.send_photo(
            chat_id=TARGET_GROUP,
            photo=io.BytesIO(image_content),
            caption=caption,
            parse_mode='Markdown'
        )

        return {"status": "success", "detail": "Image and data forwarded to group"}

    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Failed to send to Telegram")


if __name__ == "__main__":
    # The bot runs as a web server on port 8000
    uvicorn.run(app, host="0.0.0.0", port=7999)