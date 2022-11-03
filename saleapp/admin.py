from saleapp.models import Category, Product, UserRole
from flask_admin import Admin, expose, BaseView
from saleapp import db, app
from flask_admin.contrib.sqla import ModelView
from flask import redirect
from flask_login import logout_user, current_user


admin = Admin(app=app, name="Quản trị CSDL", template_mode='bootstrap4')


class AuthenticatedAdminView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN


class AuthenticatedView(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class AuthenticatedAdminViewBase(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == UserRole.ADMIN


class ProductModel(AuthenticatedAdminView):
    column_filters = ['name', 'description']
    column_searchable_list = ['name', 'description']
    can_export = True
    column_exclude_list = ['image']
    column_export_exclude_list = ['image']
    column_labels = {
        'name': 'Sản phẩm',
        'description': 'Mô tả',
        'price': 'Giá'
    }


class ReportModel(AuthenticatedAdminViewBase):
    @expose('/')
    def index(self):
        return self.render('admin/report.html')


class LogoutView(AuthenticatedView):
    @expose('/')
    def __index__(self):
        logout_user()
        return redirect("/admin")


admin.add_view(AuthenticatedAdminView(Category, db.session, name='Danh mục'))
admin.add_view(ProductModel(Product, db.session, name='Sản phẩm'))
admin.add_view(ReportModel(name='Report'))
admin.add_view(LogoutView(name="Đăng xuất"))
