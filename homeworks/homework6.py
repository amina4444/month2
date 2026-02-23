class Streamer:
    def live(self):
        return "Запускаю стрим! Подписывайтесь, ставьте лайки!"
    def earn(self):
        return "Заработал 500 донатов за 2 часа"

class TikToker:
    def live(self):
        return "Снимаю трендовый тикток под песню месяца!"

    def viral(self):
      return "Набрал 3 миллиона просмотров за сутки!"

class Mutant:
    def live(self):
        return "Я... я свечусь в темноте... это мой вайб..."
    def superpower(self):  return "Летаю и стреляю лазерами из глаз"

class GlowStreamer(Streamer,Mutant):
    def ultimate_content(self):
        return f"{self.live()} + {self.superpower()} "

class ViralCyborg(TikToker,Mutant):
    def ultimate_content(self):
        return f"{self.live()} + {self.superpower()} "

class DonateMage(Streamer,TikToker):
    def ultimate_content(self):
        return f"{self.live()} + {self.viral()} + {self.earn()} "

print(GlowStreamer.mro())
print(ViralCyborg.mro())
print(DonateMage.mro())

streamer = GlowStreamer()
print(streamer.live())
print(streamer.ultimate_content())
cyborg = ViralCyborg()
print(cyborg.live())
print(cyborg.ultimate_content())
donate = DonateMage()
print(donate.live())
print(donate.ultimate_content())