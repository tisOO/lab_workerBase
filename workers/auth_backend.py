from django.contrib.auth.backends import ModelBackend

from workers.models import Worker


class WorkerModelBackend(ModelBackend):
    user_class = Worker

    def authenticate(self, username=None, password=None):
        try:
            user = self.user_class.objects.get(username = username)
            if user.check_password(password):
                return user
        except self.user_class.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return self.user_class.objects.get(pk=user_id)
        except self.user_class.DoesNotExist:
            return None
