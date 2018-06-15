# Jonathan Elsner
# 2018-05-10
#
# I went to France for vacation and took a bunch of pictures on my phone and camera. While I changed the time on my
# phone, I forgot to do so on my camera, thus, when I aggregated all of the photos, they were out of order.
#
# I created this simple script to change the time on all of my camera's photos. There were ~1000 of them I think,
# this made short work of them, in less than an hour. (Of course writing the program took a while though...)

import piexif  # import piexif library to work with exif data
from PIL import Image  # import Image from the PIL library to work with images
from datetime import datetime, timedelta  # import datetime and timedelta to manipulate the time
import glob  # import a library to work with files
from os.path import basename  # import a library to parse the filename of a file

# get a list of JPEG files in the directory
files = glob.glob('C:\Users\Jonathan\OneDrive\Pictures\Canon PowerShot G5 X\\100___04\*.JPG')

counter = 0  # initialize a counter

for f in files:  # iterate through the files

	counter += 1  # increment a counter for information purposes

	img = Image.open(f)  # load the image
	exif_dict = piexif.load(img.info['exif'])  # pull the exif data from the image

	str_date = exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal]  # grab the string representation of the creation time
	time = datetime.strptime(str_date, '%Y:%m:%d %H:%M:%S')  # create a datetime object from the exif time string
	new_time = time + timedelta(hours=21)  # increment the time by the correct amount

	# put the correct time back into the exif data
	exif_dict['Exif'][piexif.ExifIFD.DateTimeOriginal] = new_time.strftime('%Y:%m:%d %H:%M:%S')

	bytes = piexif.dump(exif_dict)  # turn the exif data into an array of bytes
	img.save('%s' % f, 'jpeg', exif=bytes)  # save the exif data array back onto the original image

	print('{0}/{1}: {2} {3} -> {4}'.format(counter, len(files), basename(f), time, new_time))  # print out progress info



