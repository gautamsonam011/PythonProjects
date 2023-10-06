# How to make a simplest instagram bot python. 
# pip install instabot

from instabot import Bot

bot = Bot()
bot.login(username = "sonamga527",password="sonam7485")
bot.follow('dsjhjd@_45')
bot.upload_photo("sg.png")
bot.unfollow("dsjhjd@_45")
bot.send_message("I love python",["dsjhjd@_45","sonam_564"])

followers = bot.get_user_followers("sonamga527")
for follower in followers:
    print(bot.get_user_info(follower))
    
following = bot.get_user_following("sonamga527")

for Following in following:
    print(bot.get_user_info(Following))
    

    



