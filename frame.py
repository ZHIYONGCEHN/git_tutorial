import numpy as np
import pandas as pd

cols = ['A', 'B']
df = pd.DataFrame(np.random.randn(20, 2), columns = cols)

df_stat = df.describe()

if __name__ == "__main__":
    print(df_stat)
    
    
