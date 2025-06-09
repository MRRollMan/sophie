from enum import StrEnum

from aiogram.filters.callback_data import CallbackData


class Games(StrEnum):
    KILLRU = "killru"
    GAME = "game"
    DICE = "dice"
    DARTS = "darts"
    BOWLING = "bowling"
    BASKETBALL = "basketball"
    FOOTBALL = "football"
    CASINO = "casino"


class Actions(StrEnum):
    GIVE = "give"


class BaseGameEnum(StrEnum):
    PLAY = "play"
    BACK = "back"
    CANCEL = "cancel"


class BetButtonType(StrEnum):
    BET = "bet"
    CANCEL = "cancel"


class DiceParityEnum(StrEnum):
    EVEN = "even"
    ODD = "odd"
    BACK = "back"
    CANCEL = "cancel"


class GameCellEnum(StrEnum):
    CELL = "cell"
    BACK = "back"
    CANCEL = "cancel"


class SettingsEnum(StrEnum):
    MINIGAMES = "minigames"
    GIVE = "give"


class ShopEnum(StrEnum):
    HOW_TO_BUY = "how_to_buy"
    WHAT_IS_PRICE = "what_is_price"
    WHERE_MONEY_GO = "where_money_go"


class GiveEnum(StrEnum):
    YES = "yes"
    NO = "no"


class BetCallback(CallbackData, prefix="bet"):
    user_id: int
    bet: int
    action: BetButtonType
    game: Games


class GameCallback(CallbackData, prefix="game"):
    user_id: int
    bet: int
    cell: GameCellEnum


class DiceCallback(CallbackData, prefix="dice"):
    user_id: int
    bet: int
    parity: DiceParityEnum


class BaseGameCallback(CallbackData, prefix="games"):
    user_id: int
    bet: int
    action: BaseGameEnum
    game: Games


class LeaveCallback(CallbackData, prefix="leave"):
    user_id: int
    confirm: bool


class SettingsCallback(CallbackData, prefix="settings"):
    setting: SettingsEnum


class ShopCallback(CallbackData, prefix="shop"):
    menu: ShopEnum


class HelpCallback(CallbackData, prefix="help"):
    game: Games


class GiveCallback(CallbackData, prefix="give"):
    user_id: int
    receiver_id: int
    value: int
    receiver_balance: int
    action: GiveEnum
