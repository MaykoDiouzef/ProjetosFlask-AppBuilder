from flask import render_template, flash
from flask_appbuilder.forms import DynamicForm
from flask_appbuilder.security.sqla.models import Role
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder import ModelView, ModelRestApi, AppBuilder, expose, BaseView, has_access, SimpleFormView
from flask_babel import lazy_gettext as _
from wtforms import SelectField

from app.models import Contact, ContactGroup
from .forms import MyForm

from . import appbuilder, db


"""
    Create your Model based REST API::

    class MyModelApi(ModelRestApi):
        datamodel = SQLAInterface(MyModel)

    appbuilder.add_api(MyModelApi)


    Create your Views::


    class MyModelView(ModelView):
        datamodel = SQLAInterface(MyModel)


    Next, register your Views::


    appbuilder.add_view(
        MyModelView,
        "My View",
        icon="fa-folder-open-o",
        category="My Category",
        category_icon='fa-envelope'
    )
"""

"""
    Application wide 404 error handler
"""

class CustomUserForm(DynamicForm):
    role = SelectField("Role", widget=Select2Widget())

class CustomUserView(ModelView):
    base_permissions = ["can_add", "can_edit", "can_delete", "can_list"]
    form = CustomUserForm

    def __init__(self):
        super().__init__()
        # Aqui você limita os papéis disponíveis com base no papel do usuário logado
        user_role = self.get_user_role()  # Função para obter o papel do usuário
        if user_role == "Admin":
            allowed_roles = ["Public"]
        elif user_role == "Public":
            allowed_roles = ["Teste"]
        else:
            allowed_roles = []

        # Filtra os papéis permitidos no formulário
        self.form.role.choices = [(role.id, role.name) for role in Role.query.filter(Role.name.in_(allowed_roles))]

class ContactModelView(ModelView):
    datamodel = SQLAInterface(Contact)

    label_columns = {'contact_group':'Grupo de Contato'}
    list_columns = ['nome','celular_pessoal','aniversario','contact_group']

    show_fieldsets = [
        (
            'Resumo',
            {'fields': ['nome', 'logradouro', 'contact_group']}
        ),
        (
            'Informações pessoais',
            {'fields': ['aniversario', 'telefone_pessoal', 'celular_pessoal'], 'expanded': False}
        ),
    ]

class GroupModelView(ModelView):
    datamodel = SQLAInterface(ContactGroup)
    related_views = [ContactModelView]


appbuilder.add_view(
    GroupModelView,
    "Lista de Grupos",
    icon = "fa-folder-open-o",
    category = "Contatos",
    category_icon = "fa-envelope"
)

appbuilder.add_view(
    ContactModelView,
    "Lista de Contatos",
    icon = "fa-envelope",
    category = "Contatos"
)


@appbuilder.app.errorhandler(404)
def page_not_found(e):
    return (
        render_template(
            "404.html", base_template=appbuilder.base_template, appbuilder=appbuilder
        ),
        404,
    )


db.create_all()
