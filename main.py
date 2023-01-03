import logging
from aiogram import Bot, Dispatcher, executor, types
from config import *
from buttons import * 
from aiogram.types import Message,CallbackQuery
 


logging.basicConfig(level=logging.INFO)


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
  await message.reply(f" Assalomu aleykum tilni tanlang",reply_markup=kirish_nopka)


@dp.message_handler(text="🇺🇿 Uzbek")
async def echo(message: types.Message):
   await message.answer("Assalomu alaykum!👋Assalomu alaykum!\n\nSizni kuzatuvchilarimiz safida ko'rganimizdan mamnunmiz!Yosh menejerlar dasturi Besh tashabbus loyihasi hamda MBM IT kompaniyasi vakillari hamkorligida tashkil etilgan maxsus dastur hisoblanadi!\n\nUshbu loyiha orqali xalqaro doirada boshqaruv qobiliyatiga ega kadrlar tizimi shakllantiriladi.",reply_markup=menu)

@dp.message_handler(text="🇺🇸 English")
async def echo(message: types.Message):
   await message.answer("👋Hello my friend!\n\nWe are glad to see you among our observers! The Young Managers Program is a special project organized in collaboration with the Five Initiative Project and representatives of MBM IT Company!\n\n Through this program personnel management skills system will be formed in the international arena.",reply_markup=menu1)

#####################################################################################loyixa
@dp.callback_query_handler(text="loy")
async def echo(call:CallbackQuery):
   await call.message.answer("Loyiha maqsadi",reply_markup=loy_menu)
   await call.message.delete()
#################################################################################english loyixa
@dp.callback_query_handler(text="abo")
async def echo(call:CallbackQuery):
   await call.message.answer("About project",reply_markup=loy_menu11)
   await call.message.delete()
#################################################################################################
@dp.callback_query_handler(text="ai")
async def echo(call:CallbackQuery):
   await call.message.answer("🔰 What is the main purpose of the Young Managers Program?\n\nProject is designed to provide theoretical training in project management to young people from aged 17 to 25, to share practical work experience with young people, and to establish a community between people with different ideas and worldviews.",reply_markup=menu_nopka11)
   await call.message.delete()
@dp.callback_query_handler(text="pro")
async def echo(call:CallbackQuery):
   await call.message.answer("🔰 What are the objectives of project? \n\n• Training of specialists with international qualifications in the field of management and creation of a potential human resources system for entities and objects in the public and private sectors;\n\n• Providing high-paid jobs to increase the knowledge and skills of youth; \n\n• To form a process of communication between the older and younger generations, to put an end to the 'cliff' between them, to help them to ensure their interaction;",reply_markup=menu_nopka11)
   await call.message.delete()
@dp.callback_query_handler(text="the")
async def echo(call:CallbackQuery):
   await call.message.answer("🔰 How long will the project last and what is the procedure?\n\n📝 Procedure for the Young Managers Program:\nThe project will last for 10 weeks: practical and theoretical lessons will be conducted.\n\n📋 From August 25 to September 10, the process of registration and selection of candidates for participation in the project will be organized:\n• Round 1 qualifiers: September 13 will be announced. (100 participants);\n• Qualifying Round 2: September 15-16;\n• Answers: to be announced on September 18 (50 participants).\n\n💡 Out of the candidates, 50 young people who are strong, fluent in English, have their own ambitions and have big goals for the future will be selected.",reply_markup=menu_nopka11)
   await call.message.delete()
@dp.callback_query_handler(text="req")
async def echo(call:CallbackQuery):
   await call.message.answer("🔰 What are the requirements for candidates to participate?\n\n— Office work in English, Russian, Uzbek: fluent speaking and writing skills;\n— Knowledge of IT and media; \n— 17-25 years old;\n— Resident of Tashkent city and region.",reply_markup=menu_nopka11)
   await call.message.delete()

@dp.callback_query_handler(text="maq")
async def echo(call:CallbackQuery):
   await call.message.answer("🔰 Yosh Menejerlar dasturi nima maqsadda tashkil etilmoqda?\n\n\nMazkur loyiha 17 yoshdan 25 yoshgacha bo'lgan yoshlar qatlamini loyihalar boshqaruvi bo'yicha nazariy jihatdan o'qitish, amaliy jihatdan yoshlarga ish tajribasini ulashish, turli fikr va dunyoqarashga ega shaxslar orasida muloqot almashinuvini yo'lga qo'yish maqsadida tashkil etilgan.",reply_markup=menu_nopka)
   await call.message.delete()

@dp.callback_query_handler(text="vaz")
async def echo(call:CallbackQuery):
   await call.message.answer("🔰 Loyihaning vazifalari nimalardan iborat?\n\n• Boshqaruv sohasida malakaga ega, xalqaro doirada faoliyat yurita oladigan mutaxassislar tayyorlab, davlat va nodavlat sektoridagi subyekt/obyektlar uchun salohiyatli kadrlar tizimini yaratib berish;\n\n• Yoshlarning bilim va ko'nikmasini oshirib, yuqori daromad keltiradigan ish bilan ta'minlash;• Kattalar va yoshlar orasida kommunikatsiya jarayonini shakllantirib, o'rtadagi 'jarlik' ka ma'lum ma'noda chek qo'yish, ularning o'zaro hamkorligini ta'minlashga ko'maklashish.",reply_markup=menu_nopka)
   await call.message.delete()


@dp.callback_query_handler(text="tar")
async def echo(call:CallbackQuery):
   await call.message.answer("🔰 Loyiha qancha vaqt davom etadi va o'tkazilish tartibi qanday?\n\n\n📝Yosh menejerlar dasturining o’tkazilish tartibi:Loyiha 10 hafta davomida bo'lib o'tadi: amaliy va nazariy darslar olib boriladi.\n\n📋 Avgust oyining 25-sanasidan boshlab 10-Sentabr kuniga qadar loyihada ishtirok etishga nomzod shaxslarni ro'yxatdan o'tkazish va saralash jarayoni tashkil etiladi:\n\n• 1-bosqichi saralashdan o’tganlar: 13 Sentabr e’lon qilinadi. (100 ta ishtirokchi);\n\n• 2-saralash bosqichi: 15-16 Sentabr kuni bo’lib o’tadi;\n\n• Javoblar: 18 Sentabr kuni e’lon qilinadi (50 ta ishtirokchi).\n\n💡 Nomzodlar ichidan 50 nafar kuchga to'la, ingliz tilini yaxshi biluvchi, o'z ambitsiyalariga ega va kelajakda katta maqsadlari bor yoshlar tanlab olinadi.",reply_markup=menu_nopka)
   await call.message.delete()

@dp.callback_query_handler(text="talab")
async def echo(call:CallbackQuery):
   await call.message.answer("🔰 Loyihada qatnashish uchun nomzodlarga qanday talablar qo'yiladi?\n\n — ingliz, rus, o'zbek tilida ish yuritish: erkin so'zlashish va yoza olish;\n — IT texnologiyalari hamda mediasavodxonlik bo'yicha bilimga egalik;\n— 17-25 yosh orasida bo'lish;\n— Toshkent shahri va viloyati hududida istiqomat qilish",reply_markup=menu_nopka)
   await call.message.delete()
###############################################################################################loyixa back
@dp.callback_query_handler(text="back1")
async def echo(call:CallbackQuery):
   await call.message.answer("Loyiha maqsadi",reply_markup=menu)
   await call.message.delete()
@dp.callback_query_handler(text="back2")
async def echo(call:CallbackQuery):
   await call.message.answer("Loyiha maqsadi",reply_markup=loy_menu)
   await call.message.delete()
@dp.callback_query_handler(text="back10")
async def echo(call:CallbackQuery):
   await call.message.answer("About project",reply_markup=menu1)
   await call.message.delete()
@dp.callback_query_handler(text="back11")
async def echo(call:CallbackQuery):
   await call.message.answer("About project",reply_markup=loy_menu11)
   await call.message.delete()
@dp.callback_query_handler(text="back12")
async def echo(call:CallbackQuery):
   await call.message.answer("About project",reply_markup=menu1)
   await call.message.delete()


##################################################################################################royxatdan otish
@dp.callback_query_handler(text="roy")
async def til_tanlash(call:CallbackQuery):
    await call.answer("Ro'yxatdan o'tqazildingiz",show_alert=True )

@dp.callback_query_handler(text="reg")
async def til_tanlash(call:CallbackQuery):
    await call.answer("You are registered",show_alert=True )
   
###############################################################################################################
@dp.callback_query_handler(text="savol")
async def echo(call:CallbackQuery):
   await call.message.answer("Assalomu alaykum!\n\nSavollaringizni @Tawken01 ga yo'llashingiz mumkin. Sizga tez orada javob beramiz!\n\nE'tiboringiz uchun rahmat.",reply_markup=menu_nopka1)
   await call.message.delete()
@dp.callback_query_handler(text="send")
async def echo(call:CallbackQuery):
   await call.message.answer("Hello!\n\nYou can send your questions to @Tawken01. We will reply you soon.Thank you for your attention.",reply_markup=menu_nopka111)
   await call.message.delete()

@dp.callback_query_handler(text="back3")
async def echo(call:CallbackQuery):
   await call.message.answer("Loyiha maqsadi",reply_markup=menu)
   await call.message.delete()

if __name__ == '__main__':
   executor.start_polling(dp, skip_updates=True)
  