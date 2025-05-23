# option-profit-calculate

應用於台指選擇權組合單的損益試算圖形介面。

## 使用方式

輸入選擇權部位之資訊，即可將其加入列表。

各欄位應填寫內容如下所列。

### 1. 買進/賣出

輸入要加入的選擇權是 **買進部位** 或 **賣出部位**。

可使用 **1 / buy** 表示 **買進**， **0 / -1 / sell** 表示 **賣出**。（大小寫不拘）

### 2. 買權/賣權

輸入要加入的選擇權是 **買權（call）** 或 **賣權（put）**。

可使用 **1 / c / call** 表示 **買權**， **0 / -1 / p / put** 表示 **賣權**。（大小寫不拘）

### 3. 履約價

輸入該選擇權部位的 **履約價**。

因履約價為每 50 點一個合約 [註1]，因此本欄位須輸入 50 的倍數。

### 4. 選擇權價格

輸入該選擇權部位的 **成交價**。

### 5. 口數

輸入該選擇權部位的 **口數**。

若要刪除已輸入的部位，請輸入 **完全相同** 的前四項、口數取相反數（負數），即可完成刪除。除此之外，口數須為正數。

### 按鈕

- **確認輸入**：將所填寫資料加入列表。若資料填寫不符格式，將跳出對話框要求改正。

- **清除填寫**：將填寫欄位中，未加入的內容清除。

- **清除全部**：清除已加入列表，亦清除未加入的內容。

## 程式執行結果

右方圖表將繪出選擇權損益圖。[註2]

**x 軸** 為 **結算價**，**y 軸** 為所列組合單之 **最終損益**。其中，結算價每 **50 點** 會標出一個新的點。

此外，程式會將圖表的每一個轉折點都繪製出來。

## 附註

[註1]：當台指大於 3000 點時，週選擇權的履約價是每 50 點一跳。

月選擇權的履約價是每 100 點一跳，季選擇權的履約價是每 200 點一跳，皆符合 50 的倍數的條件，因此不特別區分。

台指低於 3000 點時，週選擇權的履約價是每 25 點一跳，但本程式不考慮此情況。（台指從破兩萬到跌破 3000 點，那就真的崩啦......）

[註2]：每次 **確認輸入** 且更新成功時，以及 **清除全部** 時，程式會在同一目錄下新增 plot_img.png 檔案。

該檔案可隨時刪除，繪製新損益圖時不會使用到原本的圖片檔。

若未刪除，新損益圖將取代原圖片，因此亦不需擔心沒有用的舊檔案累積的問題。

