# Copyright (c) 2024, Kushika and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class CRUD(Document):
	def validate(self):
		if self.display_full_name and self.first_name and self.last_name:
			self.full_name=f"{self.first_name} {self.last_name}"



