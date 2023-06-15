from aiogram import types

class Keyboards:
    def main(self):
        inl = types.InlineKeyboardMarkup()
        birlik = types.InlineKeyboardButton("🧍‍♂️🧍‍♀️ Bir kishilik", callback_data="birlik")
        juftlik = types.InlineKeyboardButton("👩‍❤️‍👨 Juftlik", callback_data="juftlik")
        inl.add(birlik, juftlik)
        return inl

    def catgory(self, cat, s, ln):
        com = 'select'
        if cat == 'juftlik':
            com = 'slcj'
        inl = types.InlineKeyboardMarkup()
        ortga = types.InlineKeyboardButton("Ortga", callback_data=f"back|{cat}|{s}")
        son = types.InlineKeyboardButton(f"{s}/{ln}", callback_data="_")
        oldinga = types.InlineKeyboardButton("oldinga", callback_data=f"next|{cat}|{s}")
        tanlash = types.InlineKeyboardButton("Tanlash", callback_data=f"{com}|{cat}|{s}")
        inl.add(ortga, son,  oldinga).add(tanlash)
        return inl
    


kb = Keyboards()