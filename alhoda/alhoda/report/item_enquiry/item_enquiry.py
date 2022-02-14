# Copyright (c) 2013, Syed Malik Ali and contributors
# For license information, please see license.txt

import frappe

def execute(filters=None):
	return get_columns(),get_data(filters)
def get_data(filters):
	print(f"\n\n\n{filters}\n\n\n")

	data = frappe.db.sql("""SELECT item_code,warehouse,actual_qty,reserved_qty,format(valuation_rate,2)  from `tabBin`;""")
	return data
def get_columns():
	return[
		"Item Code:Link/bin:100",
		"Warehouse:Data/warehouse:150",
		"Current Stock:Data/actual_qty:150",
		"Reseved Qty:reserved_qty:150",
		"Avg.Cost:valuation_rate:150",
	]
