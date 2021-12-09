from .models import *


class IsmaMixin:

    def is_ma(self):

        groups =  []
        for g in self.request.user.groups.all():
            groups.append(g.name)

        if 'Менеджеры' in groups:
            return True
        else:
            return False