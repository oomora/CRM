from io import BytesIO
import os
import urllib2
from PIL import Image


from django.http.response import HttpResponse

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

from django.conf import settings

#from django.contrib.auth.models import User
from products.models import ProductRegister

# Create your views here.
def UserReport(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] ='attachment; filename=PDF-Report.pdf'

    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)

    user_list = ProductRegister.objects.all().order_by('id')

    #Creation of the report header.
    c.setLineWidth(0.3)
    c.setFont('Helvetica', 20)
    c.drawString(10,750, 'Servipumps S.A. de C.V.')
    c.setFont('Helvetica', 14)
    c.drawString(10,735, 'Reporte de Productos')
    c.line(10,730,250,730)

    i = 10
    id = 1
    c.setFont('Helvetica', 10)
    for u in user_list:
        c.drawString(10,700-i, str(id))
        c.drawString(50,700-i, u.nombre)
        c.drawString(150,700-i, u.descripcion)
        c.drawString(250,700-i,u.email)
        i+=10
        id+=1

    c.rect(100,100,200, 200, stroke=1, fill=0)
    c.drawImage('BombaLogo.jpg', 10,10, width=None,height=None,mask=None)

    c.showPage()
    c.save()
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response