# fju-information-test
輔大畢業資訊能力測驗的自動出題系統

## 介紹
基本上為一個簡單的CLI小程式，它會讀取同資料夾底下的exam.xlsx，接著提示使用者輸入想要的難易度與題數，隨機抽選題目出來給使用者。

## 檔案說明
1. main.py
  為主要的程式檔，引用了[pyexcel](https://github.com/pyexcel/pyexcel) ，需自行安裝
2. exam.xlsx
  題庫檔，從 **輔仁大學資訊基本能力評量試題201404.pdf** 轉出為xlsx的。
  
## 已知問題
1. 無法顯示圖片
  可能未來需要寫個GUI才會比較方便吧
