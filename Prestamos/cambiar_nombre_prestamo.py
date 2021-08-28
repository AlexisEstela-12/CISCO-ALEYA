import os
from posixpath import join
from uuid import uuid4


def path_and_rename(instance,filename):
    upload_to = 'PERU/guias_entrada'
    ext = filename.split('.')[-1]

    if instance.codigo_prestamo:
        filename = 'Guia entrada {}.{}'.format(instance.codigo_prestamo, ext)
    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to,filename)

def path_and_rename_CR(instance,filename):
    upload_to = 'COSTA RICA/guias_entrada'
    ext = filename.split('.')[-1]

    if instance.codigo_prestamo:
        filename = 'Guia entrada {}.{}'.format(instance.codigo_prestamo, ext)

    else:
        filename = '{}.{}'.format(uuid4().hex, ext)
    return os.path.join(upload_to,filename)