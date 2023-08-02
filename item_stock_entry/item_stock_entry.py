# Copyright (c) 2023, stanch and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe import _

class Item_StockEntry(Document):
    @frappe.whitelist()
    def export_items(self):
        orgnl = frappe.db.get_value('items',{'name':self.item_name},['quantity'])
        if orgnl < self.quantity:
            frappe.throw(_('The available quantity of {0} is {1}, so kindly take available quantity.').format(self.quantity, orgnl))
        else:
            stock_entry = frappe.new_doc("Stock_Entry")
            stock_entry.type = self.select
            stock_entry.item_name = self.item_name
            stock_entry.time = self.time
            stock_entry.from_warehouse = self.from_warehouse
            stock_entry.to_warehouse = self.to_warehouse
            stock_entry.quantity = self.quantity
            stock_entry.movement_id = self.movement_id
            stock_entry.insert()
            frappe.db.commit()
        frappe.msgprint("Exported Successfully..!")
        after = float(orgnl)-float(self.quantity)
        frappe.db.set_value("items",self.item_name,'quantity',after)

    @frappe.whitelist()
    def refill_item(self):
        orgnl = frappe.db.get_value('items',{'name':self.item_name},['quantity'])
        stock_entry = frappe.new_doc("Stock_Entry")
        stock_entry.type = self.select
        stock_entry.quantity = self.quantity
        stock_entry.warehouse_name = self.warehouse_name
        stock_entry.movement_id = self.movement_id
        stock_entry.item_name = self.item_name
        stock_entry.insert()
        frappe.db.commit()
        frappe.msgprint("Imported Successfully..!")
        aft = float(orgnl)+float(self.quantity)
        frappe.db.set_value("items",self.item_name,'quantity',aft)



        



        