BBox-Label-Tool
===============

画像のバウンディングボックスのラベリングツール。    

**Screenshot:**
![Label Tool](./screenshot.png)

ファイル構成    
-----------------
LabelTool  
|  
|--main.py   *# source code for the tool*  
|  
|--Images/   *# direcotry containing the images to be labeled*  
|  
|--Labels/   *# direcotry for the labeling results*  
|  
|--Examples/  *# direcotry for the example bboxes*  

環境    
----------
- python 2.7
- python PIL (Pillow)


```
pip install pillow
```

実行    
-------
$ python main.py

Usage
-----
/Images/001 配下に画像を /Labels/001 とパス配下にラベルを管理。
読み込みボタンを押下。
次へボタンと前へボタン押下でラベル情報を保存。


