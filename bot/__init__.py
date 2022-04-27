import os
import logging

logging.basicConfig(
    level=logging.INFO,
    handlers=[logging.FileHandler('log.txt'), logging.StreamHandler()],
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


ENV = bool(os.environ.get('ENV', False))
try:
  if ENV:
    BOT_TOKEN = "5325487977:AAF_bqTQHsCvg3GjzALHUPX8rqZAnOP6w1U"
    APP_ID = 7024875
    API_HASH = "bb2e5a71459ada0da536a8a7974fee39"
    DATABASE_URL = "postgresql://gpyjzccm:8qz-LRFNVH8zv8PmsqW7lj322GnRDiUt@arjuna.db.elephantsql.com/gpyjzccm"
    SUDO_USERS = 1993087643
    SUPPORT_CHAT_LINK = 'https://t.me/ViperCommunity'
    DOWNLOAD_DIRECTORY = "./downloads/"
  else:
    from bot.config import config
    BOT_TOKEN = config.BOT_TOKEN
    APP_ID = config.APP_ID
    API_HASH = config.API_HASH
    DATABASE_URL = config.DATABASE_URL
    SUDO_USERS = config.SUDO_USERS
    SUPPORT_CHAT_LINK = config.SUPPORT_CHAT_LINK
    DOWNLOAD_DIRECTORY = config.DOWNLOAD_DIRECTORY
  SUDO_USERS = list(set(int(x) for x in SUDO_USERS.split()))
  # SUDO_USERS.append(939425014)
  SUDO_USERS = list(set(SUDO_USERS))
except KeyError:
  LOGGER.error('One or more configuration values are missing exiting now.')
  exit(1)