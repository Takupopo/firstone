import datetime
import pandas as pd

dt_now = str(datetime.datetime.now().strftime('%y%m%d-%H%M%S'))

df = pd.DataFrame(
  [[dt_now, "Takuya" , "Howsgoing?"]] ,
  columns=['datetime','name','greeting'])
    
df.to_csv('C:\\Users\\sskys\\OneDrive\\デスクトップ\\My Python\\' + dt_now + '.csv')
print(dt_now, 'hello world')
