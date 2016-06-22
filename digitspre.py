# import the necessary packages
from sklearn.cross_validation import train_test_split
from sklearn.metrics import classification_report
from sklearn import datasets
from nolearn.dbn import DBN
import numpy as np
import cv2
from sklearn.externals import joblib
from PIL import Image
from StringIO import StringIO

def process_image_file(image_path):
  image_fp = StringIO(open(image_path,'rb').read())
  try:
    image = Image.open(image_fp)
    return process_image(image)
  except IOError:
    return None

process_image_file('893878_2.png')
print "[X] downloading data..."
dataset = datasets.fetch_mldata("MNIST Original")

(trainX, testX, trainY, testY) = train_test_split(
        dataset.data / 255.0, dataset.target.astype("int0"), test_size = 0.33)

# scale the data to the range [0, 1] and then construct the training
# and testing splits
# each possible output classification, which are the digits 1-10)

# compute the predictions for the test data and show a classification
# report
dbn = joblib.load('dbn.pkl')
preds = dbn.predict(testX)
print classification_report(testY, preds)

# randomly select a few of the test instances
for i in np.random.choice(np.arange(0, len(testY)), size = (10,)):
	# classify the digit
	pred = dbn.predict(np.atleast_2d(testX[i]))
 
	# reshape the feature vector to be a 28x28 pixel image, then change
	# the data type to be an unsigned 8-bit integer
	image = (testX[i] * 255).reshape((28, 28)).astype("uint8")
 
	# show the image and prediction
	print "Actual digit is {0}, predicted {1}".format(testY[i], pred[0])


