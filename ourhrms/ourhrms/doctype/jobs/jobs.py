# Copyright (c) 2025, sarvadhi and contributors
# For license information, please see license.txt

from os import name1
import frappe
from frappe.model.document import Document


class Jobs(Document):
	def create_timelog(date, total_hours, tasks):
		new_entry = frappe.get_doc({
        "doctype": "Jobs",
        "job_name": name1
        })
		new_entry.insert()
		frappe.db.commit()
		return new_entry