class song():
	def __init__(self):
		self.lyrics = ["Happy birthday to you",
				   "I don't want to get sued",
				   "So I'll stop right there"]
	
	def sing_me_a_song(self):
		for line in self.lyrics:
			print line
	
#happy_bday = song(["Happy birthday to you",
#				   "I don't want to get sued",
#				   "So I'll stop right there"])				   
				   
happy_bday = song()
happy_bday.sing_me_a_song()

