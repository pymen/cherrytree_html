# -*- coding: UTF-8 -*-
import os, sys

VERSION = "0.32.0"
APP_NAME = "cherrytree"
NEWER_VERSION_URL = "http://www.giuspen.com/software/version_cherrytree"
if sys.platform.startswith("win"):
    IS_WIN_OS = True
    CONFIG_DIR = os.path.join(os.environ['APPDATA'], APP_NAME)
    if SHARE_PATH:
        EXE_DIR = SHARE_PATH
        os.chdir(EXE_DIR)
    else: EXE_DIR = os.getcwd()
    TMP_FOLDER = os.path.join(os.environ['TEMP'], 'ct_tmp/')
    GLADE_PATH = os.path.join(EXE_DIR, 'glade/')
    SPECS_PATH = os.path.join(EXE_DIR, 'language-specs/')
    LOCALE_PATH = os.path.join(EXE_DIR, 'locale/')
else:
    IS_WIN_OS = False
    CONFIG_DIR = os.path.join(os.path.expanduser('~'), '.config/cherrytree')
    TMP_FOLDER = '/tmp/ct_tmp/'
    if not SHARE_PATH:
        GLADE_PATH = os.path.join(os.getcwd(), "glade/")
        SPECS_PATH = os.path.join(os.getcwd(), 'language-specs/')
        LOCALE_PATH = os.path.join(os.getcwd(), 'locale/')
    else:
        GLADE_PATH = os.path.join(SHARE_PATH, 'cherrytree/glade/')
        SPECS_PATH = os.path.join(SHARE_PATH, 'cherrytree/language-specs')
        LOCALE_PATH = os.path.join(SHARE_PATH, 'locale')
CONFIG_PATH = os.path.join(CONFIG_DIR, 'config.cfg')
LANG_PATH = os.path.join(CONFIG_DIR, 'lang')
IMG_PATH = os.path.join(CONFIG_DIR, 'img_tmp.png')

try:
    import appindicator
    HAS_APPINDICATOR = True
except: HAS_APPINDICATOR = False


XDG_CURRENT_DESKTOP = 'XDG_CURRENT_DESKTOP'
HAS_SYSTRAY = not (XDG_CURRENT_DESKTOP in os.environ and os.environ[XDG_CURRENT_DESKTOP] == "Unity")

AVAILABLE_LANGS = ['default', 'cs', 'de', 'en', 'es', 'fr', 'it', 'nl', 'pl', 'pt_BR', 'ru', 'uk', 'zh_CN']
COLOR_48_LINK_WEBS = "#00004444ffff"
COLOR_48_LINK_NODE = "#071c838e071c"
COLOR_48_LINK_FILE = "#8b8b69691414"
COLOR_48_LINK_FOLD = "#7f7f7f7f7f7f"
COLOR_48_YELLOW = "#bbbbbbbb0000"
COLOR_48_WHITE = "#ffffffffffff"
COLOR_48_BLACK = "#000000000000"
COLOR_24_BLACK = "#000000"
COLOR_24_WHITE = "#ffffff"
COLOR_24_BLUEBG = "#001b33"
COLOR_24_LBLACK = "#0b0c0c"
COLOR_24_GRAY = "#e0e0e0"
RICH_TEXT_DARK_FG = COLOR_24_WHITE
RICH_TEXT_DARK_BG = COLOR_24_BLUEBG
RICH_TEXT_LIGHT_FG = COLOR_24_BLACK
RICH_TEXT_LIGHT_BG = COLOR_24_WHITE
TREE_TEXT_DARK_FG = COLOR_24_WHITE
TREE_TEXT_DARK_BG = COLOR_24_BLUEBG
TREE_TEXT_LIGHT_FG = COLOR_24_LBLACK
TREE_TEXT_LIGHT_BG = COLOR_24_GRAY
BAD_CHARS = "[\x00-\x08\x0b-\x1f]"
GTKSPELLCHECK_TAG_NAME = "gtkspellchecker-misspelled"
TAG_WEIGHT = "weight"
TAG_FOREGROUND = "foreground"
TAG_BACKGROUND = "background"
TAG_STYLE = "style"
TAG_UNDERLINE = "underline"
TAG_STRIKETHROUGH = "strikethrough"
TAG_SCALE = "scale"
TAG_FAMILY = "family"
TAG_JUSTIFICATION = "justification"
TAG_LINK = "link"
TAG_PROP_HEAVY = "heavy"
TAG_PROP_ITALIC = "italic"
TAG_PROP_MONOSPACE = "monospace"
TAG_PROP_SINGLE = "single"
TAG_PROP_TRUE = "true"
TAG_PROP_H1 = "h1"
TAG_PROP_H2 = "h2"
TAG_PROP_H3 = "h3"
TAG_PROP_H4 = "h4"
TAG_PROP_H5 = "h5"
TAG_PROP_H6 = "h6"
TAG_PROP_SUP = "sup"
TAG_PROP_SUB = "sub"
TAG_PROP_LEFT = "left"
TAG_PROP_CENTER = "center"
TAG_PROP_RIGHT = "right"
TAG_PROPERTIES = [TAG_WEIGHT, TAG_FOREGROUND, TAG_BACKGROUND, TAG_STYLE, TAG_UNDERLINE,
                  TAG_STRIKETHROUGH, TAG_SCALE, TAG_FAMILY, TAG_JUSTIFICATION, TAG_LINK]
LINK_TYPE_WEBS = "webs"
LINK_TYPE_FILE = "file"
LINK_TYPE_FOLD = "fold"
LINK_TYPE_NODE = "node"
CUSTOM_COLORS_ID = "custom-colors"
STYLE_SCHEME_DEFAULT = "cobalt"
ANCHOR_CHAR = GLADE_PATH + 'anchor.png'
NODES_ICONS = {0:'cherry_red', 1:'cherry_blue', 2:'cherry_orange', 3:'cherry_cyan',
               4:'cherry_orange_dark', 5:'cherry_sherbert', 6:'cherry_yellow'}
CODE_ICONS = {"python": 'cherry_green', "sh":'cherry_purple',
              "c":'cherry_black', "cpp":'cherry_black', "chdr":'cherry_black'}

MAX_FILE_NAME_LEN = 150
WHITE_SPACE_BETW_PIXB_AND_TEXT = 3
GRID_SLIP_OFFSET = 3
MAIN_WIN_TO_TEXT_WIN_NORMALIZER = 50
MAX_RECENT_DOCS = 10
TABLE_DEFAULT_COL_MIN = 40
TABLE_DEFAULT_COL_MAX = 400

CHAR_SPACE = " "
CHAR_NEWLINE = "\n"
CHAR_NEWPAGE = "\x0c"
CHAR_CR = "\r"
CHAR_TAB = "\t"
CHAR_LISTBUL = "•"
CHAR_LISTARR = "►"
CHAR_LISTTODO = "☐"
CHAR_LISTDONEOK= "☑"
CHAR_LISTDONEFAIL= "☒"
CHAR_TILDE = "~"
CHAR_MINUS = "-"
CHAR_DQUOTE = '"'
CHAR_SQUOTE = "'"
CHAR_SLASH = "/"
CHAR_BSLASH = "\\"
CHAR_SQ_BR_OPEN = "["
CHAR_SQ_BR_CLOSE = "]"
CHAR_PARENTH_OPEN = "("
CHAR_PARENTH_CLOSE = ")"
CHAR_LESSER = "<"
CHAR_GREATER = ">"
CHAR_STAR = "*"
CHAR_QUESTION = "?"
CHAR_COLON = ":"
CHAR_USCORE = "_"
CHAR_EQUAL = "="
CHAR_BR_OPEN = "{"
CHAR_BR_CLOSE = "}"
CHAR_CARET = "^"
CHAR_PIPE = "|"

SPECIAL_CHAR_ARROW_RIGHT = "→"
SPECIAL_CHAR_ARROW_LEFT = "←"
SPECIAL_CHAR_ARROW_DOUBLE = "↔"
SPECIAL_CHAR_COPYRIGHT = "©"
SPECIAL_CHAR_UNREGISTERED_TRADEMARK = "™"
SPECIAL_CHAR_REGISTERED_TRADEMARK = "®"

STR_CURSOR_POSITION = "cursor-position"
STR_STOCK_CT_IMP = "import_in_cherrytree"
STR_VISIBLE = "visible"
STR_UTF8 = "utf-8"
STR_UTF16 = "utf-16"
STR_IGNORE = "ignore"
STR_RETURN = "Return"
STR_PYGTK_222_REQUIRED = "PyGTK 2.22 required"
