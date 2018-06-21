import json

from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response

from django.http import HttpResponse

@api_view(('GET',))
def api_root(request, format=None):
    """
    This is the entry point for the API described in the
    Follow the hyperinks each resource offers to explore the API.
    Note that you can also explore the API from the command line,
      for instance using the `curl` command-line tool.
    For example: `curl -X GET http://restframework.herokuapp.com/
    -H "Accept: application/json; indent=4"`
    """
    return Response({
        'themes': reverse('theme-api-list', request=request, format=format),
})

#http://www.xlauncher.cn/business/getrecommand?xd=12333&la=cn
#http://www.xlauncher.cn/business/getrecommand?xd=862374037967029&la=cn
'''
            {
                "packageName":"com.one.click.ido.screenshot", 
                "Name" : "One ClickScreenshot", 
                "downloadUrl" : "https://play.google.com/store/apps/details?id=com.one.click.ido.screenshot", 
                "icon_url": "http://www.xlauncher.cn/media/business/screenshot.png",
                "description": "According to statistics,taking screenshot by notification bar or floating bubble can greatly enhance the life of the power button. Screenshot almost cover every kinds of Android phone and don't need to  root your phone. Picture editing function is easy to use, let you easily deal with picture editing."

            }
'''

def getrecommand(request):
    xd = request.GET.get('xd', '')
    if xd == "864413034260570" or xd == "862374037967029" or xd == "865736032296280x" :
        obj2 = {"recommand-list" : 
        [
            {
                "packageName":"com.erciyuan.clock", 
                "Name" : "Alarm", 
                "downloadUrl" : "https://play.google.com/store/apps/details?id=com.erciyuan.clock", 
                "icon_url": "http://www.xlauncher.cn/media/business/alarm.png",
                "description":"Anime and minimalist design is the most important feature of the One AlarmClock, so that anime lovers cannot put it down. Stick to the anime style at the same time, but also contains the practicality of the function,such as alarm clocks, world clocks, stopwatches and timer."
            }, 
            {
                "packageName":"com.one.click.ido.screenshot", 
                "Name" : "Screenshot", 
                "downloadUrl" : "https://play.google.com/store/apps/details?id=com.one.click.ido.screenshot", 
                "icon_url": "http://www.xlauncher.cn/media/business/screenshot.png",
                "description": "According to statistics,taking screenshot by notification bar or floating bubble can greatly enhance the life of the power button. Screenshot almost cover every kinds of Android phone and don't need to  root your phone. Picture editing function is easy to use, let you easily deal with picture editing."

            }, 
            {
                "packageName":"com.quna.compass", 
                "Name" : "compass", 
                "downloadUrl" : "https://play.google.com/store/apps/details?id=com.quna.compass", 
                "icon_url": "http://www.xlauncher.cn/media/business/one_compass.jpg",
                "description": "One Compass is a travel essential device, so you can find direction quickly with this App.One second to identify the direction."

            }, 
            {
                "packageName":"com.iboxltt.flashlight", 
                "Name" : "flashlight", 
                "downloadUrl" : "https://play.google.com/store/apps/details?id=com.iboxltt.flashlight", 
                "icon_url": "http://www.xlauncher.cn/media/business/one_flashlight.jpg",
                "description": "Gorgeous UI, will certainly be able to meet the girls critical vision and taste.Completely free, easy to use,power-saving ability,excellent adaptation.Flashlight,SOS light,Night Camera contained in One Flashlight."
            }
        ]
        }
    else :
        obj2 = {"recommand-list" : 
        [
            {
                "packageName":"com.erciyuan.clock", 
                "Name" : "Alarm", 
                "downloadUrl" : "https://play.google.com/store/apps/details?id=com.erciyuan.clock", 
                "icon_url": "http://www.xlauncher.cn/media/business/alarm.png",
                "description":"Anime and minimalist design is the most important feature of the One AlarmClock, so that anime lovers cannot put it down. Stick to the anime style at the same time, but also contains the practicality of the function,such as alarm clocks, world clocks, stopwatches and timer."
            }, 
            {
                "packageName":"com.one.click.ido.screenshot", 
                "Name" : "Screenshot", 
                "downloadUrl" : "https://play.google.com/store/apps/details?id=com.one.click.ido.screenshot", 
                "icon_url": "http://www.xlauncher.cn/media/business/screenshot.png",
                "description": "According to statistics,taking screenshot by notification bar or floating bubble can greatly enhance the life of the power button. Screenshot almost cover every kinds of Android phone and don't need to  root your phone. Picture editing function is easy to use, let you easily deal with picture editing."

            }, 
            {
                "packageName":"com.onetouch.clicklock", 
                "Name" : "Touch", 
                "downloadUrl" : "https://play.google.com/store/apps/details?id=com.onetouch.clicklock", 
                "icon_url": "http://www.xlauncher.cn/media/business/one touch.jpg",
                "description": "You can simply click the icon of One Touch on your desktop and the phone will be locked immediately .this app intend to protect the power button of your phone."

            },
            {
                "packageName":"com.xui.launcher.xtwo", 
                "Name" : "X Theme", 
                "downloadUrl" : "https://play.google.com/store/apps/details?id=com.xui.launcher.xtwo", 
                "icon_url": "http://www.xlauncher.cn/media/business/xtheme_logo.png",
                "description": "New Launcher Theme. clear & clean. "
            }                        
        ]
        }
        
    return HttpResponse(json.dumps(obj2), content_type="application/json")
    