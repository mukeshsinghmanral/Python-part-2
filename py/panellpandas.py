import pandas as pd
import numpy as np
s = pd.Series(np.random.randn(4))
print(s)
print("The axes are:")
print(s.axes)