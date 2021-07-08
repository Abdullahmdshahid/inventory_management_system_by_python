from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.urls import reverse
from .models import *
from .forms import productForm,customerForm

def home(request):
	return render(request, "allform/home.html")


# Product views ---

def addproduct(request):
    if request.method == "POST":
        form = productForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("product")
    form = productForm()    
    return render(request, "allform/product/add_new_product.html", {'form':form})


def product(request):
	products = Product.objects.all()
	return render(request, "allform/product/product.html",{'products':products})

def editproduct(request, pk):
	products = Product.objects.get(id=pk)
	form = productForm(instance=products)
	if request.method == "POST":
		form = productForm(request.POST,instance=products)
		if form.is_valid():
			form.save()
			return redirect("product")

	return render(request, "allform/product/edit_product.html",{'form':form})


def deleteproduct(request, pk):
	products = Product.objects.get(id=pk)
	context = {'products':products,'name':products}
	return render(request, "allform/product/delete_product.html", context)

#-----

# Customer views -----

def addcustomer(request):
	if request.method == "POST":
		form = customerForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("customer")
	form = customerForm()
	return render(request, "allform/customer/add_new_customer.html",{'form':form})



def customer(request):
	customers = Customer.objects.all()
	return render(request, "allform/customer/customer.html",{'customers':customers})



def editcustomer(request, pk):
	customers = Customer.objects.get(id=pk)
	form = customerForm(instance=customers)
	if request.method == "POST":
		form = customerForm(request.POST,instance=customers)
		if form.is_valid():
			form.save()
			return redirect("customer")

	return render(request, "allform/customer/edit_customer.html",{'form':form})


def deletecustomer(request, pk):
	customers = Customer.objects.get(id=pk)
	context = {'customers':customers,'name':customers}
	return render(request, "allform/customer/delete_customer.html", context)
	

#---------