import csv
from django.http import HttpResponse

def export_to_csv(queryset, filename, fields, related_fields=None):
    """
    Exporta un queryset a un archivo CSV.
    :param queryset: Queryset de Django con los datos.
    :param filename: Nombre del archivo CSV resultante.
    :param fields: Lista de campos directos a exportar.
    :param related_fields: Diccionario con los campos relacionados a exportar {campo: "campo_relacionado"}.
    """
    related_fields = related_fields or {}
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{filename}.csv"'

    writer = csv.writer(response)

    # Encabezados
    header = fields + list(related_fields.values())
    writer.writerow(header)

    # Filas
    for obj in queryset:
        row = [getattr(obj, field) for field in fields]  # Campos directos
        for field, related_field in related_fields.items():
            related_obj = getattr(obj, field)  # Obtener el objeto relacionado
            row.append(getattr(related_obj, related_field) if related_obj else None)
        writer.writerow(row)

    return response

