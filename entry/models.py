from django.db import models

class Entry(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    Lab_incharge_name = models.CharField(max_length=50)
    productid = models.CharField(max_length=20)
    part_name = models.CharField(max_length=50)



    SERVICE = 'SERVICE'
    NEW_ORDER = 'NEW ORDER'
    SERVICETYPE = (
        (SERVICE, 'SERVICE'),
        (NEW_ORDER, 'NEW ORDER'),
    )

    service_type = models.CharField(
        max_length=10,
        choices=SERVICETYPE,
        default=SERVICE,
    )

    """
    LAB1 = 'LAB1',
    LAB2 = 'LAB2',
    LAB3 = 'LAB3',
    LAB4 = 'lb4',
    LAB5 = 'LAB5',
    LAB6 = 'LAB6',
    LAB7 = 'LAB7',
    LAB8 = 'LAB8',
    LAB9 = 'LAB9', 
    Labnumber = (
        (LAB1, 'LAB1'),
        (LAB2, 'LAB2'),
        (LAB3, 'LAB3'),
        (LAB4, 'LAB4'),
        (LAB5, 'LAB5'),
        (LAB6, 'LAB6'),
        (LAB7, 'LAB7'),
        (LAB8, 'LAB8'),
        (LAB9, 'LAB9'),
    )

    lab_number = models.CharField(
        max_length=5,
        choices=Labnumber,
        default=LAB1,
    )"""

    lab_number = models.DecimalField(decimal_places=0, max_digits=2)

    timestamp = models.DateTimeField()


    def __str__(self):
        return self.title