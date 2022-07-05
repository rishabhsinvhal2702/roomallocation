import string
from django.http import JsonResponse
from django.shortcuts import render, redirect
from .models import Room
from accounts.models import Account
from django.contrib.auth.decorators import login_required

@login_required(login_url="/login/")
def block_list(request):
    return render(request, 'rooms/block_list.html')

@login_required(login_url="/login/")
def block_rooms(request, block, floor):
    if request.is_ajax and request.method == 'POST':
        roomno = request.POST.get('room_no')
        request.user.is_alloted = True
        request.user.room_no = roomno
        request.user.save()
        updated_room = Room.objects.filter(room_no=roomno)[0]
        if updated_room.is_alloted == False:
            updated_room.is_alloted = True
            updated_room.rollno = request.user.rollno
            updated_room.name = request.user.first_name
            updated_room.save()
    b_room = Room.objects.filter(block=block, floor=floor)
    data = {
        "b_room": b_room,
        "rusers": {
            "roll": request.user.rollno,
            "first_name": request.user.first_name,
            "user_room": request.user.room_no,
            "allot": request.user.is_alloted,
            "block": block,
            "floor":floor
        }
    }
    return render(request, 'rooms/blockwise_rooms.html', data)