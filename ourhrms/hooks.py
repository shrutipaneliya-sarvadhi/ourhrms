

app_name = "ourhrms"
app_title = "ourhrms"
app_publisher = "sarvadhi"
app_description = "ourhrms"
app_email = "connect@sarvadhi.com"
app_license = "mit"


fixtures = [
    { "dt": "Web Page"   },
    { "dt": "Website Sidebar" },
    { "dt": "Website Theme" }

]


# import frappe

# def get_home_page(user):
#     """Redirect users based on their role"""
#     if "Employee" in frappe.get_roles(user):
#         return "/employee"
#     return "/"

# get_website_user_home_page = "ourhrms.hooks.get_home_page"

# Link the login event to the new on_login function
# on_login = "ourhrms.api.on_login"

# home_page = "login"  # Default page for non-logged-in users

# role_home_page = {
#     "Employee": "employee"  # Redirect Employee role users to portal page
# }

# after_login = "ourhrms.api.redirect_after_login"

# # Set the function in the hooks
# website_redirects = {
#     "get_website_user_home_page": "ourhrms.hooks.get_home_page"
# }
# app_include_js = "/assets/ourhrms/js/leave.js"



# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "ourhrms",
# 		"logo": "/assets/ourhrms/logo.png",
# 		"title": "ourhrms",
# 		"route": "/ourhrms",
# 		"has_permission": "ourhrms.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/ourhrms/css/ourhrms.css"
# app_include_js = "/assets/ourhrms/js/ourhrms.js"

# include js, css files in header of web template
# web_include_css = "/assets/ourhrms/css/ourhrms.css"
# web_include_js = "/assets/ourhrms/js/ourhrms.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "ourhrms/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "ourhrms/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
role_home_page = {
    "Employee": "employee"
}


# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page",
#     "Employee":"employee/index.html"
# }
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "ourhrms.utils.jinja_methods",
# 	"filters": "ourhrms.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "ourhrms.install.before_install"
# after_install = "ourhrms.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "ourhrms.uninstall.before_uninstall"
# after_uninstall = "ourhrms.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "ourhrms.utils.before_app_install"
# after_app_install = "ourhrms.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "ourhrms.utils.before_app_uninstall"
# after_app_uninstall = "ourhrms.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "ourhrms.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"ourhrms.tasks.all"
# 	],
# 	"daily": [
# 		"ourhrms.tasks.daily"
# 	],
# 	"hourly": [
# 		"ourhrms.tasks.hourly"
# 	],
# 	"weekly": [
# 		"ourhrms.tasks.weekly"
# 	],
# 	"monthly": [
# 		"ourhrms.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "ourhrms.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "ourhrms.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "ourhrms.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["ourhrms.utils.before_request"]
# after_request = ["ourhrms.utils.after_request"]

# Job Events
# ----------
# before_job = ["ourhrms.utils.before_job"]
# after_job = ["ourhrms.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"ourhrms.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

