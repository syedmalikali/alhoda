// Copyright (c) 2016, Syed Malik Ali and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Item Enquiry"] = {
	"filters": [
				{
					"fieldname":"item_code",
					"label":__("Item Code"),
					"fieldtype":"Link",
					"options":"Item",
					"width":100,
					"reqd":0,
				}
	]
};
