import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer
# Create your views here.

# curl -X POST http://127.0.0.1:8000/chess/queen/ -H ‘Content-Type: application/json’ -d ‘{"positions": {"Knight":[1,2,3]}}’ 
# @api_view(('GET','POST'))
# @renderer_classes((TemplateHTMLRenderer,JSONRenderer))


def bishop_moves(position):
    # {"postions": {"Queen": "E7", "Bishop": "B7", "Rook":"G5", "Knight": "C3""}}
    # valid_moves = ["A8",B7,"C6","D5","E4","F3","G2","H1",,,,,"E6","F7","G8","C4","B3","A2"]
    # {"positions": {"Queen": "A5", "Bishop": "G8", "Rook":"H5", "Knight": "G4"}}
    bishop_pos_list,switch = [],0
    
    chess_width = ["A","B","C","D","E","F","G","H"]
    chess_index = ["1","2","3","4","5","6","7","8"]
    first_item,second_item = position[0],position[1]
    print(f"{switch}")
    first_index, second_index = chess_width.index(first_item),chess_index.index(second_item)
    while first_item in chess_width and second_item in chess_index:
        print("Inside While Loop")
        if switch==0:
            if first_index+1==len(chess_width) or second_index+1==len(chess_index):
                first_item,second_item = position[0],position[1]
                first_index, second_index = chess_width.index(first_item),chess_index.index(second_item)
                switch=1
            else:
                first_index+=1
                second_index+=1
                first_item,second_item = chess_width[first_index],chess_index[second_index]
                bishop_pos_list.append(first_item+second_item)
        elif switch==1:
            
            if first_index-1==-1 or second_index-1==-1:
                break
            else:
                first_index-=1
                second_index-=1
                first_item,second_item = chess_width[first_index],chess_index[second_index]
                bishop_pos_list.append(first_item+second_item)

    first_item,second_item = position[0],position[1]
    first_index, second_index = chess_width.index(first_item),chess_index.index(second_item)
    switch=0
    while first_item in chess_width and second_item in chess_index:
        
        if switch==0:
            if first_index+1==len(chess_width) or second_index-1==-1:
                first_item,second_item = position[0],position[1]
                first_index, second_index = chess_width.index(first_item),chess_index.index(second_item)
                switch=1
            else:
                first_index+=1
                second_index-=1
                first_item,second_item = chess_width[first_index],chess_index[second_index]
                bishop_pos_list.append(first_item+second_item)
        elif switch==1:
            
            if first_index-1==-1 or second_index+1==len(chess_index):
                break
            else:
                first_index-=1
                second_index+=1
                first_item,second_item = chess_width[first_index],chess_index[second_index]
                bishop_pos_list.append(first_item+second_item)

    print(bishop_pos_list)
    return bishop_pos_list

def rook_moves(position):
        
    rook_pos_list = []
    chess_index = ["1","2","3","4","5","6","7","8"]
    chess_width = ["A","B","C","D","E","F","G","H"]
    for item1 in chess_index:
        rook_pos_list.append(position[0]+item1)
        
    for item2 in chess_width:
        rook_pos_list.append(item2+position[1])
    print(rook_pos_list)
    return rook_pos_list


# Need to remove the duplicate element
def queen_moves(position):

    valid_rook_moves = rook_moves(position)
    valid_bishop_moves = bishop_moves(position)
    return valid_bishop_moves+valid_rook_moves

@csrf_exempt
def output(request,slug):
    """
    List all possible moves of the Knight.
    """
    
    # {"positions": {"Queen": "A5", "Bishop": "G8", "Rook":"H5", "Knight": "G4"}}
    if request.method == 'POST':
        if slug == "queen":
            # print(dir(request))
            # print(request.headers)
            valid_moves = {}
            json_data = json.loads(request.body)
            print("Request.BODY")
            # print(request.POST.get("positions")["Queen"])
            # print(request.body.decode()[1:10])
            print(json_data.get("positions").get("Queen"))
            valid_queen_moves = queen_moves(json_data.get("positions").get("Queen"))
            # {"Queen": "H1", "Bishop": "B7", "Rook":"H8", "Knight": "F2"}
            valid_moves["valid_moves"] = valid_queen_moves
            return JsonResponse(valid_moves)

        elif slug == "knight":

            return JsonResponse(request.data["positions"]["Knight"])

        elif slug == "rook":

            valid_moves = {}
            json_data = json.loads(request.body)
            valid_rook_moves = rook_moves(json_data.get("positions").get("Rook"))

            valid_moves["valid_moves"] = valid_rook_moves
            return JsonResponse(valid_moves)

        elif slug == "bishop":
            valid_moves = {}
            json_data = json.loads(request.body)
            valid_bishop_moves = bishop_moves(json_data.get("positions").get("Bishop"))

            valid_moves["valid_moves"] = valid_bishop_moves
            return JsonResponse(valid_moves)



        
    

    # def queen_decorator(func):
    #     def bishop_moves(*args):
    #         return bishop_arr
    #     def inner(*args):
    #         valid_bishop_moves = bishop_moves(*args)
    #         valid_rook_moves = rook_moves(*args)
    #         return set(valid_bishop_moves+valid_rook_moves)
    #     return inner


        # return 
        # data = JSONParser().parse(request)
        # print(slug)
        # print(type(slug))
        
        #     print(type(data))
        # return Response(data, template_name='assessments.html')
        # if slug == "knight":
        #     pass
        # elif slug == "queen":
        #     pass
        # elif slug == "rook":
        #     pass
        # elif slug == "bishop":
        #     pass
        
        
        
        # '''

        #  Input - {"postions": {"Queen": "E7", "Bishop": "B7", "Rook":"G5", "Knight": "C3""}}
        # '''
        # current_knight_pos = data["postion"]["Knight"]

        # '''"KnightC3" - {a4,a2,b5,d5,e4,e2,b1,d1}'''
        # '''queenE7 - {E1-E8,A7-H7,F6,G5,H4, D6,C5,B4,A3,F8,D8}'''
        # '''BishopB7 - {A6,A8,C8,C6,D5,E4,F3,G2,H1}'''
        # '''RookG5 - {}''' 
        # available_pos = 
        # '''
        # Output - {"valid_moves": ["A4", "A2", "B1","D1"]}
        # ''' 
        # serializer = SnippetSerializer(data=data)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse(serializer.data, status=201)
        # return JsonResponse(serializer.errors, status=400)


def hello(request):
    return HttpResponse("Hello World")