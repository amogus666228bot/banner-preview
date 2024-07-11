from PIL import Image, ImageDraw, ImageFont

class AvatarImage:
	def __init__(self, avatar_path, username, bio, bot_id, discord_id, premium_type, background_path: str = None, is_black = False):
		# print("Working")
		if background_path is not None:
			self.image = Image.open(background_path)
		else:
			self.image = Image.new("RGB", (400, 200), (255, 255, 255))
		self.avatar = Image.open(avatar_path).resize((100, 100))
		self.username = username
		self.bio = bio
		self.is_black = is_black
		self.bot_id = bot_id
		self.discord_id = discord_id
		if premium_type == "cool":
			self.premium = Image.open("assets/cool.png").resize((35, 35)).convert("RGBA")
		elif premium_type == "nice+":
			self.premium = Image.open("assets/nice.png").resize((35, 35)).convert("RGBA")
		elif premium_type == "nice++":
			self.premium = Image.open("assets/niceplus.png").resize((35, 35)).convert("RGBA")
		else:
			self.premium = None
			
	def draw(self):
		self.draw = ImageDraw.Draw(self.image)
		self.image.paste(self.avatar, (7, 8))
		font = ImageFont.truetype("arialbd.ttf", 15)
		if self.is_black:
			fill = (255, 255, 255)
		else:
			fill = (0, 0, 0)
		self.draw.text((123, 5.5), self.username, font=font, fill=fill)
		font = ImageFont.truetype("arial.ttf", 12)
		self.draw.text((123, 24), self.bio, font=font, fill=fill)
		font = ImageFont.truetype("arial.ttf", 12)
		if self.is_black:
			fill = (255, 255, 255)
		else:
			fill = (0, 0, 0)
		self.draw.text((7, 168), f"ID (В боте): {self.bot_id}\nDiscord ID: {self.discord_id}", font=font, fill=fill)
		if self.premium:
			self.image.paste(self.premium, (84, 84), self.premium)

	def open(self):
		# Return path
		self.image.show()


background = input("Путь к фоновой картинке: ")
isBlack = input("Фоновый цвет - черный? (y/n): ")
isBlack = True if isBlack == "y" else False
prem = input("Добавить значок? (cool/nice+/nice++/none): ")
prem = None if prem == "none" or None or "" else prem

builder = AvatarImage("./avatar.png", "username", "Hello, World!\nУровень: -1 | -1/0 (Всего: -1)", -1, -1, prem, background, isBlack)
builder.draw()
builder.open()
print("Тестовая картинка сделана! Она скоро будет открыта")