from django.shortcuts import render

from django.shortcuts import render
from pyecharts import options as opts
from pyecharts.charts import Line

def index(request):
    line_chart = (
        Line()
        .add_xaxis(["Jan", "Feb", "Mar", "Apr", "May"])
        .add_yaxis("Sales", [5, 20, 36, 10, 75])
        .set_global_opts(title_opts=opts.TitleOpts(title="Line Chart"))
    )
    line_chart.render("myapp/static/line_chart.html")
    return render(request, 'index.html')


# Create your views here.
