import numpy as np

#--------transpose matrix & vector ------------------
#creare vector

vector = np.array([11,22,33,44,55,66])

#create matrix

matrix = np.array([[2,4,6],
                  [8,10,12],
                  [14,16,18],
                   ])
#transpose matrix
print(matrix.T)

#------------------------------------------------------

#=============>>reshape array<<<=======================

matrix2 = np.array([[2,4,6],
                  [8,10,12],
                  [14,16,18],
                   [20,22,24],
                    [26,28,30],
                    [32,34,36],
                    ])

#reshape matrix into matrix
print(matrix2.reshape(2,9))

#=======================================================
#----------- invert a matrix----------------------------
matrix3 = np.array([[4,3,4],
                    [5,6,5],
                    [6,6,5]
                    ])
print(np.linalg.inv(matrix3))

#---------