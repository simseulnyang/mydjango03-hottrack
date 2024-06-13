from django.apps import AppConfig


class HottrackConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'hottrack'
    
    #ADDED : admin 페이지에서 지정 이름으로 보여집니다.
    verbose_name = "핫트랙"
