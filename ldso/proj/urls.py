from __future__ import unicode_literals
from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from proj.models import Blog, Circulos, CirculoForum, Musica, Participante



urlpatterns = patterns('', 
	url(r'^$', ListView.as_view(
		queryset=Blog.objects.all().order_by("-date")[:0],
		template_name="base.html")),


	url(r'^blog/$', 'proj.views.blog_view', name= 'blog_view'),

	url(r'^blog/(?P<page_id>[0-9]+)/$', 'proj.views.blog_view_paginas', name= 'blog_view_paginas'),

	url(r'^blog/post/(?P<post_id>[0-9]+)/$', 'proj.views.post_view', name= 'post_view'),

	url(r'^login/$', ListView.as_view(
						model = Blog,
						template_name="login.html")),


	url(r'^forum/$', 'proj.views.forum_page', name= 'forum_page'),

	url(r'^forum/logout/$', 'proj.views.logout_view', name= 'logout_view'),

	url(r'^forum/(?P<forum_id>[0-9]+)/$', 'proj.views.forum_view', name= 'forum_view'),

	url(r'^forum/(?P<forum_id>[0-9]+)/(?P<pagina_id>[0-9]+)/$', 'proj.views.forum_view_pagina', name= 'forum_view_pagina'),

	url(r'^forum/(?P<forum_id>[0-9]+)/CriarTopico/$', 'proj.views.create_post', name= 'create_post'),

	url(r'^forum/(?P<forum_id>[0-9]+)/postTopico/$', 'proj.views.post_topico', name= 'post_topico'),

	url(r'^forum/topico/(?P<topico_id>[0-9]+)/$', 'proj.views.topico_view', name= 'topico_view'),

	url(r'^forum/topico/(?P<topico_id>[0-9]+)/(?P<pagina_id>[0-9]+)/$', 'proj.views.topico_view_paginas', name= 'topico_view_paginas'),

	url(r'^forum/topico/(?P<topico_id>[0-9]+)/(?P<outro_comentario>[/comentario/]*)comentario/$', 'proj.views.post_comentario', name= 'post_comentario'),

	url(r'^forum/mensagens/$', 'proj.views.mensagens_view', name= 'mensagens_view'),

	url(r'^forum/mensagem/(?P<user_id>[0-9]+)/$', 'proj.views.single_mensage', name= 'single_mensage'),

	url(r'^forum/mensagem/(?P<user_id>[0-9]+)/(?P<page_id>[0-9]+)/$', 'proj.views.single_mensage_paginas', name= 'single_mensage_paginas'),


	url(r'^forum/post_mensagem/(?P<user_id>[0-9]+)/$', 'proj.views.post_mensagem', name= 'post_mensagem'),

	url(r'^forum/post_mensagem/$', 'proj.views.post_mensagem_inicial', name= 'post_mensagem_inicial'),

	url(r'^forum/post_removeCom/$', 'proj.views.post_removeCom', name= 'post_removeCom'),

	url(r'^about/$', ListView.as_view(
                        queryset=Blog.objects.all().order_by("-date"),
                        template_name="about.html")),

	url(r'^contact/$', ListView.as_view(
                       	queryset=Blog.objects.all().order_by("-date"),
                        template_name="contact.html")),

	url(r'^post_email/$', 'proj.views.post_email', name= 'post_email'),

	url(r'^post_login/$', 'proj.views.login_view', name= 'login_view'),

	url(r'^post_User/$', 'proj.views.edit_names', name= 'edit_names'),

	url(r'^teste/$', 'proj.views.verifica_mensagens', name= 'verifica_mensagens'),

	url(r'^oquefazemos/$', ListView.as_view(
                        queryset=Blog.objects.all().order_by("-date"),
                        template_name="oquefazemos.html")),

	url(r'^parceiros/$', ListView.as_view(
                        queryset=Blog.objects.all().order_by("-date"),
                        template_name="patrocinios.html")),
	 
	 url(r'^circulos/$', ListView.as_view(
                        queryset=Circulos.objects.all().order_by("-date"),
                        template_name="circulos.html")),

	 url(r'^radio/$', ListView.as_view(
                        queryset=Musica.objects.all(),
                        template_name="radio.html")),


	 url(r'^forum/areapessoal/$', 'proj.views.area_pessoal', name= 'area_pessoal'),

	 url(r'^forum/editarperfil/$', ListView.as_view(
					model = Blog,
					template_name="editarprofile.html")),

	 url(r'^forum/novamensagem/$', 'proj.views.pessoal_circulo', name= 'pessoal_circulo'),

	 #url(r'^novamensagem/$', ListView.as_view(
      #                  queryset=Participante.objects.all(),
       #                 template_name="teste.html")),

	url(r'^(?P<pk>\d+)$', DetailView.as_view(
		model = Blog,
		template_name="post.html")),

	url(r'^base$', ListView.as_view(
		queryset=Blog.objects.all().order_by("-date"),
		template_name="base.html")),

	url(r'^api/user/$', 'proj.views.api_user', name= 'api_user'),

	url(r'^api/forum/$', 'proj.views.api_forum', name= 'api_forum'),

	url(r'^api/circulo/$', 'proj.views.api_circulo', name= 'api_circulo'),

	url(r'^api/mensagens/$', 'proj.views.api_forum', name= 'api_forum'), #notDone

	url(r'^api/mensagem/$', 'proj.views.api_mensagem', name= 'api_mensagem'), 

	url(r'^api/comentario/$', 'proj.views.api_comentario', name= 'api_comentario'),

	)