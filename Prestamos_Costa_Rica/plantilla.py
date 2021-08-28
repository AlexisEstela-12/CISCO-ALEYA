from ProyectoLab.settings import MEDIA_ROOT_DOCU
from ProyectoLab.settings import MEDIA_ROOT_SAVE_COSTA_RICA
from docxtpl import DocxTemplate




def funcion_Costa_Rica(doc_name,context):

    base_url = MEDIA_ROOT_DOCU 
    asset_url = base_url / 'Template Prestamo COSTA RICA.docx'
    tp1 = DocxTemplate(asset_url)
    tp1.render(context)
    name = "Guia_de_Prestamo_equipo_{}.docx".format(doc_name)
    place_to_save = MEDIA_ROOT_SAVE_COSTA_RICA /name
    tp1.save(place_to_save)
    return place_to_save
    

