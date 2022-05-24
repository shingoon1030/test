from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from account import views as accountview
from homeapp import views as homeview
from freeboard import views as freeboardview
from questionboard import views as questionboardview
from lectureboard import views as lectureboardview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homeview.home, name = 'home'),

    path('summernote/', include('django_summernote.urls')),

    path('account/login/', accountview.login, name = 'login'),
    path('account/signup/', accountview.signup, name = 'signup'),
    path('account/logout/', accountview.logout, name = 'logout'),
    path('account/mustAuth/', accountview.mustAuth, name = 'mustAuth'),
    path('account/timetable/', accountview.timetableShow, name = 'timetable'),
    path('account/timetable/update/', accountview.timetableUpdate, name = 'timetableupdate'),
    path('account/activate/<str:uid64>/<str:token>/', accountview.activate, name = 'activate'),


    path('freeboard/', freeboardview.home, name = 'freeboard'),
    path('freeboard/new/', freeboardview.new, name = 'fnew'),
    path('freeboard/<int:post_id>/', freeboardview.detail, name = 'detail'),
    path('freeboard/delete/<int:post_id>/', freeboardview.del_detail, name = "delete"),
    path('freeboard/commentdelete/<int:post_id>/<int:comment_id>', freeboardview.del_comment, name = "commentdelete"),
    path('freeboard/create_comment/<int:post_id>', freeboardview.new_comment, name = 'fnew_comment'),   
    path('freeboard/search', freeboardview.search, name='search'),

    path('questionboard/', questionboardview.home, name = 'questionboard'),
    path('questionboard/new/', questionboardview.new, name = 'fnewQ'),
    path('questionboard/<int:post_id>/', questionboardview.detail, name = 'detailQ'),
    path('questionboard/delete/<int:post_id>/', questionboardview.del_detail, name = "deleteQ"),
    path('questionboard/commentdelete/<int:post_id>/<int:comment_id>', questionboardview.del_comment, name = "commentdeleteQ"),
    path('questionboard/create_comment/<int:post_id>', questionboardview.new_comment, name = 'fnew_commentQ'),  
    path('questionboard/search', questionboardview.search, name='searchQ'), 

    path('lectureboard/', lectureboardview.home, name = 'lectureboard'),
    path('lectureboard/new/', lectureboardview.new, name = 'fnewL'),
    path('lectureboard/<int:post_id>/', lectureboardview.detail, name = 'detailL'),
    path('lectureboard/delete/<int:post_id>/', lectureboardview.del_detail, name = "deleteL"),
    path('lectureboard/search', lectureboardview.search, name='searchL'), 


    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)