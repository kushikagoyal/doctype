# Copyright (c) 2024, Kushika and contributors
# For license information, please see license.txt

import frappe


def execute(filters=None):
	columns=[{
		"fieldname":"first_num",
		"label":"First Num",
		"fieldtype":"Int"
	},{
		"fieldname":"second_num",
		"label":"Second Num",
		"fieldtype":"Int"
	},{
		"fieldname":"sum",
		"label":"Sum",
		"fieldtype":"Int"
	},
	
	]
	data=frappe.get_all(
		"MySum",
		fields=["sum","first_num","second_num"]
	)
	return columns, data
