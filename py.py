from pyrogram import Client, filters
from pyrogram.types import InlineQueryResultArticle, InputTextMessageContent

app = Client("my_bot", bot_token="7262692879:AAGLMtLcrL2fN5oBhhUz_LAGsSTvYjdCglg")

@app.on_inline_query()
async def inline_query(client, query):
    if query.query.startswith("@mybotinlinequery"):
        username_or_id = query.query.split()[1].strip()
        
        try:
            user = await client.get_users(username_or_id)
        except Exception as e:
            print(f"Error: {e}")
            return
        
        results = [
            InlineQueryResultArticle(
                title=user.first_name,
                description=user.username,
                thumb_url=user.photo.small_file_id if user.photo else None,
                input_message_content=InputTextMessageContent(
                    message_text=f"ID: {user.id}\nUsername: @{user.username}\nName: {user.first_name}"
                )
            )
        ]
        
        await query.answer(results)

app.run()
