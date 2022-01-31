// Copyright (c) 2022, Syed Malik Ali and contributors
// For license information, please see license.txt

frappe.ui.form.on('Item Enquiry', {
	// refresh: function(frm) {
item_code:function(frm){
  //self.sql()
  frm.set_value('item_name',"Malik")
//for d in data:
let row = frm.add_child('wh_details',{
  //wh:d.warehouse,
  //cur_qty:d.actual_qty
})
refresh_field('wh_details')
}


	// }
});
