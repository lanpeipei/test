from django.http import HttpResponse

import json
from pymongo import MongoClient
import pymongo




def hello(request):
    mc = MongoClient("localhost", 27017)
    db = mc.textlive
    c=db.textlive.find()
    jsons=[]
    j=0
    for i in c:
        res={}
        res['comm']=i['comm']
        res['liveId']=i['liveId']
        res['o_no']=i['o_no']

        # print i
        jsons.append(res)

    rjson=json.dumps(jsons)
    print rjson
    return HttpResponse(rjson)

def current(request):
    id = request.GET.get('liveid')
    mc = MongoClient("localhost", 27017)
    db = mc.textlive
    c = db.textlive.find({"liveId":id}).sort("timestamp",pymongo.DESCENDING).limit(1)
    jsons = []
    j = 0
    for i in c:
        res = {}
        res['comm'] = i['comm']
        res['liveId'] = i['liveId']
        res['o_no'] = i['o_no']
        # print i
        jsons.append(res)
    re =json.dumps(jsons[0])

    return HttpResponse(re, content_type="application/json")


def currentLives(request):
    mc = MongoClient("localhost", 27017)
    db = mc.textlive
    jsons = []
    id = request.GET.get('liveid')
    _time=request.GET.get('timestamp')
    _mode=request.GET.get('mode')
    if _time:
        cur_comm=db.textlive.find_one({"ids":_time+id})
        # print cur_comm
        cur_bno=cur_comm['b_no']
        cur_iid=cur_comm['i_id']
        # print cur_iid
        print _mode
        if _mode=='prev':
            print 1
            c=db.textlive.find({'liveId':id,'i_id':cur_iid,'b_no':{'$lt':cur_bno,'$gte':cur_bno-10}}).sort('timestamp',pymongo.DESCENDING)
            for o in c:
                res = {}
                res['comm'] = o['comm']
                res['liveId'] = o['liveId']
                res['o_no'] = o['o_no']
                res['timestamp'] =o['timestamp']
                res['b_no'] = o['b_no']
                res['i_id'] = o['i_id']
                jsons.append(res)
            re=json.dumps(jsons)
            print re
            return HttpResponse(re, content_type="application/json")
        # return HttpResponse(json.dumps({_o_no:_mode}),content_type="application/json")
    else:
        print 0

    c = db.textlive.find({"liveId":id}).sort("timestamp",pymongo.DESCENDING).limit(10)


    for i in c:
        res = {}
        res['comm']   = i['comm']
        res['liveId'] = i['liveId']
        res['o_no']   = i['o_no']
        res['timestamp']=i['timestamp']
        res['b_no']   =i['b_no']
        res['i_id']   = i['i_id']
        # print i
        jsons.append(res)
    re =json.dumps(jsons)
    return HttpResponse(re,content_type="application/json")

def hello1(request,str):
    return HttpResponse(str)
