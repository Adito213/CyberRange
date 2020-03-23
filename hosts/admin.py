from django.contrib import admin

from .models import Logs
from .models import Sreenshots
from .models import Category
from .models import Source
from .models import Team
from .models import Trainings
#Register your models here

admin.site.register(Logs)
admin.site.register(Sreenshots)
admin.site.register(Category)
admin.site.register(Source)
admin.site.register(Team)
admin.site.register(Trainings)




# Model have been register to admin

