from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views import generic
from django.utils import timezone
from datetime import timedelta, date

from dateutil.relativedelta import relativedelta

import datetime

from django.shortcuts import reverse
from .models import NewsItem, ScrapeHistory
from .forms import ScrapeForm
from .tasks import scrape_async


class ScrapeRecordListView(generic.FormView):
    template_name = "scrape-history.html"
    form_class = ScrapeForm

    def get_success_url(self):
        return reverse("scrape-history")

    def form_valid(self, form):
        scrape_async.delay()
        return super(ScrapeRecordListView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(ScrapeRecordListView, self).get_context_data(**kwargs)
        page = self.request.GET.get("page", 1)
        query_set = ScrapeHistory.objects.all()
        paginator = Paginator(query_set, 15)
        try:
            query_set = paginator.page(page)
        except PageNotAnInteger:
            query_set = paginator.page(1)
        except EmptyPage:
            query_set = paginator.page(paginator.num_pages)
        context.update({"object_list": query_set})
        return context




class NewsItemsListView(generic.ListView):
    model = NewsItem
    template_name = "news-item-list.html"
    paginate_by = 15

    def get_queryset(self):
        queryset = super().get_queryset()
    
        # Get filter values from request parameters
        filter_year = self.request.GET.get('filter_year')
        filter_month = self.request.GET.get('filter_month')
        filter_day = self.request.GET.get('filter_day')
        timeframe = self.request.GET.get('timeframe')

    
        # Apply filters
        if filter_year:
            queryset = queryset.filter(published_date__year=int(filter_year))
        if filter_month:
            queryset = queryset.filter(published_date__month=int(filter_month))
        if filter_day:
            queryset = queryset.filter(published_date__day=int(filter_day))
            
        if timeframe == 'last_week':
            last_week = datetime.date.today() - datetime.timedelta(days=7)
            queryset = queryset.filter(published_date__gte=last_week)
        elif timeframe == 'last_month':
            last_month = datetime.date.today() - relativedelta(months=1)
            queryset = queryset.filter(published_date__gte=last_month)
        elif timeframe == 'last_year':
            last_year = datetime.date.today() - relativedelta(years=1)
            queryset = queryset.filter(published_date__gte=last_year)

        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        total_count = self.model.objects.count()
        context["total_count"] = total_count
        # Add the day, month, and year options for the date filter
        today = datetime.date.today()
        context["days"] = range(1, 32)
        context["months"] = [
            (i, datetime.date(today.year, i, 1).strftime("%B")) for i in range(1, 13)
        ]
        context["years"] = range(today.year - 10, today.year + 1)
        return context
