from django.shortcuts import render

# Create your views here.
from   django.shortcuts        import   render
from   rest_framework.views    import   APIView
from   rest_framework          import   status
from   .models                 import   *
from   rest_framework          import   generics
from   .serializers            import   *
from   rest_framework.response import   Response
from   django.core.mail        import   send_mail
from   datetime                import   datetime



class CustomerCart(generics.CreateAPIView):
    serializer_class = CustomerCartSerializer

    def get(self,request,format= None):

        try:
            queryset = CutomerCart.objects.filter(customer_details =request.user).all().values()
            return Response(queryset)
        except:
            return Response("Cart is empty")


    def post(self,request,format = None):
        serializer = CustomerCartSerializer(data = request.data)
        if serializer.is_valid():
             serializer.validated_data['customer_details'] = self.request.user
             try:
                CutomerCart.objects.filter(customer_details =request.user).delete()
             except:
                pass
             serializer.save()
             return Response({"message": "added to cart"})
        return Response({'message': list(serializer.errors.keys())[0]+' - '+list(serializer.errors.values())[0][0]}, status=status.HTTP_200_OK)







class CreateOrders(generics.CreateAPIView):
    
    serializer_class = CustomerOrdersSerializer
    def get(self,request,format = None):
        

        data={}
        #order data
        try:
            order_data = CutomerCart.objects.filter(customer_details= request.user).all().values()
            print('order_data')
            orders = order_data[0]['orders']
            data['orders'] =[]
            data['order_price']=0

            for i in orders:
                data['orders'].append({'item_name': i['item_name'],'item_price': i['item_price']})
                data['order_price']=data['order_price'] + i['item_price']

        except:
            return Response("your cart is empty")
        
        

        # data['ordered_date_time']=datetime.now()
        data['ordered_quantity'] =len(orders)
        data['delivery_charges']=30
        data['discount']=0
        data['final_price'] = int(data['order_price']) + int(data['delivery_charges'])-int((int(data['order_price'])*int(data['discount']))/100)

        #payment data
        # data['mode_of_payment']="null"
        # data['is_paid']=0

        # #delivery data
        # delivery_person = getdeliverypersondetails()
        # print(delivery_person)
        # data['delivery_person_name']=delivery_person['name']
        # data['delivery_person_phone']=delivery_person['phone']
        # data['is_delivered']=0
        # data['is_canceled']=0
        # data['reason_for_cancel']=0
        # data['is_confirmed']=0

        serializer = CustomerOrdersSerializer(data = data)
        if serializer.is_valid():
            serializer.save()
       
        return Response(serializer.data)
        # return Response({'message': list(serializer.errors.keys())[0]+' - '+list(serializer.errors.values())[0][0]}, status=status.HTTP_200_OK)


    def post(self, request, format=None):
        serializer = CustomerOrdersSerializer(data=request.data)
        if serializer.is_valid():


            #customer data
            serializer.validated_data['customer']  = request.user
            serializer.validated_data['name']      = request.user.name
            serializer.validated_data['mail']      = request.user.email
            serializer.validated_data['phone']      = request.user.phone
            serializer.validated_data['location']  = request.user.address1

            #orders datas
            customer = serializer.validated_data['customer']
            # serializer.validated_data['final_price']=int(serializer.validated_data['order_price']) + int(serializer.validated_data['delivery_charges'])-int((int(serializer.validated_data['order_price'])*int(serializer.validated_data['discount']))/100)
            
            if serializer.validated_data['mode_of_payment'] == 'Pay_on_delivery':
                print("pay on delivery")
            else:
                #paymet api 
                #if 
                #else
                
                print("online")

            serializer.save()
            CutomerCart.objects.filter(customer_details =request.user).delete()
        
            return Response({"data": serializer.data,"message": "Order Successfully Placed" }, status=status.HTTP_201_CREATED)
            
        return Response({'message': list(serializer.errors.keys())[0]+' - '+list(serializer.errors.values())[0][0]}, status=status.HTTP_200_OK)














def getdeliverypersondetails():
    name = "first assigned one"
    phone = 9381097438
    data = {'name':name , 'phone':phone}
    return data































# class UpdateOrders(APIView):
#     serializer_class =CustomerOrdersSerializer

#     def get(self,request,pk):
#         queryset = CustomerOrders.objects.all().filter(pk = pk).values()
#         return Response(queryset)

#     def patch(self, request,pk):
#         update_object = CustomerOrders.objects.get(pk= pk)
#         serializer = CustomerOrdersSerializer(update_object, data=request.data, partial=True)
#         if serializer.is_valid():
#             serializer.save()
#             return Response( data=serializer.data)
#         return Response( data="wrong parameters")
