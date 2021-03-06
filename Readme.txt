懶人投資包-專為投資白癡設計的交易策略

「投資是一門簡單的事情，但做得好往往很少」—Warren Buffett 
市場上充滿著有訊息的法人，有經驗的老手，以及貢獻金錢的散戶。身處在財管所的我們都知道
想得到交易的聖杯，並不是簡單的事，微結構、技術指標、基本分析、投資組合等等的知識，對於
非本科系的大眾來說，是一種曲高和寡的思考。但缺乏這些知識，就代表他們不能在市場上獲利嗎?
我們認為不是的，只要我們做好策略、限定好可投資股票，就算是投資白癡，只要會下單，也能從市
場上得到應有的報酬。

有感於身旁親朋好友，想投資，無法充分了解金融知識，只想知道買哪支股票，什麼時候買，所以我們
量身訂做此套演算法交易策略。

本套服務分為兩個部分


1.風險評估表-

 (1)透過問卷調查評估使用者的風險偏好以及承受能力：

	年齡 
	(1)69歲以上/20歲以下 (2)66-68歲 (3)56-65歲 (4)41-55歲 (5)20-40歲
	請輸入您的答案
	您選擇  

	金融理財知識：您對金融市場和投資的認識？
	(1) 我對金融市場一無所知，但有興趣進一步瞭解。
	(2) 我對金融市場只有一些基本知識，例如股票與基金的分別。
	(3) 我瞭解基本知識，並明白分散投資及資產配置的重要性，並作出分散投資。
	(4) 我對金融商品及其投資風險有進一步的認識，並明白影響股票和債券價格的因素。
	(5) 我非常熟悉大部份金融產品(包括債券、股票、認股權證、期權及期貨)，並明白影響這些金融產品的風險和表 現的各項因素。
	請輸入您的答案
	您選擇  

	金融投資商品的投資經驗, 包括期貨、股票、債券、基金、投資型保單、衍生性投資工具...等
	(1) 1 年（含）以下 (2) 1 年- 3 年（含） (3) 3 年- 6 年（含） (4) 6 年- 10 年（含） (5) 10 年以上
	請輸入您的答案
	您選擇  

	可承受的波動程度：一般而言，您可接受何種程度的價格波動？
	(1) 無法接受波動 (2) 可接受最高 5% 的波動 (3) 可接受最高 15% 的波動 (4) 可接受最高 30% 的波動 (5) 可接受 30% 以上的波動
	請輸入您的答案
	您選擇  

	投資年間：一般而言，當您投資的金融商品有波動時，您可接受的持有期間？
	(1) 3 個月以下 (2) 3 個月- 6 個月（含） (3) 6 個月- 1 年（含） (4) 1 年- 3 年（含） (5) 3 年以上
	請輸入您的答案
	您選擇  

	財務狀況：在一般情況下，您的家庭月收入約有多少比例可以用於投資或儲蓄？
	(1) 無 (2) 介於 0% - 10%（含） (3) 介於 10% - 30%（含）(4) 介於 30% - 60%（含） (5) 60% 以上
	請輸入您的答案
	您選擇  

	資產配置：目前投資的資產中（不包括自用房地產），約有多少比例是持有金融投資商品？
	(1) 無 (2) > 0% - 10% (3) > 10% - 25% (4) > 25% - 50% (5) > 50%
	請輸入您的答案
	您選擇  

	金融投資商品的交易頻率？
	(1) 一年以上 (2) 半年 (3) 每季 (4) 每月 (5) 每週
	請輸入您的答案
	您選擇  

	投資目標：下列哪一項最能描述您的投資目標？
	(1) 首要目標是能維持本金，即使投資回報率可能非常低。
	(2) 追求穩定的定期收益，例如股息或是債券配息，即使存在資本虧損的風險。
	(3) 在穩定的資本成長與定期收益之間追求平衡的投資回報率。
	(4) 願意承擔較高的風險，追求資本增值，以累積資金。
	(5) 願意承擔更高的風險，以儘量提高資本增值。
	請輸入您的答案
	您選擇  

	若非預期的事件發生時，請問您的備用金相當於您幾個月的家庭開銷？
	(1) 無備用金儲蓄* (2) 3 個月以下 (3) 介於 3 個月到 6 個月 (4) 介於 6 個月到 9 個月 (5) 超過 9 個月 
	請輸入您的答案
	您選擇
  
 (2)根據分數的加總，給定適合的交易策略，並指出可交易標的
	
	總分<15→保守型（KD指標）
	15<總分<30→穩健型（MACD指標）
	30<總分→積極型（BBands指標）



2.交易策略-

 KD指標:
	KD指標是使用RSV的加權移動平均來計算的，RSV數據表達的是「與最近9天相比，今天的股價是強還是弱?」。
	而KD數值越高代表個股的收盤價接近最近幾天的最高價，反之KD數值越低代表個股的收盤價接近最近幾天的最低價。

	RSV計算方式：
		(今日收盤價 - 最近九天的最低價)/(最近九天的最高價 - 最近九天最低價)

	K值計算方式：
		 (RSV 和前一日的 K的加權平均K = 2/3 X (昨日K值) + 1/3 X (今日RSV))

	D值計算方式：
 		(K和前一日的 D 的加權平均K = 2/3 X (昨日D值) + 1/3 X (今日K值))

	買賣時機：
		當K>D且D>40，買進該個股;當K<D且D<60，則賣出該個股。

 MACD指標:
	MACD指標由一組曲線與圖形組成，通過收盤時股價或指數的快變及慢變的指數移動平均值（EMA）之間的差計算出來。
	「快」指更短時段的EMA，而「慢」則指較長時段的EMA，最常用的是12及26日EMA。

	DIF計算方式：
		(DIF=EMA12-EMA26)

	DEM計算方式：
		(DEM=DIF9)

	買賣時機：
		當DIF>DEM買進該個股;當DIF<DEM，則賣出該個股。

 BBand指標:
	BBand又稱布林線。此通道由三條線組成，它是由一條表示股價趨勢方向的中軌線，再加上上下兩條軌道線所組成，
	形成所謂通道或所謂帶狀，是一種應用於波段操作時的技術指標。

	UBB:
		(MA20+SMA20)

	MBB:
		(MA20)

	LBB:
		(MA20-SMA20)

	買賣時機：
		收盤價由下往上穿過LBB時，買進;收盤價由上往下穿過UBB時，賣出。

3.交易回測-
	
	交易資料表：
		利用策略回測，測試從2015/01/01~2018/1/10每支個股的進出場資訊，並將不同股票的進出場資料表透過pd.concat(trade_table.values())彙整。
		根據日期排序，避免回測過程中，出現偏誤。
		整理表格，僅留下[Buy_Date、buyPrice、Volume、symbol、signals、Sell_Date、sellPrice、Volume、symbol、signals、positions]

	基金化回測：
		設定資金部位1,000,000，最大持有股票檔數為3檔，根據進出場資料表時間，依序買進與賣出。
		結果得出該策略的淨值變化、現金變化、MDD、累積報酬率。
