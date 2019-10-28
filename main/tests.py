from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.test import Client
from django.test import TestCase
from main.forms import EntryForm
from main.models import Entry,UserProfile,Star,Comment


# Create your tests here.
   
class EntryTestCase(TestCase):

    def test_create_entry(self):
        user = User.objects.create_user(username='test',email='test@test.com',password='P@ssw0rd')
        Entry.objects.create(user=user,keyword='What did you do today?',content='I read a bit today')

    def test_entryform_valid(self):
        user = User.objects.create_user(username='test2',email='test2@test.com',password='P@ssw0rd')
        form = EntryForm({'user':user,'keyword':'test','content':'this is a test'})
        self.assertTrue(form.is_valid())

class UserprofileTestCase(TestCase):

    def test_create_userprofile(self):
        user = User.objects.create_user(username='gohankurehama',email='yosh@gmail.com',password='svm34J407675@')
        user_profile = UserProfile.objects.create(user=user,avatar='',date_of_birth=datetime.now(),description='nerd uo')

    

class StarTestCase(TestCase):

    def test_add_star(self):
        user = User.objects.create_user(username='starry',email='starru@test.com',password='kgtw830eL*')
        entry = Entry.objects.create(user=user,keyword='Debian',content='I miss using debian')
        Star.objects.create(user=user,entry=entry)

class CommentTestCase(TestCase):

    def test_create_comment(self):
        user = User.objects.create_user(username='gendo ikari',email='gendo@gmail.com',password='054jgL;@##4*')
        entry = Entry.objects.create(user=user,keyword='Gentoo',content='install gentoo')
        Comment.objects.create(entry=entry,user=user,content='nope')


       














  

