from sklearn.ensemble import GradientBoostingClassifier
import numpy as np


def loadData():
        global dataSet
        global X,YP,YV,valPop,valVir
        global validationData
        validationData =[]
        dataSet = []
        labeled = []
        global videos
        videos =[]

        global labeledPopular
        global labeledViral
        
        with open('predictionData.txt') as fp:
                for line in fp:
                        line = line.strip('\n')
                        features= (line.split(','))
                        features = [ float(x) for x in features ]
                        videos.append(features)
                        
        with open('trainingKnown.txt') as fp:
                for line in fp:
                        line = line.strip('\n')
                        features= (line.split(','))
                        features = [ float(x) for x in features ]
                        dataSet.append(features)

        with open('labelingKnown.txt') as fp:
                for line in fp:
                        line = line.strip('\n')
                        line = line.strip('[')
                        line = line.strip(']')
                        labels= (line.split(','))
                        labels = [ int(x) for x in labels ]
                        labeled.append(labels)

        with open('validationData.txt') as fp:
                for line in fp:
                        line = line.strip('\n')
                        line = line.strip('[')
                        line = line.strip(']')
                        labels= (line.split(','))
                        labels = [ int(x) for x in labels ]
                        validationData.append(labels)

        # Convert Lists to numpy array with X,Y convention
        # X_train = X
        # X_test = videos
        # Y_train = YP/YV
        # Y_test = valPop/valVir
        X = np.array(dataSet)
        videos = np.array(videos)
        YP = np.array(labeled[0])
        YV = np.array(labeled[1])
        valPop = np.array(validationData[0])
        valVir = np.array(validationData[1])
        

def classify():

        #Predict Popularity
        gbdt = GradientBoostingClassifier()
        gbdt.fit(X,YP)
        gbdt.predict(videos)
        print(valVir.shape)
        prediction = gbdt.predict(videos)
        print(prediction)

        same=0
        for i in range(0,valPop.size):
                if valPop[i]==prediction[i]:
                        same = same+1

        accurancy = same/valPop.size *100
        print(accurancy)

        
def main():
        loadData()
        classify()

if __name__=='__main__':
        main()
