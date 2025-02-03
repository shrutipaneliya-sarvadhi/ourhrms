# Copyright (c) 2025, sarvadhi and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class LeaveApplication(Document):
# 	pass

import frappe
from frappe.model.document import Document
from datetime import datetime, date

class LeaveApplication(Document):
    def before_insert(self):
        self.status = self.status or "Pending"

    def validate(self):
        self.calculate_total_days()

    def calculate_total_days(self):
        if self.from_date and self.to_date:
            # Handle both str and date types
            from_date = self.from_date if isinstance(self.from_date, date) else datetime.strptime(self.from_date, "%Y-%m-%d").date()
            to_date = self.to_date if isinstance(self.to_date, date) else datetime.strptime(self.to_date, "%Y-%m-%d").date()

            # Calculate the total days
            self.total_days = (to_date - from_date).days + 1
            print(f"Total Days Calculated: {self.total_days}")  