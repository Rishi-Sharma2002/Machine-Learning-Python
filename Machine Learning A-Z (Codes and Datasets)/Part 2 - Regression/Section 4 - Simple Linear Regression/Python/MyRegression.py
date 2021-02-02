# #Inmporting the dataset and the required libraries
# from sklearn import datasets
#
# boston = datasets.load_boston(return_X_y=False)
# x = boston.data
# y = boston.target
#
# #Spilitting the dataset in the Training and Test Stage
# from sklearn.model_selection import train_test_split
# x_train, x_test, y_train, y_test = train_test_split(x, y, train_size=0.8, random_state=1)
#
# # Performing the regression
# from sklearn.linear_model import LinearRegression
# regressor = LinearRegression()
# regressor.fit(x_train, y_train)
#
# y_pred = regressor.predict(x_train)
# print(f"Variance score is: {regressor.score(x_train, y_train)}")
# #Making the graph
# # Training Set
# import matplotlib.pyplot as plt
# plt.scatter(regressor.predict(x_train), regressor.predict(x_train)-y_train, color = 'green')
# plt.scatter(regressor.predict(x_test), regressor.predict(x_test)-y_test, color='red')
# plt.hlines(y = 0, xmin = 0, xmax = 50, linewidth = 2)
# plt.legend(loc = 'upper right')
# #plt.plot(x_train, regressor.fit(x_train), color = 'blue')
# plt.title('Training Set')
# plt.show()


