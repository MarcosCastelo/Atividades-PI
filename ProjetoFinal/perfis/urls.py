from django.urls import path
from . import views
from usuarios.views import RedefinirSenhaView


urlpatterns = [
    path('perfil/<int:perfil_id>', views.exibir_perfil, name='exibir'),
    path('perfil/', views.PerfilView.as_view(), name='meu_perfil'),
    path('perfil/<int:perfil_id>/convidar', views.convidar, name='convidar'),
    path('perfil/<int:perfil_id>/desfazer', views.desfazer, name='desfazer'),
    path('perfil/redefinir_senha',RedefinirSenhaView.as_view(), name='form_redefinir_senha'),
    path('perfil/desativar_conta',views.desativar_conta, name='desativar_conta'),
    path('perfil/ativar_conta',views.ativar_conta, name='ativar_conta'),
    path('perfil/desativar', views.DesativarContaView.as_view(), name='desativar'),
    path('perfil/ativar', views.AtivarContaView.as_view(), name='ativar'),
    path('perfil/<int:perfil_id>/super', views.setarSuperUsuario, name='super'),
    path('perfil/<int:perfil_id>/bloquear', views.bloquear, name='bloquear'),
    path('perfil/<int:bloqueio_id>/desbloquear', views.desbloquear, name='desbloquear'),
    path('perfil/postar', views.PostarView.as_view(), name='postar'),
    path('perfil/pesquisar', views.PesquisarPerfilView.as_view(), name='pesquisar'),
]
