from os import environ 

class Config:
    API_ID = environ.get("API_ID", "20919625")
    API_HASH = environ.get("API_HASH", "40168846bf06f4ff443f0f7a4182bf8d)
    BOT_TOKEN = environ.get("BOT_TOKEN", "6569842591:AAFWT0-OAnqbaoHsczM7TQQ-NKFDho9nPoA") 
    BOT_SESSION = environ.get("BOT_SESSION", "1BVtsOJABu4viqJmSLRAkLo35--Ea0dUV-K1hLsg1U7bq5xzdakKdHBGnSaCLEGczKlht99v7thsmThHdB55YdBn8diEnkQCncE1t1NdBOB1GaHyAnc2dsYNQL3BTKdJq6UAjiwlfShum8zY9NP4UL-loNHEhvkoRhE37kg4Dxvl-vg1qWE2RjSkdG7duC3lulx1eBDhGFXG1cnRaj3t6cCqfoyb9CYKPDHPoWkoIJH95AuJ7tjqTnZZBbKEXsqp-QRGmduknLjd-5lV_FW0S1zGXop4QM2rhp6L6p0DmNUYl3FYtCo-WxiCz-CEDEYv9fFbMrpGjJjL41FXS6fuKod09Jv7g0Bc=") 
    DATABASE_URI = environ.get("DATABASE", "mongodb+srv://lomag83830:Q7OXsaQchn53k4rE@cluster0.o8uqf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0)
    DATABASE_NAME = environ.get("DATABASE_NAME", "forward-bot")
    BOT_OWNER_ID = [int(id) for id in environ.get("BOT_OWNER_ID", '6233910543').split()]

class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []
   
