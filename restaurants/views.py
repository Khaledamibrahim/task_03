from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    'my_list': [
    
    	{'restaurant_name': 'Shehabs',
    	'food_type': 'fast food'},

    	{'restaurant_name': 'Khaleds',
    	'food_type': 'international'},

    	{'restaurant_name': 'coded',
    	'food_type': 'snacks'}]

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {
    	'my_object': 

    	{'restaurant_name': 'Shuwaikh', 
    	'food_type': 'Shawarma'},
    	

    }
    return render(request, 'detail.html', context)
