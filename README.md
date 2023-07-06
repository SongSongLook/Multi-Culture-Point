# Multi-Culture-Point
台灣文化部文化幣應用程式多開、避免一部iOS裝置需多個帳號結帳時登入登出之麻煩。   
(無需jailbreak，限iOS 13.0以上版本適用)   
使用範例:   
<img src="https://img.onl/Orok5R" width="25%">
## 所需app數量、版本設置  
1. 下載已砸殼ipa```DecryptedCP.ipa``` -> (https://mega.nz/file/DIl2mLyQ#ADGmpVFjhnqEoBhELtRdqDfAGSTrbNXcGTHeJBqxjj4)
2. 可用附設python檔案確認自身裝置```Model Identifiers```  
(目前原始檔案預設僅支持iPhone 8, iPhone 7,and iPhone 11 Pro Max若是以上型號可跳過步驟3)
3. 以BBedit等文本編輯器開啟ipa檔案尋找 ```info.plist``` 內展開 ```UISupportedDevices``` 如以下所示   
 於```<array>```內新增個人裝置 Model Identifiers後儲存 (格式```<string>iPhonexx,x</string>```)  
 ```
<key>UISupportedDevices</key>
	<array>
		<string>iPhone10,1</string>
		<string>iPhone10,4</string>
		<string>iPhone12,5</string>
		<string>iPhone9,1</string>
		<string>iPhone9,3</string>
```

##  ipa簽名及安裝   
1. 利用現成macOS各類助手利用Apple ID進行重簽名(此處舉例愛思助手 -> (https://www.i4.cn))    
   (Apple ID簽名ipa每七天過期需重新簽名，一部裝置最多可安裝三個自行簽名ipa檔案)   
   1(a). 連接設備 -> 上方選單點擊工具箱 -> 點擊頁尾ipa簽名 -> 點擊左上添加ipa文件 -> 點擊下方使用Apple ID簽名 -> 開始簽名
2. 安裝ipa檔案至行動裝置(可用Cydia Impactor等，此處舉例iMazing -> (https://imazing.com))   
   2(a). 連接設備 -> 點擊中間右頁選單內Manage Apps -> 點擊右下方下三角形 -> 選擇Install .IPA File安裝   
3. 至iOS設定內裝置管理點擊信任開發人員後即可正常使用  
---
*補充
1. 在```info.plist```內```<key>CFBundleDisplayName</key>```內可更改app名稱以利辨認
   ```
   <key>CFBundleDisplayName</key>
	<string>文化幣</string>
   ```
2. 若需安裝兩個以上app可重複簽名已簽名檔案覆寫```CFBundleIdentifier```
