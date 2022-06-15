from ast import Return
from json import load
from django.shortcuts import render
from django.http import HttpResponse
from App.models import Mama, Padrasto, Hermana
from django.template import loader

def mama(self):
    mama = Mama(nombre='Mariela', apodo ='Mamucha', edad = '43', cumple='1978/07/26')
    mama.save
    plantilla = loader.get_template("T1.html")
    documento = plantilla.render({"mama": mama})
    return HttpResponse(documento)

def padrastro(self):
    padrastro = Padrasto(nombre='Alfredo', apodo='Gatito', edad='45', cumple='1977/05/27')
    padrastro.save
    plantilla = loader.get_template("T2.html")
    documento = plantilla.render({"padrastro": padrastro})
    return HttpResponse(documento)

def hermana(self):
    hermana = Hermana(nombre='Candela', apodo='Petisa', edad='19', cumple='2003/06/05')
    hermana.save
    plantilla = loader.get_template("T3.html")
    documento = plantilla.render({"hermana": hermana})
    return HttpResponse(documento)