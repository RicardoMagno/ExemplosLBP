import unittest
import numpy as np
import pdb
import scipy

from codigo import LBP

class UT_LBP(unittest.TestCase):
	
	valores_p = {4,8,16}
	valores_r = {1,2,3}
	######################################
	def setUp(self):
		pass
	
	######################################
	'''
	def test_computeLBP(self):
	
		lbp = LBP()
		
		imgName = 'imgTstLbp.png'
		img1 = scipy.misc.imread(imgName, flatten=True)
		
		matLbp = lbp.computeLBP(img1, 4, 1)
		
		self.assertEqual(matLbp[0,0], -1)
	'''
	def test_calculates_x_coordinate(self):
		lbp = LBP()
		xc = 2
		r = 1
		pixel = 1
		P = 4
		x1 = xc + 1
		x2 = xc
		x3 = xc - 1
		x4 = xc
		x_viz1 = lbp.calculates_x_coordinate(xc, r, 4, P)
		x_viz2 = lbp.calculates_x_coordinate(xc, r, 3, P)
		x_viz3 = lbp.calculates_x_coordinate(xc, r, 2, P)
		x_viz4 = lbp.calculates_x_coordinate(xc, r, 1, P)

		self.assertEqual(x1, x_viz1)
		self.assertEqual(x2, x_viz2)
		self.assertEqual(x3, x_viz3)
		self.assertEqual(x4, x_viz4)

	def testAutoValueX(self):
		lbp = LBP()
		xc = 2
		for P in (4,8,16):
			for r in (1,2,3):
				x = np.zeros((1, P))
				x[0] = xc + r
				x[0][(P/4):P*3/4] = xc - r
				x[0][(P/4)] = xc
				x[0][(P*3/4)] = xc
				for i in range(P-1,-1,-1):
					if(x[0][i]!=lbp.calculates_x_coordinate(xc, r, i, P)):
						print " ",xc,r,i,P
					self.assertEqual(x[0][i], lbp.calculates_x_coordinate(xc, r, i+1, P))
	
	def test_calculates_y_coordinate(self):
		lbp = LBP()
		yc = 2
		r = 1
		pixel = 1
		P = 4
		
		y1 = yc
		y2 = yc - 1
		y3 = yc
		y4 = yc + 1
		
		y_viz1 = lbp.calculates_y_coordinate(yc, r, 4, P)
		y_viz2 = lbp.calculates_y_coordinate(yc, r, 3, P)
		y_viz3 = lbp.calculates_y_coordinate(yc, r, 2, P)
		y_viz4 = lbp.calculates_y_coordinate(yc, r, 1, P)
		
		self.assertEqual(y1, y_viz1)
		self.assertEqual(y2, y_viz2)
		self.assertEqual(y3, y_viz3)
		self.assertEqual(y4, y_viz4)
		
	def testAutoValueY(self):
		lbp = LBP()
		yc = 2
		for P in (4,8,16):
			for r in (1,2,3):
				y = np.zeros((1, P))
				y[0][0] = yc
				y[0][1:P/2] = yc - r
				y[0][P/2] = yc
				y[0][P/2+1:] = yc + r
				"""de P-1 para 0"""
				for i in range(P-1,-1,-1):
					if(y[0][i]!=lbp.calculates_y_coordinate(yc, r, i, P)):
						print " ",yc,r,i,P
					self.assertEqual(y[0][i], lbp.calculates_y_coordinate(yc, r, i+1, P))

	def test_calculates_binary(self):
		#calculates_binary(self, matVals)
		lbp = LBP()
		matVals = np.zeros((1,4))
		matVals[0,0] = 0
		matVals[0,1] = 1
		matVals[0,2] = 0
		matVals[0,3] = 1
		binNum = lbp.calculates_binary(matVals)
		self.assertEqual(binNum, 5)
		
		matVals2 = np.zeros((1,4))
		matVals2[0,0] = 1
		matVals2[0,1] = 1
		matVals2[0,2] = 1
		matVals2[0,3] = 1
		binNum2 = lbp.calculates_binary(matVals2)
		self.assertEqual(binNum2, 15)
		
if __name__ == '__main__':
    unittest.main()
