from django.http import HttpResponse, HttpRequest
from django.template import loader, Context, RequestContext
from django.shortcuts import render, render_to_response
import os
from PIL import Image as PImage

def index(request):
    return render_to_response("index.html")


def photo_albums(request):
    #This is the view to list the photo albums


    # Get a list of directories (photo albums) in the photo directory
    photoDirectory = os.path.join(os.path.split(os.path.dirname(__file__))[0], 'photos')
    filelist = createFileDirList(photoDirectory)

    #Create a dict and pass to template - uses javascript to create the
    d = dict (filelist=filelist)
    return render_to_response("photo_album_list.html", d)

def renderThumbnail(request, album, image):
    #Creates a thumbnail for each image
    # - To reduce overhead these could be rendered in advance but for small albums it is fine to do it on the fly
    try:
        if not image.endswith('.jpg'):
            image = str(image)+".jpg"

        imagefile = os.path.join(os.path.dirname(__file__),  '..', 'photos', album, image)
        im = PImage.open(imagefile)

        im.thumbnail((300,100), PImage.ANTIALIAS)

        response = HttpResponse(mimetype="image/png")
        im.save(response, "PNG")
        return response
    except:
        return HttpResponse(status=404)

def photo_viewer(request, album):
    #This is the view for the photo viewer - aka the slideshow

    albumDirectory = os.path.join(os.path.dirname(__file__), '..', 'photos', album)
    photoList = createFileDirList(albumDirectory)
    d = dict (album=album, photoList = photoList)
    return render_to_response("photo_viewer.html", d)


def createFileDirList(directory):
    # Simple function to return a list of files of directories within a directory

    dirList = []
    for file in os.listdir(directory):
        if not file.startswith('.'):
            dirList.append(file)
    return dirList