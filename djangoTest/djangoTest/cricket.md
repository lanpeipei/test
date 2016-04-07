
# 板球直播API文档


## 1.1 获取板球比赛列表

* url : http://api.newsdog.today/v1/cricket/matches
* 请求方式: GET
* 返回格式参考 : http://www.cricbuzz.com/api/match/current


## 1.2 获取Live比赛的最新状态

* url : http://api.newsdog.today/v1/cricket/live/?liveid=比赛的id
* 请求方式: GET
* 返回结果 :

```
{
   "o_no":"19.3",
   "comm":"这里是最新的评论"
}
```


##首次获取直播板球比赛的批量状态

* url : http://api.newsdog.today/v1/cricket/lives/?liveid=比赛的id
* 请求方式: GET
* 返回结果

```

{

[
	{
		"liveId": "15804",
		"comm": "Badree to Jason Roy",
		"o_no": "0.1"
        “timestamp”：“时间”
        'b_no':"数字"
        'i_id':'比赛局数'
	},
	{
		"liveId": "15804",
		"comm": "Stokes to Brathwaite, SIX, Brathwaite! ",
		"o_no": "0.2"
	}
]
}
```
## 获取直播板球比赛的批量状态

* url : http://api.newsdog.today/v1/cricket/lives/comment/?liveid=比赛的id&timestamp=已经获取到的timestamp号码&mode=`prev|next`
* 请求方式: GET
* 返回结果

```
{

[
	{
		"liveId": "15804",
		"comm": "Badree to Jason Roy",
		"o_no": "0.1"
        “timestamp”：“时间”
        'b_no':"数字"
        'i_id':'比赛局数'
	}, 
	{
		"liveId": "15804", 
		"comm": "Stokes to Brathwaite, SIX, Brathwaite! ",
		"o_no": "0.2"
	}
]
}
```

上述mode参数中prev表示获取更早的评论,next表示获取更新的评论
