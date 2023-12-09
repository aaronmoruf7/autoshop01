# forms.py
from wtforms import (
    Form,
    StringField,
    PasswordField,
    validators,
    DecimalField,
    SubmitField,
    DateField,
)
from wtforms.validators import DataRequired
from flask_wtf import FlaskForm


class RegistrationForm(Form):
    username = StringField("Username", [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])
    confirm_password = PasswordField("Password (again)", [validators.DataRequired()])


class LoginForm(Form):
    username = StringField("Username", [validators.DataRequired()])
    password = PasswordField("Password", [validators.DataRequired()])


class ChangePasswordForm(Form):
    old_password = PasswordField("Old Password", [validators.DataRequired()])
    new_password = PasswordField(
        "New Password",
        [
            validators.DataRequired(),
            validators.Length(
                min=8, message="Password must be at least 8 characters long"
            ),
            validators.EqualTo("confirm_password", message="Passwords must match"),
        ],
    )
    confirm_password = PasswordField("Confirm Password", [validators.DataRequired()])


class IncomeForm(FlaskForm):
    description = StringField("Description", validators=[DataRequired()])
    amount = DecimalField("Amount", validators=[DataRequired()])
    date = DateField("Date", format="%Y-%m-%d", validators=[DataRequired()])
    submit = SubmitField("Add Income")


class ExpenseForm(FlaskForm):
    description = StringField("Description", validators=[DataRequired()])
    amount = DecimalField("Amount", validators=[DataRequired()])
    date = DateField("Date", format="%Y-%m-%d", validators=[DataRequired()])
    submit = SubmitField("Add Expense")


class CustomerForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    number = StringField("Number", validators=[DataRequired()])
    email = StringField("Email")
    address = StringField("Address")
    submit = SubmitField("Add Customer")


class EditCustomerForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired()])
    number = StringField("Number", validators=[DataRequired()])
    email = StringField("Email")
    address = StringField("Address")
    submit = SubmitField("Save Changes")
