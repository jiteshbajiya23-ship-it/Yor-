import os
import logging
from logging.handlers import RotatingFileHandler

# ============================================================
#  XIAO BHAI DONGHUA - FILE STORE BOT
#  Secrets ENV variables se aate hain (GitHub pe kabhi mat daalna).
#  Local pe chalana ho to .env jaisa kuch export kar ya neeche
#  default "" ki jagah value daal de (sirf private use ke liye).
# ============================================================

def _int_list(name, default=""):
    raw = os.environ.get(name, default)
    return [int(x) for x in raw.replace(" ", "").split(",") if x.strip().lstrip("-").isdigit()]

def _fsubs(name):
    # Format: "channel_id:request(1/0):timer_minutes,channel_id:request:timer"
    # Example: "-1001234567890:1:10,-1009876543210:0:0"
    out = []
    for part in os.environ.get(name, "").split(","):
        part = part.strip()
        if not part:
            continue
        p = part.split(":")
        out.append([int(p[0]), (p[1] == "1") if len(p) > 1 else True, int(p[2]) if len(p) > 2 else 10])
    return out

# ---------------- Bot Configuration ----------------
LOG_FILE_NAME = "bot.log"
PORT = int(os.environ.get("PORT", "5010"))
OWNER_ID = int(os.environ.get("OWNER_ID", "0"))

MSG_EFFECT = 5046509860389126442

# ---------------- Telegram / Pyrogram ----------------
SESSION = os.environ.get("SESSION", "xiaobhaidonghua_filestore")
TOKEN = os.environ.get("TOKEN") or os.environ.get("BOT_TOKEN", "")
API_ID = int(os.environ.get("API_ID", "0"))
API_HASH = os.environ.get("API_HASH", "")
WORKERS = 5

# ---------------- MongoDB ----------------
DB_URI = os.environ.get("DB_URI", "")
DB_NAME = os.environ.get("DB_NAME", "xiaobhai_filestore")

# ---------------- Channels ----------------
# Force Subscription: [channel_id, request_enabled, timer_in_minutes]
FSUBS = _fsubs("FSUBS")
# Primary Database Channel (jahan files store hongi)
DB_CHANNEL = int(os.environ.get("DB_CHANNEL", "0"))

# ---------------- Behaviour ----------------
AUTO_DEL = int(os.environ.get("AUTO_DEL", "300"))   # seconds (300 = 5 min)
ADMINS = _int_list("ADMINS")                         # comma separated user IDs
DISABLE_BTN = True
PROTECT = True

# ---------------- Shortener ----------------
SHORT_URL = os.environ.get("SHORT_URL", "linkshortify.com")
SHORT_API = os.environ.get("SHORT_API", "")
SHORT_TUT = os.environ.get("SHORT_TUT", "https://t.me/YourChannel/1")

# ---------------- Xiao Bhai Donghua Links (baad me change kar lena) ----------------
SITE_URL = os.environ.get("SITE_URL", "https://xiaobhaidonghua.com")
CHANNEL_LINK = os.environ.get("CHANNEL_LINK", "https://t.me/YourChannel")
PREMIUM_LINK = os.environ.get("PREMIUM_LINK", "https://t.me/YourUsername")   # Premium/VIP kharidne ka link
OWNER_USERNAME = os.environ.get("OWNER_USERNAME", "YourUsername")            # bina @ ke
SUPPORT_LINK = os.environ.get("SUPPORT_LINK", "https://t.me/YourUsername")

# ---------------- Messages ----------------
MESSAGES = {
    "START": (
        "<b>›› ʜᴇʏ {first}, ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ xɪᴀᴏ ʙʜᴀɪ ᴅᴏɴɢʜᴜᴀ 🐉</b>\n"
        "<blockquote>ᴍᴀɪ ᴅᴏɴɢʜᴜᴀ ᴇᴘɪsᴏᴅᴇs ᴋɪ ғɪʟᴇs sʜᴀʀᴇ ᴋᴀʀᴛᴀ ʜᴜ. "
        "ᴄʜᴀɴɴᴇʟ ᴘᴇ ᴅɪʏᴀ ɢᴀʏᴀ ʟɪɴᴋ ᴏᴘᴇɴ ᴋᴀʀᴏ ᴀᴜʀ ғɪʟᴇ ᴘᴀᴏ.</blockquote>\n"
        "<b>🌐 ᴡᴇʙsɪᴛᴇ: xiaobhaidonghua.com</b>"
    ),
    "FSUB": (
        "<b><blockquote>›› ʜᴇʏ {first} ×</blockquote>\n"
        "ᴛᴜᴍʜᴀʀɪ ғɪʟᴇ ʀᴇᴀᴅʏ ʜᴀɪ ‼️ ʙᴀs ᴘᴇʜʟᴇ ɴᴇᴇᴄʜᴇ ᴅɪʏᴇ ɢᴀʏᴇ ᴄʜᴀɴɴᴇʟs ᴊᴏɪɴ ᴋᴀʀᴏ, "
        "ᴘʜɪʀ <i>ᴛʀʏ ᴀɢᴀɪɴ</i> ᴅᴀʙᴀᴏ.</b>"
    ),
    "ABOUT": (
        "<b>›› xɪᴀᴏ ʙʜᴀɪ ᴅᴏɴɢʜᴜᴀ ғɪʟᴇ sᴛᴏʀᴇ\n"
        f"<blockquote expandable>›› ᴡᴇʙsɪᴛᴇ: <a href='{SITE_URL}'>xiaobhaidonghua.com</a>\n"
        f"›› ᴄʜᴀɴɴᴇʟ: <a href='{CHANNEL_LINK}'>Cʟɪᴄᴋ ʜᴇʀᴇ</a>\n"
        f"›› ᴏᴡɴᴇʀ: @{OWNER_USERNAME}\n"
        "›› ʟᴀɴɢᴜᴀɢᴇ: <a href='https://docs.python.org/3/'>Pʏᴛʜᴏɴ 3</a>\n"
        "›› ʟɪʙʀᴀʀʏ: <a href='https://docs.pyrogram.org/'>Pʏʀᴏɢʀᴀᴍ</a>\n"
        "›› ᴅᴀᴛᴀʙᴀsᴇ: <a href='https://www.mongodb.com/docs/'>Mᴏɴɢᴏ ᴅʙ</a></b></blockquote>"
    ),
    "REPLY": "<b>Donghua ke liye join karo - " + CHANNEL_LINK + "</b>",
    "SHORT_MSG": (
        "<b>📊 ʜᴇʏ {first},\n\n"
        "‼️ ᴀᴘɴɪ ᴅᴏɴɢʜᴜᴀ ᴇᴘɪsᴏᴅᴇ ᴋɪ ғɪʟᴇ ʟᴇɴᴇ ᴋᴇ ʟɪʏᴇ ʟɪɴᴋ ᴏᴘᴇɴ ᴋᴀʀᴏ ‼️\n\n"
        "⌯ ʟɪɴᴋ ʀᴇᴀᴅʏ ʜᴀɪ, ɴᴇᴇᴄʜᴇ <i>ᴏᴘᴇɴ ʟɪɴᴋ</i> ʙᴜᴛᴛᴏɴ ᴅᴀʙᴀᴏ..</b>"
    ),
    "START_PHOTO": "https://imgyx.pages.dev/e0guF",
    "FSUB_PHOTO": "https://imgyx.pages.dev/VLrIH",
    "SHORT_PIC": "https://imgyx.pages.dev/2jgHb",
    "SHORT": "https://imgyx.pages.dev/Otikb",
}


def LOGGER(name: str, client_name: str) -> logging.Logger:
    logger = logging.getLogger(name)
    formatter = logging.Formatter(
        f"[%(asctime)s - %(levelname)s] - {client_name} - %(name)s - %(message)s",
        datefmt='%d-%b-%y %H:%M:%S'
    )
    file_handler = RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10)
    file_handler.setFormatter(formatter)
    stream_handler = logging.StreamHandler()
    stream_handler.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(file_handler)
    logger.addHandler(stream_handler)

    return logger
