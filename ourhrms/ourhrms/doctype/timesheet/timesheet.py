from datetime import datetime
import frappe
from frappe.model.document import Document

class Timesheet(Document):
    def before_submit(self):
        """Calculate total hours before submitting the timesheet."""
        if self.clock_in_time and self.clock_out_time:
            self.total_hours = calculate_total_hours(self.clock_in_time, self.clock_out_time)
            frappe.msgprint(f"Total Hours Worked: {self.total_hours}")  # Notify user
            print("Total hours:", self.total_hours)  # Debugging in logs

def calculate_total_hours(clock_in, clock_out):
    """Calculate total hours between clock-in and clock-out times."""
    if not clock_in or not clock_out:
        return 0  # Return 0 if any field is missing

    # Convert string to datetime
    clock_in_dt = datetime.strptime(clock_in, "%H:%M:%S")
    clock_out_dt = datetime.strptime(clock_out, "%H:%M:%S")

    total_hours = (clock_out_dt - clock_in_dt).total_seconds() / 3600  # Convert to hours
    return round(total_hours, 2)


# def calculate_total_hours(clock_in, clock_out):
# 		"""Calculate total hours between clock-in and clock-out times."""
# 		if not clock_in or not clock_out:
# 			return 0  # If any field is missing, return 0

# 		clock_in_dt = datetime.strptime(clock_in, "%Y-%m-%d %H:%M:%S")
# 		clock_out_dt = datetime.strptime(clock_out, "%Y-%m-%d %H:%M:%S")

# 		total_hours = (clock_out_dt - clock_in_dt).total_seconds() / 3600  # Convert seconds to hours
# 		return round(total_hours, 2)
