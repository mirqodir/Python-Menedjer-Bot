from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup,KeyboardButton,ReplyKeyboardMarkup

kirish_nopka=ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton("🇺🇿 Uzbek"),
		],
		[
			KeyboardButton("🇺🇸 English"),
		],

	],
	resize_keyboard=True

)

menu=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Loyiha haqida📉",callback_data="loy"),
			InlineKeyboardButton("Ro'yxatdan o'tish📝",callback_data="roy"),
		],
		[
			InlineKeyboardButton("Savollar💬",callback_data="savol"),
		],

	],
)
###############################################################################################################englihs
menu1=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("About the project📉",callback_data="abo"),
			InlineKeyboardButton("Registration📝",callback_data="reg"),
		],
		[
			InlineKeyboardButton("Send quenstions💬",callback_data="send"),
		],

	],
)

loy_menu11=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Aim of the project",callback_data="ai"),
			InlineKeyboardButton("Project task ",callback_data="pro"),

		],
		[
			InlineKeyboardButton("The order of process",callback_data="the"),
			InlineKeyboardButton("Requirements",callback_data="req"),
		],
		[
			InlineKeyboardButton("Back",callback_data="back10"),
		],

	],
)


#########################################################################################################################################
loy_menu=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Loyiha maqsadi",callback_data="maq"),
			InlineKeyboardButton("Loyiha vazifasi",callback_data="vaz"),

		],
		[
			InlineKeyboardButton("O'tkazilish tartibi",callback_data="tar"),
			InlineKeyboardButton("Talablar",callback_data="talab"),
		],
		[
			InlineKeyboardButton("orqaga",callback_data="back1"),
		],

	],
)

############################################################################################english loyixa menu
menu_nopka11=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Back",callback_data="back11"),

		],
	],
)
menu_nopka111=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("Back",callback_data="back12"),

		],
	],
)








menu_nopka=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("orqaga",callback_data="back2"),

		],
	],
)

menu_nopka1=InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton("orqaga",callback_data="back3"),

		],
	],
)