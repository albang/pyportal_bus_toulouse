import time
import board
from adafruit_pyportal import PyPortal
from secrets import secrets

stop_id="1970324837184814"
schedule_index=0
# Set up where we'll be fetching data from
DATA_SOURCE = "https://api.tisseo.fr/v1/stops_schedules.json?key="+secrets["tisseo_token"]+"&stopAreaId="+stop_id+"&timetableByArea=1"
DESTINATION_NAME = ['departures', 'stopAreas',0,'schedules',schedule_index,'destination','name']
FIRST_BUS = ['departures', 'stopAreas',0,'schedules',schedule_index,'journeys',0,'waiting_time']
SECOND_BUS = ['departures', 'stopAreas',0,'schedules',schedule_index,'journeys',1,'waiting_time']

# the current working directory (where this file is)
cwd = ("/"+__file__).rsplit('/', 1)[0]
pyportal = PyPortal(url=DATA_SOURCE,
                    json_path=(DESTINATION_NAME, FIRST_BUS,SECOND_BUS),
                    status_neopixel=board.NEOPIXEL,
                    default_bg=cwd+"/bus_free.bmp",
                    text_font=cwd+"/fonts/Arial-Bold-24.bdf",
                    text_position=((50, 40),  # Stop location
                                   (50, 80),
                                   (50, 120)), # time
                    text_color=(0xFFFFFF,  # quote text color
                                0x8080FF,
                                0x8080FF), # author text color
                    text_wrap=(35, # characters to wrap for quote
                               0,0), # no wrap for author
                    text_maxlen=(180, 30,30), # max text size for quote & author
                   )

# speed up projects with lots of text by preloading the font!
pyportal.preload_font()

while True:
    try:
        value = pyportal.fetch()
        print("Response is", value)
    except RuntimeError as e:
        print("Some error occured, retrying! -", e)
    time.sleep(60)