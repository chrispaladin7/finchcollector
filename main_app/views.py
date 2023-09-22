from django.shortcuts import render

finches = [
    {
        'species': 'House Finch',
        'color': 'Red',
        'size': 'Small',
        'description': 'Common backyard bird with red plumage.'
    },
    {
        'species': 'American Goldfinch',
        'color': 'Yellow',
        'size': 'Small',
        'description': 'Bright yellow bird with black wings.'
    },
    {
        'species': 'European Goldfinch',
        'color': 'Red and Yellow',
        'size': 'Small',
        'description': 'Distinctive red and yellow plumage.'
    },
    {
        'species': 'Zebra Finch',
        'color': 'Gray and White',
        'size': 'Small',
        'description': 'Small bird with striped plumage.'
    },
    {
        'species': 'Purple Finch',
        'color': 'Reddish-Purple',
        'size': 'Small',
        'description': 'Males have striking reddish-purple plumage.'
    },
    {
        'species': 'Cassins Finch',
        'color': 'Brown and Red',
        'size': 'Small',
        'description': 'Small finch with distinctive head markings.'
    },
    {
        'species': 'Pine Siskin',
        'color': 'Streaked Brown',
        'size': 'Small',
        'description': 'Small finch with streaked brown plumage.'
    },
    {
        'species': 'Lesser Goldfinch',
        'color': 'Black and Yellow',
        'size': 'Small',
        'description': 'Small finch with black and yellow plumage.'
    },
    {
        'species': 'Yellow-crowned Bishop',
        'color': 'Yellow and Black',
        'size': 'Small',
        'description': 'African finch with distinctive plumage.'
    },
    {
        'species': 'Red-headed Finch',
        'color': 'Red and Brown',
        'size': 'Small',
        'description': 'African finch with red head and brown body.'
    },
]

# Create your views here.
def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def finches_index(request):
    return render(request,'finches/index.html',{
        'finches': finches
    })
