app_name = "program_management"
app_title = "Program Management"
app_publisher = "Kushika"
app_description = "program management"
app_email = "kushi@gmail.com"
app_license = "mit"
# required_apps = []

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/program_management/css/program_management.css"
# app_include_js = "/assets/program_management/js/program_management.js"



# include js, css files in header of web template
# web_include_css = "/assets/program_management/css/program_management.css"
# web_include_js = "/assets/program_management/js/program_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "program_management/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"doctype" : "program_management/program/management/program_management/customization/item_sum.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "program_management/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
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
# 	"methods": "program_management.utils.jinja_methods",
# 	"filters": "program_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "program_management.install.before_install"
# after_install = "program_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "program_management.uninstall.before_uninstall"
# after_uninstall = "program_management.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "program_management.utils.before_app_install"
# after_app_install = "program_management.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "program_management.utils.before_app_uninstall"
# after_app_uninstall = "program_management.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "program_management.notifications.get_notification_config"

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

override_doctype_class = {
	"Sales Order": "program_management.override.CustomSO"
}

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# "*": {
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method"
	# }
    "Customer":{
        "validate": "program_management.program_management.customization.anniversary.validate"
	},
    "Item": {
        "validate": "program_management.program_management.customization.item_sum.calculate_total_cost"
    },
    "Purchase Order": {
        "on_submit": "program_management.program_management.customization.purchase_mail.send_notification_email"
    }
}
test = {
    "test_1": "program_management/program_management/customization/test.py",
    "test_2": "program_management/program_management/customization/test_with_data.py",
}

# Scheduled Tasks
# ---------------

scheduler_events = {
	# "all": [
	# 	"program_management.tasks.all"
	# ],
	# "daily": [
	# 	"program_management.tasks.daily"
	# ],
	# "hourly": [
	# 	"program_management.tasks.hourly"
	# ],
	# "weekly": [
	# 	"program_management.tasks.weekly"
	# ],
	# "monthly": [
	# 	"program_management.tasks.monthly"
	# ],
	"cron": {
        "*/30 * * * *": [
            "program_management.program_management.doctype.myschedule.myschedule.update_counter"
        ]
    }
}

# Testing
# -------

# before_tests = "program_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "program_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "program_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["program_management.utils.before_request"]
# after_request = ["program_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["program_management.utils.before_job"]
# after_job = ["program_management.utils.after_job"]

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
# 	"program_management.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

