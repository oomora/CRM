from io import BytesIO
import os
import urllib2
from PIL import Image

from django.http.response import HttpResponse

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib.units import cm
from reportlab.lib import colors


from django.conf import settings

#from django.contrib.auth.models import User
from products.models import ProductRegister

# Create your views here.
def UserReport(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] ='attachment; filename=PDF-Report.pdf'

    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer,pagesize=A4)
    c = canvas.Canvas(buffer, pagesize=A4)
    report=[]

    data = [[0, 1, 2, 3],
            [4, 5, 6, 7,],
            [8, 9,10, 11],
            [12,13, 14, 15]
            ]
    t = Table(data, style=[
        ('GRID', (0, 0), (-1, -1), 0.5, colors.grey),
        ('GRID', (1, 1), (-2, -2), 1, colors.green),
        ('BOX', (0, 0), (1, -1), 2, colors.red),
        ('BOX', (0, 0), (-1, -1), 2, colors.black),
        ('LINEABOVE', (1, 2), (-2, 2), 1, colors.blue),
        ('LINEBEFORE', (2, 1), (2, -2), 1, colors.pink),
        ('BACKGROUND', (0, 0), (0, 1), colors.pink),
        ('BACKGROUND', (1, 1), (1, 2), colors.lavender),
        ('BACKGROUND', (2, 2), (2, 3), colors.orange),
    ])
    report.append(t)

    user_list = ProductRegister.objects.all().order_by('id')

    #Creation of the report header.
    c.setLineWidth(0.3)
    c.setFont('Helvetica', 20)
    c.drawString(10,750, 'Servipumps S.A. de C.V.')
    c.setFont('Helvetica', 14)
    c.drawString(10,735, 'Reporte de Productos')

    header(c)

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
    report.append(c)
    c.showPage()
    c.save()

    doc.build(report)
    pdf = buffer.getvalue()
    buffer.close()
    response.write(pdf)
    return response

def header( canvas ):
    header_element = []
    canvas.setFont("Helvetica", 16)
    label =canvas.drawString(230, 790, u"Reporte de Usuarios")



    imageFile = (os.path.join(settings.MEDIA_ROOT,'logo-contactoERPNext.jpg'))
    if os.path.exists(imageFile):
        # The image is located from the bottom of the page to the top
        canvas.drawImage(imageFile, 10,775,mask=None)
        #canvas.rect(10, 735, 560, 100,1,0)
        #canvas.rect(450,735, 90, 100, 1, 0)

        #header_element.append(im)
    else:
        print 'Image not found!.'

    #header_element.append(label)


    #header_table= Table(header_element, colWidths=[2 * cm, 5 * cm, 5 * cm, 5 * cm])
    #header_table = Table(header_element)
    #header_table.setStyle(TableStyle([
    #                                    ("BOX", (0, 0), (-1, -1), 0.25, colors.black),
    #                                   ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.black)])
    #)



