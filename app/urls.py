from django.urls import path
from app import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('product/<slug>', views.ItemDetailView.as_view(), name='product'), # 追加
    path('additem/<slug>', views.addItem, name='additem'), # 追加
    path('order/', views.OrderView.as_view(), name='order'), # 追加
    path('removeitem/<slug>', views.removeItem, name='removeitem'), # 追加
    path('removesingleitem/<slug>', views.removeSingleItem, name='removesingleitem'), # 追加
    path('payment/', views.PaymentView.as_view(), name='payment'),
    path('thanks/', views.ThanksView.as_view(), name='thanks'), # 追加
]