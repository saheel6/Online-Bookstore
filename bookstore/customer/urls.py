from django.urls import path
from .views import customerhomeview,popup_view,addcart,cartshowview,cartdeleteview,checkoutview,ordershow,search,filterselectview,filtershowview,edit_profile

urlpatterns = [
    path('customerhome',customerhomeview.as_view(),name='home'),
    path('popup/',popup_view,name='popupp'),
    path('addcart/<int:pid>',addcart.as_view(),name='addcart'),
    path('carttshow',cartshowview.as_view(),name='cartshow'),
    path('cartdelete/<int:id>',cartdeleteview,name='delcart'),
    path('checkoutt/<int:cid>',checkoutview.as_view(),name="ckout"),
    path('orders',ordershow.as_view(),name='ordershoww'),
    path('searchresult',search.as_view(),name='searchres'),
    path('filterselect',filterselectview.as_view(),name='fbselect'),
    path('filetershow',filtershowview.as_view(),name='fbshow'),
    path('profile/edit/',edit_profile, name='edit_profile'),

]