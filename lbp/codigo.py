
import scipy
import scipy.misc
import pdb
import numpy as np
import math

class LBPError(Exception): pass
class LBPOutOfRangeError(LBPError): pass

class LBP:

    def __init__(self):
        pass

    # metodo para calcular a coordenada x
    def calculates_x_coordinate(self, xc, r, p, P):
        cos = round(math.cos((math.pi/P)*(2*p)))
        return xc + (r*cos)

    # metodo para calcular a coordenada y
    def calculates_y_coordinate(self, yc, r, p, P):
        sin = round(math.sin((math.pi/P)*(2*p)))
        return yc - (r*sin)

    # metodo para converter o numero binario para decimal
    def calculates_binary(self, matVals):
        num = 0
        binary = 2
        for i in range(len(matVals[0])):
            if matVals[0][i] == 1:
                #transformacao generica
                num += binary**(len(matVals[0])-i-1)
        return num

    def computeLBP(self, imgIn, p, r):
        if not (p<=(r*8)): raise LBPOutOfRangeError, 'p maior que valor possivel'
        matVals = np.zeros((1, p))
        matLbp = np.zeros((len(imgIn), len(imgIn[0])))
        for row in range(r, len(imgIn)-r):
            for col in range(r, len(imgIn[row])-r):
                centerValue = int(imgIn[row,col])
                for i in range(p):
                    if int(imgIn[self.calculates_x_coordinate(row, r, i, p) ,self.calculates_y_coordinate(col, r, i, p)]) > centerValue:
                        matVals[0, i] = 1
                    dec = self.calculates_binary(matVals)
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
    imgName = '/home/ricardo/Documentos/testarAoRedor.xcf'

    img1 = scipy.misc.imread(imgName, flatten=True)
    #scipy.misc.imshow(img1)

    lbp.computeLBP(img1, 16, 2)

    scipy.misc.imsave('imgSaida2.jpg', img1)

    imgHE = lbp.equalizeHistogram(img1)

    scipy.misc.imshow(imgHE)

    imgResized = scipy.misc.imresize(imgHE, (64, 64))
    scipy.misc.imsave('imgResized.jpg', imgResized)

