# 用於3D建模的自動拍攝平台
![image](https://github.com/s107321509/Automatic-shooting-platform-for-3D-modeling/blob/master/img/%E4%BA%8C%E8%BB%B8%E5%B9%B3%E5%8F%B0.png)
## 目錄

- [背景](#背景)
- [安裝](#安裝)
- [用法](#用法)


## 背景

`3D modeling platform3D`平台用於旋轉樣本，以從樣本的不同角度捕獲圖像，以完成3D建模所需的先前工作。但是，儘管市場上有許多現成的3D掃描儀可供公眾購買，但它們價格昂貴，且花費數万元。我們的二維平台由3D打印組件和步進電機組成，其成本相對較低。而且容易獲得。

該github提供了控制平台的代碼。


使用此程序之前，您必須準備以下幾件事：

1. 樹莓派  
![image](https://github.com/s107321509/Automatic-shooting-platform-for-3D-modeling/blob/master/img/rpi.png)
2. 3個步進電機  
![image](https://github.com/s107321509/Automatic-shooting-platform-for-3D-modeling/blob/master/img/motor.png)
3. 相機  
![image](https://github.com/s107321509/Automatic-shooting-platform-for-3D-modeling/blob/master/img/camera.png)
4. 馬達驅動  
![image](https://github.com/s107321509/Automatic-shooting-platform-for-3D-modeling/blob/master/img/%E9%A6%AC%E9%81%94%E9%A9%85%E5%8B%95.png)
5. 從[Openscan](https://www.thingiverse.com/thing:3050437)下載平台架構模型，然後使用3D打印將其打印出來  

## 安裝

該項目使用gphoto2來控制相機拍照。使用前請確保已安裝此軟件。

```sh
$ sudo apt-get install gphoto2
```
使用前請確保安裝python2.7。

```sh
$ sudo apt-get install python2.7
```

##  用法

標本的拍攝過程大致可分為以下步驟：

1.用戶可以在中定義任意數量的傾斜角度和水平旋轉的步數tilting.py，如下所示，定義為水平轉盤每轉拍攝40個環繞圖像，並且傾斜軸每次移動300微步，從不同角度分為三個拍攝。

```sh
panning_step = [40,40,40]
tilting_step = [300,300,300]
```
2.`start.py` 用於控制堆疊平台的移動，以找到對象前後焦點的清晰範圍。使用讀取鍵盤琴鍵的方法將w定義為前進，將s定義為後退，使用a和d定義拍攝的開始和結束位置，最後按q鍵完成參數設置。

3.在水平轉盤的每個步驟之後，將調用堆疊程序。在堆疊的每個步驟之後，執行相機程序以自動控制相機拍攝樣本。

4.重複步驟（3），直到水平轉盤完成一圈。

5.將傾斜軸移至下一個角度，然後重複步驟（3）（4），直至獲得所有傾斜角。

6.拍攝完成後，三軸平台返回初始位置。
