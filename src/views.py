from django.shortcuts import render

# Create your views here.
import razorpay
from .models import coffee
from django.views.decorators.csrf import csrf_exempt


def home(request):
    if request.method=="POST":
        name=request.POST.get("name")
        amount=int(request.POST.get("amount"))*100   
        client=razorpay.Client(auth=("rzp_test_FtwfAmevo4ofaL","hgsCqmlEqyJRDlty2v2GyjEW"))
        payment=client.order.create({'amount':amount, 'currency':'INR',"payment_capture":'1'})
        print(payment)
        Coffee=coffee(name=name, amount=amount,paymentid=payment["id"])
        Coffee.save()
        return render(request, 'index.html', {'payment':payment})


    return render(request, "index.html")


@csrf_exempt
def success(request):
    if request.method=='POST':
        a=request.POST
        order_id=""
        for key,val in a.items():
            if key=='razor_order_id':
                order_id=val
                break
        user=coffee.objects.filter(paymentid=order_id).first()
        if user is not None:
            client=razorpay.Client(auth=("rzp_test_FtwfAmevo4ofaL","hgsCqmlEqyJRDlty2v2GyjEW"))
            payment = client.payment.capture(user.paymentid, user.amount)
            if payment['status'] == 'captured':
                user.paid = True
                user.save()
    return render(request, "success.html")