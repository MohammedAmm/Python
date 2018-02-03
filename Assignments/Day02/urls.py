import os
import random
# get random number from 0 to 2 and store it in index
index=random.randrange(3)
#make list of urls
urls=["http://www.google.com","http://www.facebook.com","http://www.youtube.com"]
os.system("firefox "+urls[index])