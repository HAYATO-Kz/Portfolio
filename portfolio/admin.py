from django.contrib import admin

from .models import Profile, Education, Project, Experince, Inbox, Skill

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('firstname', 'lastname', 'role')

class EducationAdmin(admin.ModelAdmin):
    list_display = ('start_year', 'end_year', 'department','university')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')

class ExperinceAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')    

class InboxAdmin(admin.ModelAdmin):
    list_display = ('email', 'subject', 'pub_date')

class SkillAdmin(admin.ModelAdmin):
    list_display = ('title', 'getText')

admin.site.register(Profile,ProfileAdmin)
admin.site.register(Education,EducationAdmin)
admin.site.register(Project,ProjectAdmin)
admin.site.register(Experince,ExperinceAdmin)
admin.site.register(Inbox,InboxAdmin)
admin.site.register(Skill,SkillAdmin)