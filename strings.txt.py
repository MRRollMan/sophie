File                                  Line  Text
----------------------------------------------------------------------------------------------------
src/handlers/commands.py              123  (tb.add("📡 Ping: {ping_time} ms\n", ping_time=Code(f"{ping_time:.2f}"))
src/functions.py                       50  await bot.send_message(config.CHANNEL, f"⛔️ Offline")
src/functions.py                       41  await bot.send_message(config.CHANNEL, f"✅ Online")
src/handlers/football.py               62  await callback.bot.answer_callback_query(callback.id, "Хто прочитав той лох")
src/handlers/game.py                   86  await callback.bot.answer_callback_query(callback.id, "Хто прочитав той лох")
src/handlers/games.py                  52  await callback.bot.answer_callback_query(callback.id, "Хто прочитав той лох")
src/utils/utils.py                     61  await callback.bot.answer_callback_query(callback.id, "Хто прочитав той лох")
src/utils/utils.py                     63  await callback.bot.answer_callback_query(callback.id, "Хто прочитав той лох")
src/handlers/basketball.py             68  await callback.bot.answer_callback_query(callback.id, "Хто прочитай той лох")
src/handlers/bowling.py                73  await callback.bot.answer_callback_query(callback.id, "Хто прочитай той лох")
src/handlers/casino.py                 86  await callback.bot.answer_callback_query(callback.id, "Хто прочитай той лох")
src/handlers/darts.py                  66  await callback.bot.answer_callback_query(callback.id, "Хто прочитай той лох")
src/handlers/dice.py                   86  await callback.bot.answer_callback_query(callback.id, "Хто прочитай той лох")
src/filters.py                        113  await callback.bot.answer_callback_query(callback.id, "🖕😂 Ці кнопочки не для тебе", show_alert=True)
src/middliwares/RegisterMiddleware.py  42  await event.reply(f"👋 {event.from_user.mention_markdown()}, вітаю. Додавай мене в чат та грай\nЩоб дізнатися як, вивчай /help\nПідтримка: @k0k0sbot")
src/handlers/commands.py               23  await message.reply(Text("👋 Вітаю. Додавай мене в чат та грай\nЩоб дізнатися як, вивчай /help\nПідтримка: @k0k0sbot").as_markdown())
src/handlers/commands.py               86  await query.bot.answer_callback_query(query.id, "Хто прочитав той лох")
src/handlers/commands.py               93  await query.bot.answer_callback_query(query.id, "Хто прочитав той лох")
src/handlers/give.py                   89  await query.bot.answer_callback_query(query.id, "Хто прочитав той лох")
src/handlers/give.py                  101  await query.bot.answer_callback_query(query.id, "Хто прочитав той лох")
src/handlers/settings.py               53  await query.bot.answer_callback_query(query.id, "✅")
src/handlers/help.py                   38  await query.message.edit_text("⚙️ Тут ти можеш почитати\nпро мене все", reply_markup=kb.as_markup())
src/handlers/shop.py                   88  await query.message.edit_text("💳 Хочеш більше русофобії?\n"
src/handlers/admin_commands.py        155  await reply_and_delete(message, "⚠️ Не бачу такого id")
src/handlers/shop.py                   30  await reply_and_delete(message, "💳 Хочеш більше русофобії?\n"
src/handlers/help.py                   32  await reply_and_delete(message, text="⚙️ Тут ти можеш почитати\nпро мене все", reply_markup=kb.as_markup())
src/config.py                          64  f"Помилка конфігу: {e}"
src/config.py                          69  f"Помилка конфігу: Неправильний формат значення - {e}"
src/config.py                          54  f'Помилка конфігу: Опцію "{e.option.upper()}" не знайдено'
src/config.py                          59  f'Помилка конфігу: Опцію "{e}" не знайдено'
src/config.py                          49  f'Помилка конфігу: Секцію "{e.section.upper()}" не знайдено'
src/logger.py                          34  logging.Formatter("%(asctime)s - %(message)s", datefmt="%d.%m.%Y, %H:%M:%S")
src/middliwares/LoggingMiddleware.py   24  logging.info(f"{chat=}: {user=} - {content_type}")
src/functions.py                       39  print("Online")
src/functions.py                       52  print(f"Помилка зупинки: {e}")
src/functions.py                       43  print(f"Помилка старту: {e}")
src/handlers/commands.py               39  tb.add("Made {onilyxe}. Idea {den}. Updated and fixed {htivka}", True)
src/handlers/admin_commands.py         40  tb.add("\n\n\n⚠️ Йобнуті ({removed_chats_count}):", removed_chats_count=removed_chats_count)
src/handlers/admin_commands.py         89  tb.add("\n⚠️ Помилки:\n{error_messages}", error_messages=error_messages, new_line=True)
src/utils/utils.py                     93  tb.add("{emoji} {user}, граємо?\n", emoji=emoji, user=TextMention(user.first_name, user=user))
src/handlers/commands.py               37  tb.add("{news_channel}", True)
src/handlers/commands.py               38  tb.add("{source}\n", True)
src/handlers/commands.py               50  tb.add("👛 Баланс {user} {russophobia} кг", russophobia=Code(russophobia))
src/handlers/commands.py               63  tb.add("{user}, значить так, собака спідозна. Якщо підеш з гри, то всі твої дані (зокрема точне місце проживання тебе і всіх твоїх рідних) буде передано поважним особам. Після підтвердження, протягом 120 хвилин до тебе приїдуть у гості")
src/handlers/shop.py                   41  tb.add("Головна умова, вказати ID чату де ви хочете поповнення русофобії "
src/handlers/shop.py                   39  tb.add("Посилання на банку: {bank}", bank=TextLink("send.monobank.ua", url=config.DONATE))
src/handlers/shop.py                   40  tb.add("Робите донат на потрібну вам суму, і відправляєте скрін сплати в @k0k0sbot", new_line=True)
src/handlers/commands.py               52  tb.add("У {user} 0 кг🫵😂")
src/handlers/commands.py               65  tb.add("У {user} 0 кг🫵😂")
src/handlers/basketball.py             60  tb.add("↩️ Ти повернув {bet} кг\n", True, bet=Code(callback_data.bet))
src/handlers/bowling.py                65  tb.add("↩️ Ти повернув {bet} кг\n", True, bet=Code(callback_data.bet))
src/handlers/casino.py                 78  tb.add("↩️ Ти повернув {bet} кг\n", True, bet=Code(callback_data.bet))
src/handlers/darts.py                  58  tb.add("↩️ Ти повернув {bet} кг\n", True, bet=Code(callback_data.bet))
src/handlers/admin_commands.py        138  tb.add("⚠️ {example}",
src/handlers/admin_commands.py        148  tb.add("⚠️ {example}",
src/handlers/admin_commands.py        185  tb.add("⚠️ {example}",
src/handlers/admin_commands.py        123  tb.add("⚠️ {user} не має русофобії", user=mention)
src/handlers/admin_commands.py        121  tb.add("⚠️ {user} тепер має {balance} кг русофобії", user=mention, balance=Code(user_balance))
src/handlers/admin_commands.py        126  tb.add("⚠️ {user} тепер має {balance} кг русофобії", user=mention, balance=Code(value))
src/handlers/give.py                   26  tb.add("⚠️ Ну і єблан. Ось як треба: {cmd}", cmd=Code("/give [N] [reply]"))
src/handlers/admin_commands.py         50  tb.add("⚠️ Розсилка меседжів\n\n"
src/handlers/football.py               53  tb.add("⚽ {user} переміг")
src/handlers/football.py               56  tb.add("⚽ {user} програв")
src/utils/game_messages.py             68  tb.add("⚽ Футбол. Влуч у ворота\n\n👛 Баланс: {balance} кг\n🪙 {user}, роби ставку\n",
src/handlers/give.py                   83  tb.add("✅ {giver} передав {value} кг {receiver}.\n👛 Баланс: {new_value} кг",
src/handlers/admin_commands.py        170  tb.add("✅ {user_id} тепер має {updated_value} кг русофобії",
src/handlers/admin_commands.py         87  tb.add("✅ Кількість чатів: {successful_sends}", successful_sends=Code(successful_sends))
src/handlers/darts.py                  52  tb.add("🎯 {user} переміг")
src/handlers/darts.py                  60  tb.add("🎯 {user} програв")
src/handlers/darts.py                  57  tb.add("🎯 {user}, ну майже")
src/utils/game_messages.py             54  tb.add("🎯Дартс. Влуч у центр\n\n👛 Баланс: {balance} кг\n🪙 {user}, роби ставку\n",
src/handlers/casino.py                 72  tb.add("🎰 {user} переміг")
src/handlers/casino.py                 80  tb.add("🎰 {user} програв")
src/handlers/casino.py                 54  tb.add("🎰 {user}, ЄЄЄЄЄЄЄЄЄЄБАТЬ 777 МАКС ВІН🤑")
src/handlers/casino.py                 66  tb.add("🎰 {user}, переміг")
src/handlers/casino.py                 77  tb.add("🎰 {user}, наступного разу пощастить")
src/handlers/casino.py                 60  tb.add("🎰 {user}, ніхуйово")
src/utils/game_messages.py             47  tb.add("🎰 Казіно. Постарайся вибити 777\n\n👛 Баланс: {balance} кг\n🪙 {user}, роби ставку\n",
src/handlers/dice.py                   77  tb.add("🎲 {dice_value}, {parity}. {user} переміг")
src/handlers/dice.py                   80  tb.add("🎲 {dice_value}, {parity}. {user} програв")
src/handlers/dice.py                   48  tb.add("🎲 {user} граємо?\n", user=TextMention(user.first_name, user=user))
src/utils/game_messages.py             61  tb.add("🎲 Кістки. Вгадай парне чи непарне\n\n👛 Баланс: {balance} кг\n🪙 {user}, роби ставку\n",
src/handlers/bowling.py                53  tb.add("🎳 {user} переміг")
src/handlers/bowling.py                67  tb.add("🎳 {user} програв")
src/handlers/bowling.py                59  tb.add("🎳 {user}, бля, ну майже")
src/handlers/bowling.py                64  tb.add("🎳 {user}, наступного разу пощастить")
src/utils/game_messages.py             40  tb.add("🎳 Боулінг. Вибий всі кеглі\n\n👛 Баланс: {balance} кг\n🪙 {user}, роби ставку\n",
src/handlers/basketball.py             54  tb.add("🏀 {user} переміг")
src/handlers/basketball.py             62  tb.add("🏀 {user} програв")
src/handlers/basketball.py             59  tb.add("🏀 {user}, бля, ну майже")
src/utils/game_messages.py             33  tb.add("🏀 Баскетбол. Влуч м'ячем в кільце\n\n👛 Баланс: {balance} кг\n🪙 {user}, роби ставку\n",
src/utils/utils.py                     94  tb.add("🪙 Ставка: {bet} кг", True, bet=Code(bet))
src/handlers/casino.py                 83  tb.add("👛 Баланс: {new_balance} кг", True, new_balance=Code(balance))
src/handlers/game.py                   81  tb.add("👛 Баланс: {new_balance} кг", True, new_balance=Code(balance))
src/handlers/bowling.py                70  tb.add("👛 Баланс: {new_balance} кг", True, new_balance=Code(balance))
src/handlers/dice.py                   83  tb.add("👛 Баланс: {new_balance} кг", True, new_balance=Code(balance))
src/handlers/football.py               59  tb.add("👛 Баланс: {new_balance} кг", True, new_balance=Code(balance))
src/handlers/basketball.py             65  tb.add("👛 Баланс: {new_balance} кг", True, new_balance=Code(balance))
src/handlers/darts.py                  63  tb.add("👛 Баланс: {new_balance} кг", True, new_balance=Code(balance))
src/handlers/games.py                  38  tb.add("👛 Баланс: {new_russophobia} кг\n⏰ Продовжуй через {ttp}", True)
src/handlers/admin_commands.py         37  tb.add("💬 Чати ({chats_count}):", chats_count=total_chats_count)
src/handlers/dice.py                   50  tb.add("💰 Можливий виграш: {potential_win} кг", True, potential_win=Code(potential_win))
src/handlers/game.py                   50  tb.add("💰 Можливий виграш: {potential_win} кг", True, potential_win=Code(potential_win))
src/utils/utils.py                     95  tb.add("💰 Можливий виграш: {potential_win} кг", True, potential_win=potential_win)
src/handlers/games.py                  35  tb.add("📈 {user}, +{russophobia} кг")
src/handlers/basketball.py             55  tb.add("📈 Ти виграв {bet_won} кг\n", True, bet_won=Code(bet_won))
src/handlers/bowling.py                54  tb.add("📈 Ти виграв {bet_won} кг\n", True, bet_won=Code(bet_won))
src/handlers/bowling.py                60  tb.add("📈 Ти виграв {bet_won} кг\n", True, bet_won=Code(bet_won))
src/handlers/casino.py                 55  tb.add("📈 Ти виграв {bet_won} кг\n", True, bet_won=Code(bet_won))
src/handlers/casino.py                 61  tb.add("📈 Ти виграв {bet_won} кг\n", True, bet_won=Code(bet_won))
src/handlers/casino.py                 67  tb.add("📈 Ти виграв {bet_won} кг\n", True, bet_won=Code(bet_won))
src/handlers/casino.py                 73  tb.add("📈 Ти виграв {bet_won} кг\n", True, bet_won=Code(bet_won))
src/handlers/darts.py                  53  tb.add("📈 Ти виграв {bet_won} кг\n", True, bet_won=Code(bet_won))
src/handlers/dice.py                   78  tb.add("📈 Ти виграв {bet_won} кг\n", True, bet_won=Code(bet_won))
src/handlers/football.py               54  tb.add("📈 Ти виграв {bet_won} кг\n", True, bet_won=Code(bet_won))
src/handlers/game.py                   76  tb.add("📈 Ти виграв {bet_won} кг\n\n", True, bet_won=Code(bet_won))
src/handlers/games.py                  37  tb.add("📉 {user}, -{russophobia} кг")
src/handlers/basketball.py             63  tb.add("📉 Проїбав {bet} кг\n", True, bet=Code(callback_data.bet))
src/handlers/bowling.py                68  tb.add("📉 Проїбав {bet} кг\n", True, bet=Code(callback_data.bet))
src/handlers/casino.py                 81  tb.add("📉 Проїбав {bet} кг\n", True, bet=Code(callback_data.bet))
src/handlers/darts.py                  61  tb.add("📉 Проїбав {bet} кг\n", True, bet=Code(callback_data.bet))
src/handlers/dice.py                   81  tb.add("📉 Проїбав {bet} кг\n", True, bet=Code(callback_data.bet))
src/handlers/football.py               57  tb.add("📉 Проїбав {bet} кг\n", True, bet=Code(callback_data.bet))
src/handlers/game.py                   79  tb.add("📉 Проїбав {bet} кг\n\n", True, bet=Code(callback_data.bet))
src/handlers/commands.py               36  tb.add("📡 Sophie {version}\n", True)
src/handlers/give.py                   58  tb.add("🔄 {giver} хоче передати {value} кг {receiver}. \n👛 Баланс: {current_value} кг",
src/handlers/game.py                   75  tb.add("🧌 {user} переміг")
src/handlers/game.py                   78  tb.add("🧌 {user} програв")
src/handlers/game.py                   48  tb.add("🧌 {user}, граємо?\n", user=TextMention(user.first_name, user=user))
src/utils/game_messages.py             75  tb.add("🧌 Вбий кацапа. Якщо вгадаєш де кацап, вб'єш його та отримаєш винагороду\n\n👛 Баланс: {balance} кг\n🪙 {user}, роби ставку\n",
src/handlers/dice.py                   49  tb.add("🪙 Ставка: {bet} кг", True, bet=Code(bet))
src/handlers/game.py                   49  tb.add("🪙 Ставка: {bet} кг", True, bet=Code(bet))
src/utils/utils.py                     94  tb.add("🪙 Ставка: {bet} кг", True, bet=Code(bet))
src/handlers/give.py                   79  tb.add("🫵😂 В тебе {russophobia} кг. Бомж ахахахха", russophobia=Code(chat_user[3][3] if chat_user else 0))
src/handlers/give.py                   42  tb.add("🫵😂 В тебе {russophobia} кг. Бомж ахахахха", russophobia=Code(giver[3] if giver else 0))
src/handlers/admin_commands.py         38  tb.add('\n'.join(chat_list_lines), new_line=True)
src/handlers/admin_commands.py         41  tb.add('\n'.join(removed_chats_info), new_line=True)
src/utils/utils.py                    184  tb.add('{count_%(count)s}. {user_name_%(count)s}: {rusophobia_%(count)s} кг' % {"count": count}, True,
src/handlers/admin_commands.py        195  tb.add(f"{e}")
src/utils/utils.py                    178  tb.add(f'{title}:\n🟰 Всього: {total_kg} кг\n')
src/handlers/settings.py               18  kb.row(InlineKeyboardButton(text=f"Міні ігри: {'✅' if minigames_enabled else '⛔️'}",
src/handlers/help.py                   13  kb.row(InlineKeyboardButton(text="Основне - /killru", callback_data=HelpCallback(game=Games.KILLRU).pack()),
src/handlers/settings.py               20  InlineKeyboardButton(text=f"Передача кг: {'✅' if give_enabled else '⛔️'}",
src/handlers/dice.py                   45  kb.row(InlineKeyboardButton(text="↩️ Назад", callback_data=back.pack()),
src/handlers/game.py                   45  kb.row(InlineKeyboardButton(text="↩️ Назад", callback_data=back.pack()),
src/handlers/help.py                  114  kb.row(InlineKeyboardButton(text="↩️ Назад", callback_data="back_to_help"))
src/handlers/shop.py                   48  back_button = InlineKeyboardButton(text="↩️ Назад", callback_data="back_to_shop")
src/handlers/shop.py                   65  back_button = InlineKeyboardButton(text="↩️ Назад", callback_data="back_to_shop")
src/handlers/shop.py                   79  back_button = InlineKeyboardButton(text="↩️ Назад", callback_data="back_to_shop")
src/utils/utils.py                     89  kb.row(InlineKeyboardButton(text="▶️ Єбаш", callback_data=play.pack()),
src/handlers/help.py                   21  InlineKeyboardButton(text="⚽", callback_data=HelpCallback(game=Games.FOOTBALL).pack()),
src/handlers/dice.py                   46  InlineKeyboardButton(text="⛔️ Нахуй", callback_data=cancel.pack()), width=1)
src/handlers/game.py                   46  InlineKeyboardButton(text="⛔️ Нахуй", callback_data=cancel.pack()), width=1)
src/handlers/give.py                   56  kb.row(InlineKeyboardButton(text="⛔️ Нахуй", callback_data=no.pack()))
src/handlers/give.py                   55  kb.row(InlineKeyboardButton(text="✅ Єбаш", callback_data=yes.pack()))
src/handlers/dice.py                   44  InlineKeyboardButton(text="✖️ Непарне", callback_data=odd.pack()), width=2)
src/utils/utils.py                     34  kb.row(InlineKeyboardButton(text="⛔ Нахуй", callback_data=BetCallback(user_id=user_id, bet=0,
src/utils/utils.py                     91  InlineKeyboardButton(text="⛔ Нахуй", callback_data=cancel.pack()), width=1)
src/handlers/shop.py                   19  kb.row(InlineKeyboardButton(text="❔ Як купити?", callback_data=how_to_buy_btn.pack()))
src/handlers/dice.py                   43  kb.row(InlineKeyboardButton(text="➗ Парне", callback_data=even.pack()),
src/utils/utils.py                     90  InlineKeyboardButton(text="↩️ Назад", callback_data=back.pack()),
src/handlers/help.py                   18  InlineKeyboardButton(text="🎯", callback_data=HelpCallback(game=Games.DARTS).pack()),
src/handlers/help.py                   22  InlineKeyboardButton(text="🎰", callback_data=HelpCallback(game=Games.CASINO).pack())
src/handlers/help.py                   17  InlineKeyboardButton(text="🎲", callback_data=HelpCallback(game=Games.DICE).pack()),
src/handlers/help.py                   19  InlineKeyboardButton(text="🎳", callback_data=HelpCallback(game=Games.BOWLING).pack()),
src/handlers/help.py                   20  InlineKeyboardButton(text="🏀", callback_data=HelpCallback(game=Games.BASKETBALL).pack()),
src/handlers/shop.py                   20  kb.row(InlineKeyboardButton(text="💲 Яка ціна?", callback_data=what_is_price_btn.pack()))
src/handlers/shop.py                   21  kb.row(InlineKeyboardButton(text="💳 Куди підуть гроші?", callback_data=where_money_go_btn.pack()))
src/handlers/game.py                   44  kb.row(*[InlineKeyboardButton(text="🧌", callback_data=cell.pack()) for cell in cells], width=3)
src/handlers/game.py                   84 await callback.message.edit_text("🧌 Перевіряю..")
src/handlers/football.py               41 await callback.message.edit_text(Text("⚽ Забиваю м'яч..").as_markdown())
src/handlers/darts.py                  40 await callback.message.edit_text(Text("🎯 Кидаю дротик..").as_markdown())
src/handlers/casino.py                 41 await callback.message.edit_text(Text("🎰 Довбаний рот цього казино, блядь! "
                                          											"Ти хто такий, сука, щоб це зробити?..").as_markdown())
src/handlers/dice.py                   64 await callback.message.edit_text(Text("🎲 Кидаю кістки..").as_markdown())
src/handlers/bowling.py                41 await callback.message.edit_text(Text("🎳 Кидаю шар..").as_markdown())
src/handlers/basketball.py             42 await callback.message.edit_text(Text("🏀 Кидаю м'яч..").as_markdown())
src/filters.py                         64 await callback.message.edit_text(TextBuilder("🫵😂 Пішов нахуй, бомж. Зароби спочатку русофобію").render())
src/handlers/games.py                  53 await callback.message.edit_text(TextBuilder(f"⚠️ Лох злякався. "
                                                 										f"{"{bet} " if callback_data.bet > 0 else ""}кг повернуто",
                                                 										bet=callback_data.bet).render())
src/handlers/help.py                   38 await query.message.edit_text("⚙️ Тут ти можеш почитати\nпро мене все", reply_markup=kb.as_markup())
src/handlers/give.py                  102 await query.message.edit_text("✅ Ну ок, хулі")
src/handlers/shop.py                   88 await query.message.edit_text("💳 Хочеш більше русофобії?\n"
