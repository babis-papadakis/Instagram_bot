from instapy import InstaPy

session = InstaPy(username="username", password="password")
session.login()
session.like_by_tags(["fashion", "style"], amount=5)
session.set_dont_like(["naked", "nsfw"])
session.end()
