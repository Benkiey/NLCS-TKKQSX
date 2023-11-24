from django.shortcuts import render
from .models import LotteryNumber
from django.db.models import Count
from django.db import connection
import matplotlib.pyplot as plt
from django.http import JsonResponse



# Create your views here.
def home(request):
    return render(request, 'app/home.html')
def base(request):
    return render(request, 'app/base.html')
######################################################################################

def thongke(request):
    # Tạo danh sách chứa tất cả các số từ 00 đến 99
    all_numbers = [f"{i:02d}" for i in range(100)]
    
    # Lấy ra 0 số lô tô đầu tiên
    recent_lottery_numbers = LotteryNumber.objects.all()[:0]
    
    # Tạo một từ điển đếm số lần xuất hiện của mỗi số
    number_counts = {num: 0 for num in all_numbers}
    for number in recent_lottery_numbers:
        num = f"{number.number:02d}"
        number_counts[num] += 1

    # Chuyển từ điển thành danh sách kết quả
    result = [(num, count) for num, count in number_counts.items()]

    # Sắp xếp các số theo thứ tự tăng dần
    sorted_number_counts = sorted(result)

    # Lấy ra 3 con số ít nhất và 3 con số nhiều nhất
    sorted_number_counts2 = sorted(result, key=lambda x: x[1])
    min_numbers = sorted_number_counts2[:3]
    max_numbers = sorted_number_counts2[-3:]

    

    return render(request, 'app/thongke.html', {'number_counts': sorted_number_counts, 'min_numbers': min_numbers, 'max_numbers': max_numbers})

###########################
def thongke50(request):
    # Tạo danh sách chứa tất cả các số từ 00 đến 99
    all_numbers = [f"{i:02d}" for i in range(100)]
    
    # Lấy ra 50 số lô tô đầu tiên
    recent_lottery_numbers = LotteryNumber.objects.all()[:50]
    
    # Tạo một từ điển đếm số lần xuất hiện của mỗi số
    number_counts = {num: 0 for num in all_numbers}
    for number in recent_lottery_numbers:
        num = f"{number.number:02d}"
        number_counts[num] += 1

    # Chuyển từ điển thành danh sách kết quả
    result = [(num, count) for num, count in number_counts.items()]

    # Sắp xếp các số theo thứ tự tăng dần
    sorted_number_counts = sorted(result)

    # Lấy ra 3 con số ít nhất và 3 con số nhiều nhất
    sorted_number_counts2 = sorted(result, key=lambda x: x[1])
    min_numbers = sorted_number_counts2[:3]
    max_numbers = sorted_number_counts2[-3:]

    

    return render(request, 'app/thongke50.html', {'number_counts': sorted_number_counts, 'min_numbers': min_numbers, 'max_numbers': max_numbers})
##################################################
def thongke100(request):
    # Tạo danh sách chứa tất cả các số từ 00 đến 99
    all_numbers = [f"{i:02d}" for i in range(100)]
    
    # Lấy ra 50 số lô tô đầu tiên
    recent_lottery_numbers = LotteryNumber.objects.all()[:100]
    
    # Tạo một từ điển đếm số lần xuất hiện của mỗi số
    number_counts = {num: 0 for num in all_numbers}
    for number in recent_lottery_numbers:
        num = f"{number.number:02d}"
        number_counts[num] += 1

    # Chuyển từ điển thành danh sách kết quả
    result = [(num, count) for num, count in number_counts.items()]

    # Sắp xếp các số theo thứ tự tăng dần
    sorted_number_counts = sorted(result)

    # Lấy ra 3 con số ít nhất và 3 con số nhiều nhất
    sorted_number_counts2 = sorted(result, key=lambda x: x[1])
    min_numbers = sorted_number_counts2[:3]
    max_numbers = sorted_number_counts2[-3:]

    

    return render(request, 'app/thongke100.html', {'number_counts': sorted_number_counts, 'min_numbers': min_numbers, 'max_numbers': max_numbers})
#####################################################
def thongke200(request):
    # Tạo danh sách chứa tất cả các số từ 00 đến 99
    all_numbers = [f"{i:02d}" for i in range(100)]
    
    # Lấy ra 50 số lô tô đầu tiên
    recent_lottery_numbers = LotteryNumber.objects.all()[:200]
    
    # Tạo một từ điển đếm số lần xuất hiện của mỗi số
    number_counts = {num: 0 for num in all_numbers}
    for number in recent_lottery_numbers:
        num = f"{number.number:02d}"
        number_counts[num] += 1

    # Chuyển từ điển thành danh sách kết quả
    result = [(num, count) for num, count in number_counts.items()]

    # Sắp xếp các số theo thứ tự tăng dần
    sorted_number_counts = sorted(result)

    # Lấy ra 3 con số ít nhất và 3 con số nhiều nhất
    sorted_number_counts2 = sorted(result, key=lambda x: x[1])
    min_numbers = sorted_number_counts2[:3]
    max_numbers = sorted_number_counts2[-3:]

    

    return render(request, 'app/thongke200.html', {'number_counts': sorted_number_counts, 'min_numbers': min_numbers, 'max_numbers': max_numbers})
###################################################
def thongke500(request):
    # Tạo danh sách chứa tất cả các số từ 00 đến 99
    all_numbers = [f"{i:02d}" for i in range(100)]
    
    # Lấy ra 50 số lô tô đầu tiên
    recent_lottery_numbers = LotteryNumber.objects.all()[:500]
    
    # Tạo một từ điển đếm số lần xuất hiện của mỗi số
    number_counts = {num: 0 for num in all_numbers}
    for number in recent_lottery_numbers:
        num = f"{number.number:02d}"
        number_counts[num] += 1

    # Chuyển từ điển thành danh sách kết quả
    result = [(num, count) for num, count in number_counts.items()]

    # Sắp xếp các số theo thứ tự tăng dần
    sorted_number_counts = sorted(result)

    # Lấy ra 3 con số ít nhất và 3 con số nhiều nhất
    sorted_number_counts2 = sorted(result, key=lambda x: x[1])
    min_numbers = sorted_number_counts2[:3]
    max_numbers = sorted_number_counts2[-3:]

    

    return render(request, 'app/thongke500.html', {'number_counts': sorted_number_counts, 'min_numbers': min_numbers, 'max_numbers': max_numbers})






        













































        # # Lấy tất cả kết quả thống kê cho số lần quay đã chọn
        # statistics = (
        #     LotteryNumber.objects.values('number')
        #     .annotate(count=Count('number'))

        #     .order_by('number')
        # )

        # # Sắp xếp kết quả thống kê theo số lần xuất hiện tăng dần
        # sorted_statistics = sorted(statistics, key=lambda x: x['count'])

        # # Lấy 3 con số xuất hiện ít nhất
        # min_count_numbers = sorted_statistics[:3]

        # # Lấy 3 con số xuất hiện nhiều nhất
        # max_count_numbers = sorted_statistics[-3:]

        # return render(request, 'app/thongke.html', {'statistics': statistics, 'min_count_numbers': min_count_numbers, 'max_count_numbers': max_count_numbers})










################################################################################
# def thongke(request):
#     # Lấy tất cả kết quả thống kê
#     statistics = (
#         LotteryNumber.objects.filter(number__gte='00', number__lte='99')
#         .values('number')
#         .annotate(count=Count('number'))
#         .order_by('number')
#     )
    

#     # Sắp xếp kết quả thống kê theo số lần xuất hiện tăng dần
#     sorted_statistics = sorted(statistics, key=lambda x: x['count'])

#     # Lấy 3 con số xuất hiện ít nhất
#     min_count_numbers = sorted_statistics[:3]

#     # Lấy 3 con số xuất hiện nhiều nhất
#     max_count_numbers = sorted_statistics[-3:]

#     return render(request, 'app/thongke.html', {'statistics': statistics, 'min_count_numbers': min_count_numbers, 'max_count_numbers': max_count_numbers})









def quaythu(request):
    return render(request, 'app/quaythu.html')




























# def thongke(request):
#     return render(request, 'app/thongke.html')
#v2:
# def thongke(request):
#     statistics = (
#         LotteryNumber.objects.filter(number__gte='00', number__lte='99')
#         .values('number')
#         .annotate(count=Count('number'))
#         .order_by('number')
#     )

#     return render(request, 'app/thongke.html', {'statistics': statistics})