import csv
import itertools

from django.views import generic
from django.http import StreamingHttpResponse
from django.db.models import Min, Max, Prefetch
from web_site import models


class PseudoBuffer(object):
    def write(self, value):
        return value


class CustomerExport(generic.View):
    # количество записей, обрабатываемых за итерацию
    EXPORT_BATCH_SIZE = 3000

    def make_csv_rows(self, start_id, end_id, batch_size):
        for i in range(start_id, end_id, batch_size):
            # проходимся по таблице окном фиксированного размера batch_size
            # этим ограничиваем кол-во объектов Customer, одновременно находящихся в памяти
            sub_qs = models.Customer.objects.filter(pk__gt=i - 1, pk__lte=i + batch_size)
            phone_prefetcher = Prefetch('phones', to_attr='phone_numbers')
            email_prefetcher = Prefetch('emails', to_attr='email_addresses')
            sub_qs = sub_qs.prefetch_related(email_prefetcher, phone_prefetcher)
            for customer in sub_qs:
                phones = [x.number for x in customer.phone_numbers]
                emails = [x.address for x in customer.email_addresses]
                for pair in itertools.zip_longest(emails, phones, fillvalue=''):
                    yield [customer.id, customer.first_name, customer.last_name, pair[0], pair[1]]

    def get(self, *args, **kwargs):
        batch_size = self.EXPORT_BATCH_SIZE
        pseudo_buffer = PseudoBuffer()
        writer = csv.writer(pseudo_buffer, delimiter=';')
        tmp = models.Customer.objects.all().aggregate(min_id=Min('pk'), max_id=Max('pk'))
        rows = self.make_csv_rows(tmp['min_id'], tmp['max_id'], batch_size)
        response = StreamingHttpResponse((writer.writerow(row) for row in rows), content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename="customers.csv"'
        return response



