from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Course, CartItem

def courses(request):
    all_courses = Course.objects.all()
    return render(request, 'courses.html', {'courses': all_courses})

@login_required
def add_to_cart(request, id):
    course = get_object_or_404(Course, id=id)
    cartitem, created = CartItem.objects.get_or_create(user=request.user, courses=course)
    if not created:
        cartitem.quantity += 1
    cartitem.save()
    return redirect('cart')

@login_required
def cart(request):
    cart_items = CartItem.objects.filter(user=request.user)
    total_price = sum(item.courses.price * item.quantity for item in cart_items)
    return render(request, 'cart.html', {'cart_items': cart_items, 'total_price': total_price})

@login_required
def remove_from_cart(request, id):
    cartitem = get_object_or_404(CartItem, id=id, user=request.user)
    cartitem.delete()
    return redirect('cart')

def search_products(request):
    query = request.GET.get('q', '')  # Safely get 'q' with a default value
    if query:
        products = Course.objects.filter(title__icontains=query)
    else:
        products = Course.objects.none()
    return render(request, 'search.html', {'products': products, 'query': query})
