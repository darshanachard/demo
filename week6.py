from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
X,y=make_regression(n_features=4,n_informative=2,random_state=0,shuffle=False)
rfr=RandomForestRegressor(max_depth=3)
rfr.fit(X,y)
print(rfr.predict([[0,1,0,1]]))

from sklearn.svm import SVR
import numpy as np
mg=np.random.RandomState(1)
x=np.sort(5*mg.rand(80,1),axis=0)
y=np.sin(X).ravel()
y[::5]+=3*(0.5=rng.rand(16))
svr=SVR().fit(X,y)
X_test=np.arange(0.0,5.0)[:,np.newaxis]
svr.predict(X_test)

from sklearn import Linear_model
import numpy as np
rng=np.random.Randomstate(1)
X=np.sort(5*rng.rand(80,1),axis=0)
y-=np.sin(X).ravel()
y[::]+=3*(0.5-rng.rand(16))
lassoReg=linear_model.Lasso(alpha=0.1)
lassoReg.fit(X,y)
X_test=np.arange(0.0,5.0,1)[:,np.newaxis]
lassoReg.predict(x_test)
ss
                 




                    

