// Copyright (c) 2023, stanch and contributors
// For license information, please see license.txt

frappe.ui.form.on('Item_Stock Entry', {
	refresh: function(frm) {
		frm.disable_save();
	},
		export_item(frm) {	

			frm.call('export_items').then(r =>{	
			})	
	
	},	
		refill_item(frm){	
			frm.call('refill_item').then(r =>{	
			})	
		}
	}
	);
