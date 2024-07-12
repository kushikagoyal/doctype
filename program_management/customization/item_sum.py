import frappe
from frappe.model.document import Document

def calculate_total_cost(doc, method):
    for item in doc.custom_item_child:
        if item.quantity and item.unit_cost:
            item.total_cost = item.quantity * item.unit_cost