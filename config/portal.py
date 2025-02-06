from frappe import _

def get_data():
    return [
        {
            "category": _("HR Management"),
            "icon": "fa fa-user",
            "label": _("My Leave Applications"),
            "route": "/leave-applications",
            "type": "page",
        },
    ]
