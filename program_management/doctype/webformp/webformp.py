# Copyright (c) 2024, Kushika and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class WebFormP(Document):
	def after_insert(self):
		self.notify_admin_on_creation()
	def notify_admin_on_creation(self):
		# admin_email = "kushikagoyal00@gmail.com"  # Replace with the actual admin email
		subject = f"New Task added: {"self.task_description"} {"self.task_time"}"
		message = f"""
        A new task has been created in the system:
        Description: {"self.task_description"} 
        time: {"self.task_time"}
        """
		print(frappe.sendmail(
            recipients="kushikagoyal00@gmail.com",
            subject= subject,
            message="message",
            delayed=False
        ))