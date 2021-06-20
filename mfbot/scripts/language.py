import gettext
import os
import locale

current_locale, encoding = locale.getdefaultlocale()

locpath = os.path.dirname(__file__)

lang = gettext.translation("argparse", os.path.join(locpath, "../locale"), [current_locale], fallback=True)