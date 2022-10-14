from django.views.generic import View, TemplateView
from django.shortcuts import render

from .scripts import get_room_status_data


class DashboardListview(TemplateView):
    template_name = "dashboard/dashboard_list.html"

    def get(self, request):
        return render(request, self.template_name, {})


class DashboardTemplateView(View):
    template_name = "dashboard/template_x.html"

    def get(self, request, *args, **kwargs):
        # Get the template id from the url
        template_id = kwargs.get("id")
        # update template name with id
        self.template_name = self.template_name.replace("x", str(template_id))
        data = get_room_status_data()
        if "floor" in data:
            return render(request, self.template_name, data)
        else:
            return render(request, self.template_name, data)