# -*- coding=utf-8 -*-
# !/usr/bin/env python3


from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from app.models import User


class LoginForm(FlaskForm):
    username = StringField("Ім'я користувача", validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    remember_me = BooleanField("Запам'ятати мене")
    submit = SubmitField('Увійти')


class RegistrationForm(FlaskForm):
    username = StringField("Ім'я користувача", validators=[DataRequired()])
    email = StringField('Електронна пошта', validators=[
                        DataRequired(), Email()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    password2 = PasswordField(
        'Повторіть пароль', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Зареєструйтесь')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(
                "Будь ласка, використовуйте інше ім’я користувача.")

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError(
                'Будь ласка, використовуйте іншу електронну адресу.')


class EditProfileForm(FlaskForm):
    username = StringField("Ім'я користувача", validators=[DataRequired()])
    about_me = TextAreaField('Про мене', validators=[Length(min=0, max=140)])
    submit = SubmitField('Відправити')
