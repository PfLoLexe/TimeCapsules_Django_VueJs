from django.urls import path
from projectFirst_app import views

urlpatterns = [
    path('vault/all', views.CapsuleListView_All.as_view(), name='vault_list'),
    path('vault/closed', views.CapsuleListView_Closed.as_view(), name='vault_list'),
    path('vault/opened', views.CapsuleListView_Opened.as_view(), name='vault_list'),
    path('vault/my/<int:user_pk>', views.CapsuleListView_My.as_view(), name='vault_list'),
    path('vault/notmy/<int:user_pk>', views.CapsuleListView_NotMy.as_view(), name='vault_list'),
    path('vault/create', views.CapsuleCreateView.as_view(), name='vault_new'),
    path('vault/<int:vault_pk>/<int:user_pk>', views.CapsuleDetailView.as_view(), name='vault_detail'),

    path('vault/<int:vault_pk>/file', views.CapsuleFileListView.as_view(), name='vault_file_list'),
    path('vault/<int:vault_pk>/file/create', views.CapsuleFileCreateView.as_view(), name='vault_file_new'),

    path('vault/comments/<int:vault_pk>/', views.CapsuleCommentsView.as_view(), name='vault_comments_list'),
    path('vault/comments/create', views.CapsuleCommentCreateView.as_view(), name='vault_comments_new'),

    path('vault/<int:vault_pk>/access', views.CapsuleAccessListView.as_view(), name='vault_access_list'),
    path('vault/<int:vault_pk>/access/add', views.CapsuleAccessCreateView.as_view(), name='vault_access_new'),

    path('person/update/<int:pk>', views.PersonUpdateView.as_view(), name='people_list'),
    path('person/<int:pk>/', views.SidePersonDetailView.as_view(), name='person_detail'),
    path('person/<int:pk>/friends', views.PersonFriendsList.as_view(), name='person_friendslist'),
    path('person/addfriend', views.PeopleFriendShipAddView.as_view(), name='people_friends_add'),
    path('person/deletefriend/<int:f_id>/<int:t_id>', views.PeopleFriendShipDeleteView.as_view(), name='people_friends_delete'),
]