"""Constants for the samsungtv_smart integration."""
from enum import Enum


class AppLoadMethod(Enum):
    All = 1
    Default = 2
    NotLoad = 3


class AppLaunchMethod(Enum):
    Standard = 1
    Remote = 2
    Rest = 3


class PowerOnMethod(Enum):
    WOL = 1
    SmartThings = 2

DOMAIN = "samsungtv_tizen"

WS_PREFIX = "[Home Assistant]"

CONF_APP_LIST = "app_list"
CONF_APP_LAUNCH_METHOD = "app_launch_method"
CONF_APP_LOAD_METHOD = "app_load_method"
CONF_CHANNEL_LIST = "channel_list"
CONF_DEVICE_NAME = "device_name"
CONF_DEVICE_MODEL = "device_model"
CONF_SOURCE_LIST = "source_list"
CONF_SHOW_CHANNEL_NR = "show_channel_number"
CONF_WS_NAME = "ws_name"
CONF_DEVICE_OS = "device_os"
CONF_LOAD_ALL_APPS = "load_all_apps"
CONF_POWER_ON_DELAY = "power_on_delay"
CONF_POWER_ON_METHOD = "power_on_method"
CONF_USE_ST_CHANNEL_INFO = "use_st_channel_info"
CONF_USE_ST_STATUS_INFO = "use_st_status_info"
CONF_USE_MUTE_CHECK = "use_mute_check"
CONF_SYNC_TURN_OFF = "sync_turn_off"
CONF_SYNC_TURN_ON = "sync_turn_on"
CONF_WOL_REPEAT = "wol_repeat"
CONF_LOGO_OPTION = "logo_option"

# obsolete
CONF_UPDATE_METHOD = "update_method"
CONF_UPDATE_CUSTOM_PING_URL = "update_custom_ping_url"
CONF_SCAN_APP_HTTP = "scan_app_http"

DEFAULT_PORT = 8001
DEFAULT_TIMEOUT = 5
DEFAULT_POWER_ON_DELAY = 30
DEFAULT_SOURCE_LIST = {"TV": "KEY_TV", "HDMI": "KEY_HDMI"}
DEFAULT_APP = "TV/HDMI"

MAX_WOL_REPEAT = 5

RESULT_NOT_SUCCESSFUL = "not_successful"
RESULT_NOT_SUPPORTED = "not_supported"
RESULT_ST_DEVICE_USED = "st_device_used"
RESULT_ST_DEVICE_NOT_FOUND = "st_device_not_found"
RESULT_ST_MULTI_DEVICES = "st_multiple_device"
RESULT_SUCCESS = "success"
RESULT_WRONG_APIKEY = "wrong_api_key"

SERVICE_SET_ART_MODE = "set_art_mode"

STD_APP_LIST = {
    # app_id: smartthings app id (if different and available)
    "org.tizen.browser": "",                    # Internet
    "11101200001": "RN1MCdNq8t.Netflix",        # Netflix
    "111299001912": "9Ur5IzDKqV.TizenYouTube",  # YouTube
    "3201512006785": "org.tizen.ignition",      # Prime Video
    "3201901017640": "MCmYXNxgcu.DisneyPlus",   # Disney+
    "11091000000": "4ovn894vo9.Facebook",       # Facebook
    "3201601007250": "QizQxC7CUf.PlayMovies",   # Google Play
    "3201606009684": "rJeHak5zRg.Spotify",      # Spotify
}

# Logo feature constants
class LogoOption(Enum):
    Disabled = 1
    WhiteColor = 2
    BlueColor = 3
    BlueWhite = 4
    DarkWhite = 5
    TransparentColor = 6
    TransparentWhite = 7

LOGO_OPTIONS_MAPPING = {
    LogoOption.Disabled: "none",
    LogoOption.WhiteColor: "fff-color",
    LogoOption.BlueColor: "05a9f4-color",
    LogoOption.BlueWhite: "05a9f4-white",
    LogoOption.DarkWhite: "282c34-white",
    LogoOption.TransparentColor: "transparent-color",
    LogoOption.TransparentWhite: "transparent-white",
}
LOGO_OPTION_DEFAULT = [LogoOption.WhiteColor.value, "fff-color"]
LOGO_BASE_URL = "https://jaruba.github.io/channel-logos/"
LOGO_FILE_PATH = "/logo_paths.json"
LOGO_FILE_DOWNLOAD_PATH = "/logo_paths_download.json"
LOGO_FILE_DAYS_BEFORE_UPDATE = 1
LOGO_MIN_SCORE_REQUIRED = 80
LOGO_MEDIATITLE_KEYWORD_REMOVAL = ["HD"]