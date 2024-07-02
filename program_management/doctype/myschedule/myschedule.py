# Copyright (c) 2024, Kushika and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class myschedule(Document):
	# def scheduled_task(self):
	# 	self.counter=self.counter+1
	# 	print("This task runs every half hour")
	pass

@frappe.whitelist()
def update_counter():
		schedules = frappe.get_all('myschedule', filters={})
              
		for schedule in schedules:
			doc = frappe.get_doc('myschedule', schedule.name)
			doc.counter = doc.counter + 1
			doc.save()
			frappe.db.commit()
			print("Counter updated for all myschedule documents")
			return doc.counter
		

