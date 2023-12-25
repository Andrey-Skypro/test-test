def bank(X, Y):
 for year in range(Y):
  X = X * 1.10 
 return X
result = bank(1000, 5)
print(result)