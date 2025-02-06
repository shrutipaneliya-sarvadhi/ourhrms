from datetime import datetime
import frappe
from frappe.model.document import Document
from frappe.utils.data import now_datetime
import pytz

class Timesheet(Document):
    def before_insert(self):
        print("before_insert callingggggggggggggggggggggggg")
        if self.clock_out_time == 0:
            self.clock_out_time = '0:00:00'


    def on_submit(self):
        print("on_submit is being called")

        # Capture the current UTC time when the submit button is clicked using now_datetime
        utc_time = now_datetime()

        print("utc yimeeeeeeeeeeeee:",utc_time)

        # Convert the UTC time to your local timezone (e.g., 'Asia/Kolkata')
        local_tz = pytz.timezone('Asia/Kolkata')  # Replace with your local timezone
        local_time = utc_time.astimezone(local_tz)

        # Assign the converted time to clock_out_time
        self.clock_out_time = local_time.strftime('%H:%M:%S')

        # Log the captured and converted time (optional for debugging)
        print("Captured and converted clock_out_time:", self.clock_out_time)

    # def on_submit(self):
    #     print("on_submit is being called")

    #     # Capture the current time when the submit button is clicked
    #     self.clock_out_time = datetime.now().strftime("%H:%M:%S.%f")

    #     # Log the captured time (optional for debugging)
    #     print("Captured clock_out_time:", self.clock_out_time)

    #     # Make sure the clock_out_time field is being updated correctly
    #     if isinstance(self.clock_out_time, str):
    #         try:
    #             # Parse the time to make sure it's in the correct format (optional)
    #             self.clock_out_time = datetime.strptime(self.clock_out_time, "%H:%M:%S.%f")
    #             print("Parsed clock_out_time:", self.clock_out_time)
    #         except ValueError:
    #             print("Error: clock_out_time format is incorrect.")

        # Call the parent method to ensure all necessary submit actions are completed
   #     super().on_submit()
    
    # def on_submit(self):
    #     print("on_submit callingggggggggggggggggggggggg")
    #     # Set the clock_out_time to the current time before submission
    #     if self.clock_out_time == 0:
    #         self.clock_out_time = frappe.utils.now_datetime()

    #      # Ensure that clock_out_time is a datetime object
    #     if isinstance(self.clock_out_time, str):
    #         self.clock_out_time = datetime.strptime(self.clock_out_time, "%Y-%m-%d %H:%M:%S")

    #     # Convert UTC to Local Time using pytz
    #     local_timezone = pytz.timezone(frappe.get_site_config().get('timezone', 'Asia/Kolkata'))  # Default to 'Asia/Kolkata'

    #     # Convert UTC time to local time
    #     utc_time = self.clock_out_time.replace(tzinfo=pytz.UTC)

    #     # Convert UTC time to local time
    #     local_time = utc_time.astimezone(local_timezone)

    #     # Format the local time to match your desired format
    #     self.clock_out_time = local_time.strftime("%Y-%m-%d %H:%M:%S")

    #     # Commit the changes to the database
    #     frappe.db.commit()

                # def before_submit(self):
    #     # Ensure the record exists before updating
    #     if self.name:
    #         # Set the clock_out_time to the current timestamp
    #         self.clock_out_time = frappe.utils.now_datetime()
    #         print("clock_out_time:", self.clock_out_time)


    # def before_submit(self):
    #     """Calculate total hours before submitting the timesheet."""
    #     if self.clock_in and self.clock_out:
    #         self.total_hours = calculate_total_hours(self.clock_in, self.clock_out)
    #         frappe.msgprint(f"Total Hours Worked: {self.total_hours}")  # Notify user
    #         print("Total hours:", self.total_hours)  # Debugging in logs

    # def calculate_hours(clock_in, clock_out):
    #     """Calculate total hours between clock-in and clock-out times."""
    #     if not clock_in or not clock_out:
    #         return 0  # Return 0 if any field is missing

    #     try:
    #         # Adjust the format to include microseconds
    #         clock_in_dt = datetime.strptime(clock_in, "%H:%M:%S.%f")  # Include microseconds
    #         clock_out_dt = datetime.strptime(clock_out, "%H:%M:%S.%f")  # Include microseconds

    #         # Calculate the total duration in hours
    #         hours = (clock_out_dt - clock_in_dt).total_seconds() / 3600  # Convert to hours
    #         print("hourssssssssssssssssss:".total_hours)
    #         return round(hours, 2)
    #     except ValueError as e:
    #        frappe.throw(f"Error parsing datetime: {str(e)}")

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
