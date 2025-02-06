# Copyright (c) 2025, hr and contributors
# For license information, please see license.txt
 
# import frappe
import frappe
from frappe.model.document import Document
from frappe.utils.file_manager import save_file
from frappe.utils.pdf import get_pdf
from datetime import datetime

 
class Payslip(Document):
    def on_submit(doc):
        print("email sending...")
        print("send_payslip_report calling...")
        try:
            # Get the employee record linked to this payslip
            employee = frappe.get_doc("Employee", doc.employee)  # 'employee' field in Payslip
            
            if employee and employee.email:
                # Get the employee email address from the Employee doctype
                employee_email = employee.email
                
                # Prepare the email content
                subject = f"Your Payslip for {doc.period_start_date} - {doc.period_end_date}"
                message = f"Dear {employee.first_name},<br><br>"
                message += f"Your payslip for the period from {doc.period_start_date} to {doc.period_end_date} has been finalized.<br>"
                message += "Regards,<br>Your HR Team Megha Sharma"
 
 
                file_name = f"Booking_Report_{doc.name}.pdf"
 
                # template_path = "customhrms/report/employee_report/templates/report/employee_report.html"
                # context = {"doc": doc}
                # html_content = frappe.render_template(template_path, context)
                
                # Generate PDF from rendered HTML
                #pdf_data = get_pdf(html_content)
                pdf_data = frappe.get_print("Payslip", doc.name, print_format="format1", as_pdf=True)
 
 
                # # Save PDF file
                # file_name = f"Booking_Report_{doc.name}.pdf"
                # saved_file = save_file(file_name, pdf_data, doc.doctype, doc.name, is_private=0)
                
                # Send the email with the report attached
                frappe.sendmail(
                    recipients=[employee_email],
                    subject=subject,
                    message=message,
                    attachments=[{
                        'fname': file_name,
                        'fcontent': pdf_data
                    }]
                )
                frappe.enqueue("frappe.email.queue.flush")
                print("Payslip email sent to:", employee_email)
            else:
                frappe.throw(frappe._("Employee record not found or email is missing."))
        
        except Exception as e:
            # Log error and notify user in case of failure
            frappe.log_error(message=str(e), title="Payslip Email Sending Error")
            frappe.msgprint(frappe._("An error occurred while sending the email. Please try again later."))
        
        print("email sending complete")
 

    # def before_save(self):
    #     # Fetch salary structure details
    #     salary_structure = frappe.get_doc("Salary_Structure", self.salary_structure)

    #     # Fetch allowances and deductions
    #     allowances = frappe.get_all(
    #         "allowances",
    #         filters={"parent": self.salary_structure},
    #         fields=["allowance_type", "amount"]
    #     )
    #     deductions = frappe.get_all(
    #         "deductions",
    #         filters={"parent": self.salary_structure},
    #         fields=["deduction_type", "amount"]
    #     )
        
    #     # Calculate total allowances (ensure float)
    #     total_allowances = sum([float(allowance['amount']) for allowance in allowances])
        
    #     # Calculate total deductions (ensure float)
    #     total_deductions = sum([float(deduction['amount']) for deduction in deductions])
        
    #     # Fetch the basic pay and overtime pay from Salary Structure (ensure float)
    #     basic_pay = float(salary_structure.basic_pay)
    #     overtime_pay = float(salary_structure.overtime_pay)
        
    #     # Gross Salary Calculation = Basic Pay + Allowances + Overtime
    #     gross_salary = basic_pay + total_allowances + overtime_pay
        
    #     # Set the calculated values to the Payslip document
    #     self.total_salary = gross_salary
    #     self.total_deductions = total_deductions

    #     # Now handle the calculation of net salary based on total hours worked (if needed during save)
    #     if self.employee and self.month and self.year:
    #         # Fetch total worked hours for the month
    #         total_hours = self.get_total_hours_worked(self.employee, self.month, self.year)
    #         self.total_hours = total_hours  # Save total hours in Payslip
            
    #         # Ensure hourly rate is set
    #         if not self.hourly_rate:
    #             frappe.throw("Hourly Rate is missing for this employee.")
            
    #         # Calculate earnings based on hourly rate
    #         self.total_earnings = self.total_hours * self.hourly_rate
            
    #         # Ensure total deductions is set (use existing value or default to 0)
    #         if not self.total_deductions:
    #             self.total_deductions = 0  # Default to 0 if not set
            
    #         # Calculate net salary = Total Earnings - Total Deductions
    #         self.net_salary = self.total_earnings - self.total_deductions

    #         # Notify the user about the calculated net salary
    #         frappe.msgprint(f"Payslip Calculated: Net Salary = {self.net_salary}")
    #         print(f"Employee: {self.employee}, Month: {self.month}, Total Hours: {self.total_hours}, Net Salary: {self.net_salary}")

    # def before_save(self):
    #     # Fetch salary structure details
    #     salary_structure = frappe.get_doc("Salary_Structure", self.salary_structure)

    #     # Fetch allowances and deductions
    #     allowances = frappe.get_all(
    #         "allowances",
    #         filters={"parent": self.salary_structure},
    #         fields=["allowance_type", "amount"]
    #     )
    #     deductions = frappe.get_all(
    #         "deductions",
    #         filters={"parent": self.salary_structure},
    #         fields=["deduction_type", "amount"]
    #     )
        
    #     # Calculate total allowances (ensure float)
    #     total_allowances = sum([float(allowance['amount']) for allowance in allowances])
        
    #     # Calculate total deductions (ensure float)
    #     total_deductions = sum([float(deduction['amount']) for deduction in deductions])
        
    #     # Fetch the basic pay and overtime pay from Salary Structure (ensure float)
    #     basic_pay = float(salary_structure.basic_pay)
    #     overtime_pay = float(salary_structure.overtime_pay)
        
    #     # Gross Salary Calculation = Basic Pay + Allowances + Overtime
    #     gross_salary = basic_pay + total_allowances + overtime_pay
        
    #     # Set the calculated values to the Payslip document
    #     self.total_salary = gross_salary
    #     self.total_deductions = total_deductions

    #     # Handle month and year if they're not explicitly set
    #     if not self.month and self.period_start_date:
    #         self.month = self.period_start_date.month  # Extract month from period_start_date
    #     if not self.year and self.period_start_date:
    #         self.year = self.period_start_date.year  # Extract year from period_start_date

    #     # Now handle the calculation of net salary based on total hours worked (if needed during save)
    #     if self.employee and self.month and self.year:
    #         # Fetch total worked hours for the month
    #         total_hours = self.get_total_hours_worked(self.employee, self.month, self.year)
    #         self.total_hours = total_hours  # Save total hours in Payslip
            
    #         # Ensure hourly rate is set
    #         if not self.hourly_rate:
    #             frappe.throw("Hourly Rate is missing for this employee.")
            
    #         # Calculate earnings based on hourly rate
    #         self.total_earnings = self.total_hours * self.hourly_rate
            
    #         # Ensure total deductions is set (use existing value or default to 0)
    #         if not self.total_deductions:
    #             self.total_deductions = 0  # Default to 0 if not set
            
    #         # Calculate net salary = Total Earnings - Total Deductions
    #         self.net_salary = self.total_earnings - self.total_deductions

    #         # Notify the user about the calculated net salary
    #         frappe.msgprint(f"Payslip Calculated: Net Salary = {self.net_salary}")
    #         print(f"Employee: {self.employee}, Month: {self.month}, Total Hours: {self.total_hours}, Net Salary: {self.net_salary}")


    # 
    

    # def before_submit(self):
    #     # Set the payslip status to 'Finalized' before submission
    #     if self.payslip_status == "Draft":  # Ensure it is in Draft state before changing
    #         self.payslip_status = "Finalized"
    #         print(f"Payslip {self.name} has been finalized.")

    #     # Fetch salary structure details
    #     salary_structure = frappe.get_doc("Salary_Structure", self.salary_structure)

    #     # Fetch allowances and deductions
    #     allowances = frappe.get_all(
    #         "allowances",
    #         filters={"parent": self.salary_structure},
    #         fields=["allowance_type", "amount"]
    #     )
    #     deductions = frappe.get_all(
    #         "deductions",
    #         filters={"parent": self.salary_structure},
    #         fields=["deduction_type", "amount"]
    #     )
        
    #     # Calculate total allowances (ensure float)
    #     total_allowances = sum([float(allowance['amount']) for allowance in allowances])
        
    #     # Calculate total deductions (ensure float)
    #     total_deductions = sum([float(deduction['amount']) for deduction in deductions])
        
    #     # Fetch the basic pay and overtime pay from Salary Structure (ensure float)
    #     basic_pay = float(salary_structure.basic_pay)
    #     overtime_pay = float(salary_structure.overtime_pay)
        
    #     # Gross Salary Calculation = Basic Pay + Allowances + Overtime
    #     gross_salary = basic_pay + total_allowances + overtime_pay

    #     # Now handle the calculation of net salary based on total hours worked
    #     if self.employee and self.period_start_date and self.period_end_date:
    #         # Fetch total worked hours for the given period
    #         total_hours = self.get_total_hours_worked_in_period(self.employee, self.period_start_date, self.period_end_date)
    #         self.total_hours = total_hours  # Save total hours in Payslip
            
    #         # Ensure hourly rate is set (fallback to a calculated value if needed)
    #         hourly_rate = salary_structure.basic_pay / 160  # Assuming 160 hours a month for salary calculation

    #         # Calculate net salary = Gross Salary + (Total Worked Hours * Hourly Rate) - Total Deductions
    #         net_salary = gross_salary + (total_hours * hourly_rate) - total_deductions
            
    #         # Set the calculated values to the Payslip document
    #         self.net_salary = net_salary
    #         self.total_salary = gross_salary
    #         self.total_deductions = total_deductions

    #         # Notify the user about the calculated net salary
    #         frappe.msgprint(f"Payslip Calculated: Net Salary = {self.net_salary}")
    #         print(f"Employee: {self.employee}, Total Hours Worked: {total_hours}, Net Salary: {self.net_salary}")

    # 
    
    def before_submit(self):
        # Set the payslip status to 'Finalized' before submission
        if self.payslip_status == "Draft":  # Ensure it is in Draft state before changing
            self.payslip_status = "Finalized"
            print(f"Payslip {self.name} has been finalized.")

        # Fetch salary structure details
        salary_structure = frappe.get_doc("Salary_Structure", self.salary_structure)

        # Log salary structure details to debug
        print(f"Salary Structure: {salary_structure.name}, Basic Pay: {salary_structure.basic_pay}, Overtime Pay: {salary_structure.overtime_pay}")
        
        # Check if basic_pay is None and handle accordingly
        
        overtime_pay = salary_structure.overtime_pay if salary_structure.overtime_pay is not None else 0.0
            
        # Fetch allowances and deductions
        allowances = frappe.get_all(
            "allowances",
            filters={"parent": self.salary_structure},
            fields=["allowance_type", "amount"]
        )
        deductions = frappe.get_all(
            "deductions",
            filters={"parent": self.salary_structure},
            fields=["deduction_type", "amount"]
        )
        
        # Calculate total allowances (ensure float)
        total_allowances = sum([float(allowance['amount']) for allowance in allowances])
        
        # Calculate total deductions (ensure float)
        total_deductions = sum([float(deduction['amount']) for deduction in deductions])
        basic_pay = float(salary_structure.basic_pay) if salary_structure.basic_pay else 0.0
        hourly_rate = basic_pay / 160  # Assuming 160 hours a month for salary calculation

        print("basiccccccccccccccccc",basic_pay)
        

        # Now handle the calculation of net salary based on total hours worked
        if self.employee and self.period_start_date and self.period_end_date:
            # Fetch total worked hours for the given period
            total_hours = self.get_total_hours_worked_in_period(self.employee, self.period_start_date, self.period_end_date)
            self.total_hours = total_hours  # Save total hours in Payslip
            
            # Gross Salary Calculation = Basic Pay + Allowances + Overtime
            gross_salary = float(total_hours * hourly_rate) + float(total_allowances) + float(overtime_pay)



            if self.total_hours >=150:
                # Calculate net salary = Gross Salary + (Total Worked Hours * Hourly Rate) - Total Deductions
                net_salary = gross_salary - total_deductions
            else:
                net_salary=gross_salary
            # tax_deduction = net_salary * 0.30  # 10% tax deduction
            # net_salary_after_tax = net_salary - tax_deduction  # Subtracting the tax from the net salary


            # Set the calculated values to the Payslip document
            self.net_salary = net_salary
            self.total_salary = gross_salary
            self.total_deductions = total_deductions

            # Notify the user about the calculated net salary
            frappe.msgprint(f"Payslip Calculated: Net Salary = {self.net_salary}")
            print(f"Employee: {self.employee}, Total Hours Worked: {total_hours}, Net Salary: {self.net_salary}")


    def get_total_hours_worked_in_period(self, employee, period_start_date, period_end_date):
        """Fetch and sum up total hours worked by the employee for the given period."""
        
        # Convert string dates to datetime objects
        period_start_date = datetime.strptime(period_start_date, '%Y-%m-%d')
        period_end_date = datetime.strptime(period_end_date, '%Y-%m-%d')
        
        # Query the timesheets based on the given period and employee
        timesheets = frappe.get_all(
            'Timesheet',
            filters={
                'employee': employee,
                'date': ['between', [period_start_date, period_end_date]]
            },
            fields=['total_hours']
        )
        
        # Sum up the total hours worked from the timesheet entries
        total_hours = 0
        for ts in timesheets:
            try:
                # Ensure the total_hours is treated as a float for addition
                total_hours += float(ts['total_hours'])
            except ValueError:
                # Handle the case where total_hours is not a valid number (e.g., invalid or empty value)
                frappe.log_error(f"Invalid total_hours value in Timesheet: {ts['total_hours']}")
        
        return total_hours


    # def get_total_hours_worked_in_period(self, employee, period_start_date, period_end_date):
    #     """Fetch and sum up total hours worked by the employee for the given period."""
        
    #     # Convert string dates to datetime objects
    #     period_start_date = datetime.strptime(period_start_date, '%Y-%m-%d')
    #     period_end_date = datetime.strptime(period_end_date, '%Y-%m-%d')
        
    #     # Query the timesheets based on the given period and employee
    #     timesheets = frappe.get_all(
    #         'Timesheet',
    #         filters={
    #             'employee': employee,
    #             'date': ['between', [period_start_date, period_end_date]]
    #         },
    #         fields=['total_hours']
    #     )
        
    #     # Sum up the total hours worked from the timesheet entries
    #     total_hours = sum(ts['total_hours'] for ts in timesheets)
        
    #     return total_hours

    # def get_total_hours_worked_in_period(self, employee, period_start_date, period_end_date):
    #     """Fetch and sum up total hours worked by the employee for the given period."""
    #     # Convert period_start_date and period_end_date to string format for query filtering
    #     period_start_date_str = period_start_date.strftime("%Y-%m-%d")
    #     period_end_date_str = period_end_date.strftime("%Y-%m-%d")
        
    #     # Fetch all timesheets for the employee within the specified period
    #     timesheets = frappe.get_all(
    #         "Timesheet",
    #         filters={
    #             "employee": employee,
    #             "date": ["between", [period_start_date_str, period_end_date_str]]
    #         },
    #         fields=["total_hours"]
    #     )

    #     # Sum total hours worked
    #     total_hours = sum(ts.get("total_hours", 0) for ts in timesheets)
    #     return total_hours

            
    # def get_total_hours_worked(self, employee, month, year):
    #     """Fetch and sum up total hours from timesheets for a given month."""
    #     timesheets = frappe.get_all(
    #         "Timesheet",
    #         filters={
    #             "employee": employee,
    #             "date": ["between", [f"{year}-{month}-01", f"{year}-{month}-31"]]
    #         },
    #         fields=["total_hours"]
    #     )

    #     # Sum total hours worked
    #     total_hours = sum(ts.get("total_hours", 0) for ts in timesheets)
    #     return total_hours
        





    # def calculate_salary(self):
    #     # Fetch salary structure and employee details
    #     salary_structure = frappe.get_doc("Salary_Structure", self.salary_structure)
    #     employee = self.employee

    #     # Fetch all attendance records for the employee for the current month
    #     total_hours_worked = self.get_total_hours_worked(employee)

    #     # Assuming 160 standard working hours in a month
    #     standard_working_hours = 190
    #     hourly_rate = salary_structure.basic_pay / standard_working_hours

    #     # Calculate total salary based on worked hours
    #     total_salary = total_hours_worked * hourly_rate
        
    #     # Calculate overtime pay for hours exceeding standard working hours
    #     overtime_hours = max(0, total_hours_worked - standard_working_hours)
    #     overtime_rate = 100  # Assuming ₹50 per hour for overtime
    #     overtime_pay = overtime_hours * overtime_rate

    #     # Calculate allowances and deductions
    #     allowances = frappe.get_all(
    #         "allowances", 
    #         filters={"parent": self.salary_structure}, 
    #         fields=["amount"]
    #     )
    #     total_allowances = sum([allowance["amount"] for allowance in allowances])

    #     deductions = frappe.get_all(
    #         "deductions", 
    #         filters={"parent": self.salary_structure}, 
    #         fields=["amount"]
    #     )
    #     total_deductions = sum([deduction["amount"] for deduction in deductions])

    #     # Calculate gross salary (including allowances and overtime)
    #     gross_salary = total_salary + total_allowances + overtime_pay

    #     # Net Salary is gross salary minus deductions
    #     net_salary = gross_salary - total_deductions

    #     # Set the calculated values in the Payslip document
    #     self.total_salary = gross_salary
    #     self.total_deductions = total_deductions
    #     self.net_salary = net_salary
    #     self.overtime_pay = overtime_pay

    # def get_total_hours_worked(self, employee):
    #     """Fetch total hours worked for the current month"""
    #     total_hours = frappe.db.sql("""
    #         SELECT SUM(hours_worked) 
    #         FROM `tabAttendance` 
    #         WHERE employee = %s AND status = 'Present' 
    #         AND MONTH(date) = MONTH(CURDATE()) 
    #         AND YEAR(date) = YEAR(CURDATE())
    #     """, (employee,), as_dict=True)[0]["SUM(hours_worked)"]

    #     return total_hours if total_hours else 0