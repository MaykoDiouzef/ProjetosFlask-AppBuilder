# class MyView(BaseView):

#     default_view = 'method1'

#     @expose('/method1/')
#     @has_access
#     def method1(self):
#         # do something with param1
#         # and return to previous page or index
#         return 'Hello'

#     @expose('/method2/<string:param1>')
#     @has_access
#     def method2(self, param1):
#         # do something with param1
#         # and render template with param
#         param1 = 'Goodbye %s' % (param1)
#         return param1
    
#     @expose('/method3/<string:param1>')
#     @has_access
#     def method3(self, param1):
#         # do something with param1
#         # and render template with param
#         param1 = 'Goodbye %s' % (param1)
#         self.update_redirect()
#         return self.render_template('method3.html', param1=param1)

# appbuilder.add_view(MyView, "Method1", category='Minha View')
# appbuilder.add_link("Method2", href='/myview/method2/Mayko', category='Minha View')
# appbuilder.add_link("Method3", href='/myview/method3/Diouzef', category='Minha View')


# class MyFormView(SimpleFormView):
#     form = MyForm
#     form_title = "This is my first form view"
#     message = "My form was submitted"

#     def form_get(self, form):
#         form.field1.data = "This was prefilled"

#     def form_post(self, form):
#         # post process form
#         flash(self.message, "info")


# appbuilder.add_view(
#     MyFormView,
#     "My form View",
#     icon="fa-group",
#     label=_("My form View"),
#     category="My Forms",
#     category_icon="fa-cogs",
# )