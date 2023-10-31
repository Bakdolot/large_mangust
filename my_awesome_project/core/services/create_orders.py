import codecs
import csv

from django.core.cache import cache
from django.db import transaction

from my_awesome_project.core.models import Order


def gen_chunks(reader, chunksize=100):
    """
    Chunk generator. Take a CSV `reader` and yield
    `chunksize` sized slices.
    """
    chunk = []
    for i, line in enumerate(reader):
        if i % chunksize == 0 and i > 0:
            yield chunk
            del chunk[:]
        chunk.append(line)
    yield chunk


def save_orders(file):
    reader = csv.DictReader(codecs.iterdecode(file, "utf-8"))
    with transaction.atomic():
        for i in gen_chunks(reader):
            Order.objects.bulk_create([Order(**data) for data in i])
    if cache.has_key("/api/orders/create"):
        cache.delete("/api/orders/create")
    return {"Status": "OK"}
