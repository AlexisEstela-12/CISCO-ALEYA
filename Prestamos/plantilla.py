from ProyectoLab.settings import MEDIA_ROOT_DOCU
from ProyectoLab.settings import MEDIA_ROOT_SAVE_PERU
from docxtpl import DocxTemplate
from django.shortcuts import render



def funcion_Peru(doc_name,context):

    base_url = MEDIA_ROOT_DOCU 
    asset_url = base_url / 'Template Prestamo PERU.docx'
    tp1 = DocxTemplate(asset_url)
    tp1.render(context)
    name = "Guia_de_Prestamo_equipo_{}.docx".format(doc_name)
    place_to_save = MEDIA_ROOT_SAVE_PERU /name
    tp1.save(place_to_save)
    return place_to_save




