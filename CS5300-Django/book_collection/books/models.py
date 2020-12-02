# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.template.defaultfilters import truncatechars


class Author(models.Model):
    author_id = models.AutoField(db_column='AUTHOR_ID', primary_key=True)  # Field name made lowercase.
    first_name = models.CharField(db_column='FIRST_NAME', max_length=511, blank=True, null=True)  # Field name made lowercase.
    last_name = models.CharField(db_column='LAST_NAME', max_length=511, blank=True, null=True)  # Field name made lowercase.
    about = models.CharField(db_column='ABOUT', max_length=8191, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    class Meta:
        managed = False
        db_table = 'AUTHOR'


class Binding(models.Model):
    binding_id = models.AutoField(db_column='BINDING_ID', primary_key=True)  # Field name made lowercase.
    binding_type = models.CharField(db_column='BINDING_TYPE', max_length=50, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.binding_type

    class Meta:
        managed = False
        db_table = 'BINDING'


class Book(models.Model):
    book_id = models.AutoField(db_column='BOOK_ID', primary_key=True)  # Field name made lowercase.
    title = models.CharField(db_column='TITLE', max_length=4096, blank=True, null=True)  # Field name made lowercase.
    publisher = models.ForeignKey('Publisher', models.DO_NOTHING, db_column='PUBLISHER_ID', blank=True, null=True)  # Field name made lowercase.
    publication_date = models.IntegerField(db_column='PUBLICATION_DATE', blank=True, null=True)  # Field name made lowercase.
    synopsis = models.TextField(db_column='SYNOPSIS', blank=True, null=True)  # Field name made lowercase.

    @property
    def short_title(self):
        return truncatechars(self.title, 50)

    def __str__(self):
        return self.short_title

    class Meta:
        managed = False
        db_table = 'BOOK'


class Copy(models.Model):
    copy_id = models.AutoField(db_column='COPY_ID', primary_key=True)  # Field name made lowercase.
    book = models.ForeignKey(Book, models.DO_NOTHING, db_column='BOOK_ID', blank=True, null=True)  # Field name made lowercase.
    binding = models.ForeignKey(Binding, models.DO_NOTHING, db_column='BINDING_ID', blank=True, null=True)  # Field name made lowercase.
    language_id = models.IntegerField(db_column='LANGUAGE_ID', blank=True, null=True)  # Field name made lowercase.
    grade = models.ForeignKey('Grade', models.DO_NOTHING, db_column='GRADE_ID', blank=True, null=True)  # Field name made lowercase.
    has_jacket = models.IntegerField(db_column='HAS_JACKET', blank=True, null=True)  # Field name made lowercase.
    edition = models.CharField(db_column='EDITION', max_length=511, blank=True, null=True)  # Field name made lowercase.
    isbn_10 = models.CharField(db_column='ISBN_10', max_length=10, blank=True, null=True)  # Field name made lowercase.
    isbn_13 = models.CharField(db_column='ISBN_13', max_length=13, blank=True, null=True)  # Field name made lowercase.
    price = models.DecimalField(db_column='PRICE', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    descr = models.CharField(db_column='DESCR', max_length=4096, blank=True, null=True)  # Field name made lowercase.
    signed = models.IntegerField(db_column='SIGNED', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'COPY'


class Grade(models.Model):
    grade_id = models.AutoField(db_column='GRADE_ID', primary_key=True)  # Field name made lowercase.
    label = models.CharField(db_column='LABEL', max_length=20, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.label

    class Meta:
        managed = False
        db_table = 'GRADE'


class Language(models.Model):
    language_id = models.AutoField(db_column='LANGUAGE_ID', primary_key=True)  # Field name made lowercase.
    language_code = models.CharField(db_column='LANGUAGE_CODE', max_length=2, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.language_code

    class Meta:
        managed = False
        db_table = 'LANGUAGE'


class Publisher(models.Model):
    publisher_id = models.AutoField(db_column='PUBLISHER_ID', primary_key=True)  # Field name made lowercase.
    publisher_name = models.CharField(db_column='PUBLISHER_NAME', max_length=511, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.publisher_name

    class Meta:
        managed = False
        db_table = 'PUBLISHER'


class WrittenBy(models.Model):
    book = models.OneToOneField(Book, models.DO_NOTHING, db_column='BOOK_ID', primary_key=True)  # Field name made lowercase.
    author = models.ForeignKey(Author, models.DO_NOTHING, db_column='AUTHOR_ID')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'WRITTEN_BY'
        unique_together = (('book', 'author'),)


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'
