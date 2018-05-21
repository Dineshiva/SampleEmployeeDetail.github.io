from odoo import models, fields, api


class List(models.Model):
    _name = 'employeedetail.list'

    name = fields.Char(string="Name", required=True)
    email = fields.Char(string="Email", index=True)
    team = fields.Text()


class List(models.Model):
    _name = 'employeedetail.secondlist'

    secondname = fields.Char(string="SecondName")
    phoneno = fields.Integer(string="PhoneNo.")
    photo = fields.Binary(string="Image", help="Select image here")
