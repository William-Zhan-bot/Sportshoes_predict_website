import os
import sys
import joblib
import pandas as pd
import json


temp=str(sys.argv[0])
brand=str(sys.argv[1])
size=str(sys.argv[2])
gender=str(sys.argv[3])
type=str(sys.argv[4])
color=str(sys.argv[5])
material=str(sys.argv[6])
# 參數
data=list(sys.argv[1:])

# MODEL
regtree=os.getcwd()+"/web/backend/decision_tree_model.pkl"
model=joblib.load(regtree)

# feature list
f_lst=['Brand','Size', 'Gender', 'Type', 'Color', 'Material']

def pred(data):
    if len(data) != 6:
        return 'error!'

    # 建立全為false空表單
    col=["Brand_Adidas","Brand_Asics","Brand_Converse","Brand_Fila",
     "Brand_New Balance","Brand_Nike","Brand_Puma","Brand_Reebok",
     "Brand_Skechers","Brand_Vans","Type_Basketball","Type_Casual",
     "Type_Cross-training","Type_CrossFit","Type_Crossfit","Type_Fashion",
     "Type_Hiking","Type_Lifestyle","Type_Racing","Type_Retro","Type_Running",
     "Type_Skate","Type_Slides","Type_Trail","Type_Trail Running",
     "Type_Training","Type_Walking","Type_Weightlifting","Gender_Men",
     "Gender_Women","Size_US 10","Size_US 10.5","Size_US 11","Size_US 11.5",
     "Size_US 12","Size_US 6","Size_US 6.5","Size_US 7","Size_US 7.5",
     "Size_US 8","Size_US 8.5","Size_US 9","Size_US 9.5","Color_Beige",
     "Color_Black","Color_Black/Blue","Color_Black/Gold","Color_Black/Gold/Red",
     "Color_Black/Green","Color_Black/Grey","Color_Black/Gum","Color_Black/Pink",
     "Color_Black/Red","Color_Black/White","Color_Black/White Checkerboard",
     "Color_Black/Yellow","Color_Blue","Color_Blue/Black","Color_Blue/Green",
     "Color_Blue/Orange","Color_Blue/Pink","Color_Blue/Red","Color_Blue/White",
     "Color_Blue/Yellow","Color_Brown","Color_Burgundy","Color_Charcoal",
     "Color_Checkerboard","Color_Checkerboard Black/White","Color_Checkered",
     "Color_Cinder","Color_Clay Brown","Color_Cloud White","Color_Collegiate Navy",
     "Color_Cream","Color_Cream White","Color_Egret","Color_Egret/Black",
     "Color_Green","Color_Green/Black","Color_Green/Orange","Color_Green/White",
     "Color_Grey","Color_Grey/Black","Color_Grey/Green","Color_Grey/Orange",
     "Color_Grey/Pink","Color_Grey/Purple","Color_Grey/White","Color_Grey/Yellow",
     "Color_Ivory","Color_Khaki","Color_Multi-color","Color_Natural",
     "Color_Natural Ivory","Color_Navy","Color_Navy/Red","Color_Navy/White",
     "Color_Orange","Color_Pink","Color_Pink/Black","Color_Pink/White","Color_Purple",
     "Color_Red","Color_Red/Black","Color_Red/White","Color_Silver","Color_Silver/White",
     "Color_Sunflower","Color_True White","Color_White","Color_White/Black",
     "Color_White/Blue","Color_White/Gold","Color_White/Green","Color_White/Grey",
     "Color_White/Navy","Color_White/Navy/Red","Color_White/Pink","Color_White/Red",
     "Color_White/Red/Blue","Color_White/Red/Navy","Color_Yellow","Color_Yellow/Black",
     "Color_Zebra","Material_Canvas","Material_Canvas/Leather","Material_Canvas/Suede",
     "Material_Flexweave","Material_Flexweave/Cushioning","Material_Flexweave/Knit",
     "Material_Flexweave/Synthetic","Material_Flyknit","Material_Knit",
     "Material_Knit/Synthetic","Material_Leather","Material_Leather/Mesh",
     "Material_Leather/Suede","Material_Leather/Synthetic","Material_Mesh",
     "Material_Mesh/Leather","Material_Mesh/Suede","Material_Mesh/Synthetic",
     "Material_Nylon","Material_Nylon/Suede","Material_Primeknit",
     "Material_Primeknit/Synthetic","Material_Suede","Material_Suede/Canvas",
     "Material_Suede/Leather","Material_Suede/Mesh","Material_Suede/Nylon",
     "Material_Suede/Textile","Material_Synthetic","Material_Synthetic/Leather",
     "Material_Synthetic/Mesh","Material_Synthetic/Textile","Material_Textile",
     "Material_Textile/Leather"]
    false_df=pd.DataFrame(columns=col)
    false_df.loc[0]=[False] * len(col)
    # 轉換資料一樣的填入
    for i in range(len(data)):
        col=f_lst[i]+"_"+data[i]
        false_df[col]=True
    # 預測資料
    result=model.predict(false_df)
    return result

result=str(pred(data))
result=json.dumps(result)
print(result)