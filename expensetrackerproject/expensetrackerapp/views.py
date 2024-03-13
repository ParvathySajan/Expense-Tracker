from django.shortcuts import render
from.models import Expense,Balance

# Create your views here.
def home(request):
    return render(request,'index.html')

def addexpense(request):
    try:
        '''initiol_amt=int(request.POST['initiol'])   
        ilist=Balance(balance_amount=initiol_amt)
        ilist.save()
        return render(request,'index.html',{'msg':'added'})'''
        response={}
        expname=request.POST['exp']
        expamount=int(request.POST['amt'])
        exps=Expense.objects.all()
        flag=0
        for i in exps:
            if expname in i.expense_name:
                flag=1
        if flag==1:
            blist=Balance.objects.get(id=1)
            initiol=blist.balance_amount
            if expamount>initiol:
                response['msg']='insufficient balance'
            else:
                amtlist=Expense.objects.get(expense_name=expname)
                amtlist.save()
                old=amtlist.amount+expamount
                Expense.objects.filter(expense_name=expname).update(amount=old)
                blist=Balance.objects.get(id=1)  
                blist.balance_amount=blist.balance_amount-expamount
                blist.save()
                response['msg']='Expense Added'
                return render(request, 'index.html',response)
        else:
            blist=Balance.objects.get(id=1)
            if expamount>blist.balance_amount:
                response['msg']='insufficient balance'
            else:    
                blist=Balance.objects.get(id=1)  
                blist.balance_amount=blist.balance_amount-expamount
                blist.save()
                explist=Expense(expense_name=expname,amount=expamount)
                explist.save()
                response['msg']='Expense Added'
        return render(request, 'index.html',response)
    except Exception as e:
        print(e)
        response['msg']='Expense not added'
        return render(request, 'index.html',response)

def displayexpense(request):
    expdtls=Expense.objects.all()
    return render(request,'index.html',{'exp':expdtls})
def displaybalance(request):
    baldtls=Balance.objects.all()
    return render(request,'index.html',{'blns':baldtls})
    
def creditcash(request):
    camount=int(request.POST['cramt'])
    bls=Balance.objects.get(id=1)
    bls.balance_amount=bls.balance_amount+camount
    bls.save()
    return render(request,'index.html',{'cmsg':'Credited successfully Current balance :'+str(bls.balance_amount)})
    