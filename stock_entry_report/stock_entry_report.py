# Copyright (c) 2023, stanch and contributors
# For license information, please see license.txt

# Copyright (c) 2023, stanch and contributors
# For license information, please see license.txt

import datetime
import frappe
import math
import frappe
import json
import requests
import openpyxl
from six import BytesIO
from frappe.utils import (
    flt,
    cint,
    cstr,
    get_html_format,
    get_url_to_form,
    gzip_decompress,
    format_duration,
    today
)
from datetime import timedelta, datetime
# from __future__ import unicode_literals
from six.moves import range
from six import string_types
import frappe
import json
from frappe.utils import getdate,get_time, cint, add_months, date_diff, add_days, nowdate, get_datetime_str, cstr, get_datetime, now_datetime, format_datetime
from datetime import datetime
from calendar import monthrange

from frappe import _, msgprint
from frappe.utils import flt
from frappe.utils import cstr, cint, getdate
# from __future__ import unicode_literals
from functools import total_ordering
from itertools import count,groupby
# import more_itertools
import frappe
from frappe import permissions
from frappe.utils import cstr, cint, getdate, get_last_day, get_first_day, add_days
from frappe.utils import cstr, add_days, date_diff, getdate, format_date,now
from math import floor
from frappe import msgprint, _
from calendar import month, monthrange
from datetime import date, timedelta, datetime,time
from six.moves import range
from six import string_types
import frappe
import json
from frappe.utils import getdate, cint, add_months, date_diff, add_days, nowdate, get_datetime_str, cstr, get_datetime, now_datetime, format_datetime
from datetime import datetime
from calendar import monthrange
from frappe import _, msgprint
from frappe.utils import flt
from frappe.utils import cstr, cint, getdate
# from __future__ import unicode_literals
from functools import total_ordering
from itertools import count
import frappe
from frappe import permissions
from frappe.utils import cstr, cint, getdate, get_last_day, get_first_day, add_days
from frappe.utils import cstr, add_days, date_diff, getdate, format_date
from math import floor
from frappe import msgprint, _
from calendar import month, monthrange
from datetime import date, timedelta, datetime,time
from frappe.utils.data import add_days, getdate,date_diff
import datetime as dt
from datetime import datetime


def execute(filters=None):
    columns, data = [], []
    columns = get_columns(filters)
    data = get_data(filters)
    return columns, data

def get_columns(filters):
    column = [
    _('Type') + ':Data:150',
    _('Item Name') + ':Data:150',
    _('Time') + ':Time:180',
    _('From Warehouse') + ': Data:140',
    _('To Warehouse') + ':Data:90',
    _('Type Quantity') + ': Data:110',
    _('Movement ID') + ':Data:120',
    _('Item MRP') + ': Currency:110',
    _('Toatl Quantity') + ': Int:110',

    ]
    return column

def get_data(filters):
    data = []
    record = frappe.db.get_all("Stock_Entry",['*'])
    rcd = frappe.db.get_all("items",['*'])
    for r in record:
        qty = frappe.db.get_value('items',{'name':r.item_name},['Quantity'])
        mrp = frappe.db.get_value('items',{'name':r.item_name},['mrp'])
        frappe.errprint(qty)
        row = [r.type,r.item_name,r.time,r.from_warehouse,r.to_warehouse,r.quantity,r.movement_id,mrp,qty]
        data.append(row)
    return data