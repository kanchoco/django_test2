from django.http import HttpResponse
from django.shortcuts import render

# from django.http import FileResponse
# import cv2

# camera = cv2.VideoCapture(0, cv2.CAP_MSMF)
# camera.set(cv2.CAP_PROP_BUFFERSIZE, 3)  # Increase buffer size


def index(request):
    return HttpResponse("<h1>Hello world!</h1>")


def myfirst(request):
    return render(request, "myfirst.html")


def fileupload(request):
    return render(request, "fileupload.html")


def classification(request):
    return render(request, "classification.html")


# def generate_frames():
#     while True:
#         success, frame = camera.read()  # 카메라로부터 프레임 읽기
#         if not success:
#             break
#         else:
#             # 이미지를 JPEG 형식으로 인코딩
#             _, buffer = cv2.imencode(".jpg", frame)
#             frame = buffer.tobytes()

#             # HTTP 응답 형식으로 프레임 전달
#             yield (b"--frame\r\n" b"Content-Type: image/jpeg\r\n\r\n" + frame + b"\r\n")


# def video_feed():
#     return FileResponse(generate_frames(), content_type="video/webm")

# from .forms import ReadFileForm


# def read_file(request):
#     form = ReadFileForm()
#     if request.method == 'POST':
#         form = ReadFileForm(request.POST, request.FILES)
#         if form.is_valid():
#             content = request.FILES['file'].read()
#             # Do something with content
#     return render(request, 'read_file.html', locals())
