from instabot import Bot

# Initialize the bot
bot = Bot()

# Login to Instagram
bot.login(username="otabek_03.02", password="muhammadali", ask_for_code=True)

# Follow a user
bot.follow("ruhsoraemm")


# Upload a photo
bot.upload_photo("photo.jpg", caption="Hello, World!")

# Unfollow a user
bot.unfollow("ruhsoraemm")

# Get user followers
followers = bot.get_user_followers("ruhsoraemm")
print(followers)

# Send a message to a user
bot.send_message("Hello, World!", "makhmudjan_turakhulovm")

# Send a message to multiple users
bot.send_message("Hello, World!", ["makhmudjan_turakhulovm", "temurovkamron"])