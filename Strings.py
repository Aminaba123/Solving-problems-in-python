############## The particular format for strptime: ############################
datetime.datetime.strptime(string_date, "%Y-%m-%d %H:%M:%S.%f")
datetime.datetime(2013, 9, 28, 20, 30, 55, 782000)

string_date = "2013-09-28 20:30:55.78200"
abc = datetime.datetime.now()

if abc  > string_date :
    print True

############### How to convert a date string to different format #####################

datetime.datetime.strptime("2013-1-25", '%Y-%m-%d').strftime('%m/%d/%y')

############### Converting string into datetime ###############

# datetime.strptime is the main routine for parsing strings into datetimes. It can handle all sorts of formats, 
# with the format determined by a format string you give it

from datetime import datetime

datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')

#######################################################################################

