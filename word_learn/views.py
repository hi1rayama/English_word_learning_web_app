from django.contrib.auth.forms import UserCreationForm  
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.shortcuts import render
from django.shortcuts import redirect,get_object_or_404
from django.utils import timezone
from django.urls import reverse_lazy 
from django.views.generic import TemplateView,CreateView,ListView,View
from django.http import HttpResponse


from . import forms
from .forms import WordForm
from .models import Word


class HomeView(TemplateView): 
	'''
	ログイン前のホーム画面
	'''
	template_name = 'word_learn/home.html'  #テンプレート名を指定している。TemplateViewでは必須。

	def home(self,request):  #基本的には親メソッドをオーバーライドして独自処理を追加する。	
		 return HttpResponse(self.tempalte_name)


class UserHomeView(ListView):
	'''
	ログイン後のユーザーのホーム画面
	'''
	model=Word
	template_name='word_learn/user_menu.html'
	context_object_name = 'words'
	def get_queryset(self):
		return Word.objects.filter(user=self.request.user)
		

class ResisterWordView(View):
	'''
	英単語登録画面
	'''
	form_class=WordForm
	template_name='word_learn/resister_word.html'

	def get(self, request, *args, **kwargs):
		form = self.form_class()
		return render(request, self.template_name, {'form': form})
	
	def post(self, request, *args, **kwargs):
		form = self.form_class(request.POST)
		if form.is_valid():
			word = form.save(commit=False)
			word.user = request.user
			word.save()
			return redirect('ResisterWord')
		return render(request, self.template_name, {'form': form})


	
def LearningHome(request):
	'''
	学習サイトのホーム画面
	'''

	if request.method == "POST":
		radio_value = request.POST.getlist('range')
		r=radio_value.pop(0)
		return redirect('Learning',value=r)
		

	return render(request,'word_learn/learning_home.html',{})



def Learning(request,value='all',*args,**kwargs):
	'''
	苦手英単語一覧
	'''
	if value=='weak':
		weaks=Word.objects.filter(user=request.user,weak=True)
	else:
		weaks=Word.objects.filter(user=request.user)
	
	ans={}
	if request.method == "POST":
		for word in weaks:
			a=request.POST.get(str(word.id))
			if len(a)!=0:
				if word.japanese_word==a:
					ans.setdefault(str(a), []).append(word.english_word)
					ans.setdefault(str(a), []).append(word.japanese_word)

				else:
					ans.setdefault(str(a), []).append(word.english_word)
					ans.setdefault(str(a), []).append(word.japanese_word)					
		context = {'answer': ans}
		print(ans)
		return render(request,'word_learn/result.html',context)
	

	return render(request,'word_learn/learning.html',{'weaks':weaks})


def Result(request,*args,**kwargs):
	'''
	回答結果
	'''
	weaks=kwargs

	return render(request,'word_learn/result.html',{'weaks':weaks})


class WeakListView(ListView):
	'''
	苦手英単語一覧
	'''
	model=Word
	template_name='word_learn/weak_list.html'
	context_object_name = 'weaks'
	def get_queryset(self):
		return Word.objects.filter(user=self.request.user,weak=True)
		

def WeakListEdit(request,*args,**kwargs):
	'''
	苦手単語リストを編集する
	'''
	words=Word.objects.filter(user=request.user)
	checks_value = request.POST.getlist('list[]')
	print("checks_value = " + str(checks_value))
	lis=[]
	if request.method == "POST":
		for w in words:
			w.weak=False
			for id in checks_value:
				if w.id==int(id):
					w.weak=True
			lis.append(w)
		Word.objects.bulk_update(lis, fields=['weak'])
		return redirect('WeakList')
	return render(request,'word_learn/weak_list_edit.html',{'words':words})	



#ブログ引用
class MyLoginView(LoginView):
    form_class = forms.LoginForm
    template_name = "word_learn/login.html"

class MyLogoutView(LoginRequiredMixin, LogoutView):
    template_name = "word_learn/logout.html"

class IndexView(TemplateView):
    template_name = "word_learn/index.html"


class UserCreateView(CreateView):
    form_class = UserCreationForm
    template_name = "word_learn/create.html"
    success_url = reverse_lazy("login")



	