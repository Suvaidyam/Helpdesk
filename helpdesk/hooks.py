app_name = "helpdesk"
app_title = "Helpdesk"
app_publisher = "Frappe Technologies"
app_description = "Customer Service Software"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "hello@frappe.io"
from frappe.utils.background_jobs import enqueue
app_license = "AGPLv3"

before_install = "helpdesk.setup.install.before_install"
after_install = "helpdesk.setup.install.after_install"
after_migrate = "helpdesk.search.build_index_in_background"

scheduler_events = {
    "all": ["helpdesk.search.build_index_if_not_exists"],
    "cron": {
        "* * * * *": [
            "helpdesk.helpdesk.doctype.hd_ticket.hd_ticket.auto_assignAgent"
        ]
    }
}


# def scheduler_events():
#     enqueue("helpdesk.doctype.hd_ticket.hd_ticket.call_function", queue='long', timeout=1),

website_route_rules = [
	{
		"from_route": "/helpdesk/<path:app_path>",
		"to_route": "helpdesk",
	},
]

doc_events = {
	"Contact": {
		"before_insert": "helpdesk.helpdesk.hooks.contact.before_insert",
	},
	"Assignment Rule": {
		"on_trash": "helpdesk.overrides.on_assignment_rule_trash",
	},
}

has_permission = {
	"HD Ticket": "helpdesk.helpdesk.doctype.hd_ticket.hd_ticket.has_permission",
}

permission_query_conditions = {
	"HD Ticket": "helpdesk.helpdesk.doctype.hd_ticket.hd_ticket.permission_query",
}

ignore_links_on_delete = [
	"HD Notification",
]
