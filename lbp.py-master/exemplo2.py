
import scipy
import scipy.misc
import pdb
import numpy as np

class LBP:
	
	def __init__(self):
		pass

	def computeLBP(self, imgIn, p=4, r=1):
	
		matVals = np.zeros((1, p))
		matLbp = np.zeros((len(imgIn), len(imgIn[0])))
	
		for row in range(r, len(imgIn)-r):
			for col in range(r, len(imgIn[row])-r):
				centerValue = int(imgIn[row,col])

				if int(imgIn[row-r,col]) > centerValue:
					matVals[0,0] = 1
				if int(imgIn[row,col+r]) > centerValue:
					matVals[0,1] = 2
				if int(imgIn[row+r,col]) > centerValue:
					matVals[0,2] = 4
				if int(imgIn[row,col-r]) > centerValue:
					matVals[0,3] = 8
				dec = np.sum(matVals)
				print dec
				matLbp[row,col] = dec
				
		return matLbp
				
	def getHistogram(self, imgIn):

		hist = np.zeros((1, 256))
	
		for row in range(0, len(imgIn)):
			for col in range(0, len(imgIn[row])):
				value = imgIn[row,col]
				#pdb.set_trace()
				hist[0][int(value)] = hist[0][int(value)] + 1
		return hist

	def equalizeHistogram(self, imgIn):
	
	#	pdb.set_trace()	
		
		quantRows = len(imgIn)
		quantCols = len(imgIn[0])
	
		imgHE = np.zeros((quantRows, quantCols))
	
		hist = self.getHistogram(imgIn)
		minValHist = np.amin(hist)
	
		for row in range(0, len(imgIn)):
			for col in range(0, len(imgIn[row])):
				#imgHE[row, col] = imgIn[row,col]/(quantRows*quantCols)
				value = imgIn[row,col]
				imgHE[row, col] = ((hist[0,int(value)] - minValHist)/(quantRows*quantCols-1))*255
			#print imgHE[row, col]
	
		return imgHE


lbp = LBP()


if __name__=="__main__":
	imgName = '/home/eanes/Documents/DSC/2017/estudosPythonAlunos/imagens/jaffeimages (1)/jaffe/KA.AN1.39.tiff'

	img1 = scipy.misc.imread(imgName, flatten=True)
#scipy.misc.imshow(img1)

	lbp.computeLBP(img1)

	scipy.misc.imsave('imgSaida.jpg', img1)

	imgHE = lbp.equalizeHistogram(img1)

	scipy.misc.imshow(imgHE)

	imgResized = scipy.misc.imresize(imgHE, (64, 64))
	scipy.misc.imsave('imgResized.jpg', imgResized)

