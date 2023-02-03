from django.db.models import Manager


class TodoManager(Manager):

    def get_done_todos_by_user(self, user):
        '''
        This Method Will Return List Of Todo for User With is_done=True 
        '''
        todos = self.get_queryset().filter(user=user, is_done=True)
        return todos

    def get_pending_todos_by_user(self, user):
        '''
        This Method Will Return List Of Todo for User With is_done=False 
        '''
        object_list = self.get_queryset().filter(is_done=False, user=user)
        return object_list