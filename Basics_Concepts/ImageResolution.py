from skimage import io
import pandas as pd

img=io.imread('cat.jpg')
print(img.shape)
df=pd.DataFrame(img.flatten())
name='pixel.xlsx'
df.to_excel(name)
print(df)