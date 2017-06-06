import test_twitter_cnn as cnn
#import twitterpull
import sys
import subprocess as sub

def main(twitterhandle, folder):	
	alltweets = ['hello', 'strong and stable']#twitterpull.get_all_tweets(twitterhandle)
 	print('python test_twitter_cnn.py --load ' + folder + ' --custom_multiple_input ' + twitterhandle)
 	sys.stdout.flush

 	pipe = sub.Popen('python test_twitter_cnn.py --load ' + folder + ' --custom_multiple_input ' + twitterhandle, stdout=sub.PIPE)
 	text = sub.pipe.communicate()[0]
 	return text


arguments = sys.argv
twitterhandle = arguments[1]
folder = arguments[2]

if __name__ == "__main__":
    print(main(twitterhandle,folder))
    sys.stdout.flush()