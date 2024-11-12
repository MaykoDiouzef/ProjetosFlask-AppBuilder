from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date
from sqlalchemy.orm import relationship

"""

You can use the extra Flask-AppBuilder fields and Mixin's

AuditMixin will add automatic timestamp of created and modified by who


"""


class ContactGroup(Model):
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.nome


class Contact(Model):
    id = Column(Integer, primary_key=True)
    nome =  Column(String(150), unique = True, nullable=False)
    logradouro =  Column(String(564), default='Street ')
    aniversario = Column(Date)
    telefone_pessoal = Column(String(20))
    celular_pessoal = Column(String(20))
    contact_group_id = Column(Integer, ForeignKey('contact_group.id'))
    contact_group = relationship("ContactGroup")

    def __repr__(self):
        return self.nome