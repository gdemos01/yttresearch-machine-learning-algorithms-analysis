import matplotlib.pyplot as plt
import numpy as np
import os

def load_tw_train_all(dir,t,o,l):
        
        # tw_train_all
        name = 'tw_train_all_'+str(t)+str(o)+str(l)+'.txt'
        with open(os.path.join(dir,name)) as fp:
                dataSet =[]
                for line in fp:
                        line = line.strip('\n')
                        features= (line.split(','))
                        features = [ float(x) for x in features ]
                        dataSet.append(features)

        tw_train_all = np.array(dataSet)
        
        return tw_train_all

def load_tw_train_all_recent(dir,t,o,l):
        name = 'tw_train_all_recent_'+str(t)+str(o)+str(l)+'.txt'
        with open(os.path.join(dir,name)) as fp:
                dataSet =[]
                for line in fp:
                        line = line.strip('\n')
                        features= (line.split(','))
                        features = [ float(x) for x in features ]
                        dataSet.append(features)

        tw_train_all_recent = np.array(dataSet)
        return tw_train_all_recent

def load_tw_train_base(dir,t,o,l):
        name = 'tw_train_base_'+str(t)+str(o)+str(l)+'.txt'
        with open(os.path.join(dir,name)) as fp:
                dataSet =[]
                for line in fp:
                        line = line.strip('\n')
                        features= (line.split(','))
                        features = [ float(x) for x in features ]
                        dataSet.append(features)

        tw_train_base = np.array(dataSet)
        return tw_train_base

def load_tw_train_base_recent(dir,t,o,l):
        name = 'tw_train_base_recent_'+str(t)+str(o)+str(l)+'.txt'
        with open(os.path.join(dir,name)) as fp:
                dataSet =[]
                for line in fp:
                        line = line.strip('\n')
                        features= (line.split(','))
                        features = [ float(x) for x in features ]
                        dataSet.append(features)

        tw_train_base_recent = np.array(dataSet)
        return tw_train_base_recent
        

def load_yt_train_all(dir,t,o,l):
        name = 'yt_train_all_'+str(t)+str(o)+str(l)+'.txt'
        with open(os.path.join(dir,name)) as fp:
                dataSet =[]
                for line in fp:
                        line = line.strip('\n')
                        features= (line.split(','))
                        features = [ float(x) for x in features ]
                        dataSet.append(features)

        yt_train_all = np.array(dataSet)
        return yt_train_all

def load_yt_train_all_recent(dir,t,o,l):
        name = 'yt_train_all_recent_'+str(t)+str(o)+str(l)+'.txt'
        with open(os.path.join(dir,name)) as fp:
                dataSet =[]
                for line in fp:
                        line = line.strip('\n')
                        features= (line.split(','))
                        features = [ float(x) for x in features ]
                        dataSet.append(features)

        yt_train_all_recent = np.array(dataSet)
        return yt_train_all_recent

def load_yt_train_base(dir,t,o,l):
        name = 'yt_train_base_'+str(t)+str(o)+str(l)+'.txt'
        with open(os.path.join(dir,name)) as fp:
                dataSet =[]
                for line in fp:
                        line = line.strip('\n')
                        features= (line.split(','))
                        features = [ float(x) for x in features ]
                        dataSet.append(features)

        yt_train_base = np.array(dataSet)
        return yt_train_base

def load_yt_train_base_recent(dir,t,o,l):
        name = 'yt_train_base_recent_'+str(t)+str(o)+str(l)+'.txt'
        with open(os.path.join(dir,name)) as fp:
                dataSet =[]
                for line in fp:
                        line = line.strip('\n')
                        features= (line.split(','))
                        features = [ float(x) for x in features ]
                        dataSet.append(features)

        yt_train_base_recent = np.array(dataSet)
        return yt_train_base_recent

def load_labeling(dir,t,o,l):
        name = 'labeling_'+str(t)+str(o)+str(l)+'.txt'
        with open(os.path.join(dir,name)) as fp:
                labeled =[]
                for line in fp:
                        line = line.strip('\n')
                        line = line.strip('[')
                        line = line.strip(']')
                        labels= (line.split(','))
                        labels = [ int(x) for x in labels ]
                        labeled.append(labels)
        return labeled

def load_labeling_recent(dir,t,o,l):
        name = 'labeling_recent_'+str(t)+str(o)+str(l)+'.txt'
        with open(os.path.join(dir,name)) as fp:
                labeled =[]
                for line in fp:
                        line = line.strip('\n')
                        line = line.strip('[')
                        line = line.strip(']')
                        labels= (line.split(','))
                        labels = [ int(x) for x in labels ]
                        labeled.append(labels)
        return labeled
        
