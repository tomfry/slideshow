from django.http import HttpResponse, HttpRequest
from django.template import loader, Context, RequestContext
from django.shortcuts import render, render_to_response
import os
from PIL import Image as PImage

def index(request):
    return render_to_response("index.html")


def photos(request):
    photodir = (os.path.join(os.path.dirname(__file__), '..', 'photos').replace('\\','/'),)

    filelist = createFileList(photodir[0])
    testlist = [ "test", "new" ]
    d = dict (testlist=testlist, filelist=filelist, user=request.user)
    return render_to_response(	"photo_album_list.html", d)


def renderThumbnail(request, album, image):
    try:
        if not image.endswith('.jpg'):
            image = str(image)+".jpg"
        print image

        imagefile = os.path.join(os.path.dirname(__file__),  '..', 'photos', album, image)

        print imagefile
        im = PImage.open(imagefile)

        im.thumbnail((300,100), PImage.ANTIALIAS)

        response = HttpResponse(mimetype="image/png")
        im.save(response, "PNG")
        return response
    except :
        return HttpResponse(status=404)

def album(request, album):
    #return HttpResponse("You're looking at album %s." % album)
    albumDirectory = os.path.join(os.path.dirname(__file__), '..', 'photos', album)

    photoList = createFileList(albumDirectory)

    d = dict (album=album, photoList = photoList)

    return render_to_response("photo_viewer.html", d)

def createFileList(directory):

    #photodir = (os.path.join(os.path.dirname(__file__),  '..', 'photos').replace('\\','/'),)
    print directory

    dirList = []
    #for file in os.listdir('/home/djangouser/swallowsbottom/photos'):
    for file in os.listdir(directory):
        print file
        #if os.path.isdir(os.path.join(photodir[0], file)):
        if not file.startswith('.'):
            dirList.append(file)
    return dirList