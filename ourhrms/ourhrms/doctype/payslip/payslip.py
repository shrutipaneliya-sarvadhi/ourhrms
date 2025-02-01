# Copyright (c) 2025, hr and contributors
# For license information, please see license.txt
 
# import frappe
import frappe
from frappe.model.document import Document
from frappe.utils.file_manager import save_file
from frappe.utils.pdf import get_pdf
 
 
class Payslip(Document):
    def before_save(self):
        salary_structure = frappe.get_doc("Salary_Structure", self.salary_structure)
 
        # Correctly reference the allowances child table using the fieldname 'allowances'
        allowances = frappe.get_all(
            "allowances",  # Ensure this is the correct child table name if needed
            filters={"parent": self.salary_structure},
            fields=["allowance_type", "amount"]
        )
        print("----------------------------------------------------------------------",allowances)
         # Fetch Deductions from the Salary Structure (child table)
        deductions = frappe.get_all(
            "deductions",  # Assuming "Deduction" is the correct child table DocType name
            filters={"parent": self.salary_structure},  # Filter by Salary Structure
            fields=["deduction_type", "amount"]  # Fields we need for calculation
        )
        
        # # Check if allowances are found
        # if allowances:
        #   for allowance in allowances:
        #       # Process each allowance here
        #       allowance_type = allowance.get('allowance_type')
        #       amount = allowance.get('amount')
        #       # You can perform further processing using allowance_type and amount
        # else:
        #   # Handle case where no allowances are found
        #   frappe.throw("No allowances found for the selected salary structure.")
 
         # Calculate total allowances
         
        total_allowances = sum([allowance['amount'] for allowance in allowances])
        
        # Calculate total deductions
        total_deductions = sum([deduction['amount'] for deduction in deductions])
 
        # Fetch the basic pay from Salary Structure
        basic_pay = salary_structure.basic_pay
        
        # You may want to include overtime, if applicable
        overtime_pay = salary_structure.overtime_pay
        
        # Gross Salary Calculation = Basic Pay + Allowances + Overtime
        gross_salary = basic_pay + total_allowances + overtime_pay
 
        # Net Salary = Gross Salary - Deductions
        net_salary = gross_salary - total_deductions
 
        # Set the calculated values to the Payslip document
        self.total_salary = gross_salary
        self.total_deductions = total_deductions
        self.net_salary = net_salary
    
    def before_submit(self):
        # Set the payslip status to 'Finalized' before submission
        if self.payslip_status == "Draft":  # Ensure it is in Draft state before changing
            self.payslip_status = "Finalized"
            # You can perform additional logic here if necessary
 
 
 
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
 
    # def on_submit(self):
    #   print("email sendinggggggggggggg")
        
    #   try:
    #       # Get the employee record linked to this payslip
    #       employee = frappe.get_doc("Employee", self.employee)  # 'employee' field in Payslip
            
    #       if employee and employee.email:
    #           # Get the employee email address from the Employee doctype
    #           employee_email = employee.email
                
    #           # Prepare the email content
    #           subject = f"Your Payslip for {self.period_start_date} - {self.period_end_date}"
    #           message = f"Dear {employee.name1},<br><br>"
    #           message += f"Your payslip for the period from {self.period_start_date} to {self.period_end_date} has been finalized.<br>"
    #           message += f"Total Salary: {self.total_salary}<br>"
    #           message += f"Total Deductions: {self.total_deductions}<br>"
    #           message += f"Net Salary: {self.net_salary}<br><br>"
    #           message += "Regards,<br>Your HR Team"
                
    #           # Generate the Payslip Report using your custom print format 'format1'
    #           report = frappe.get_doc("Payslip", self.name)
    #           report_html=report.run_method('get_print', 'customhrms/print_format/format1')
 
 
    #           # Optionally, you can convert the HTML to PDF (if needed) and attach it
    #           pdf_content = frappe.utils.pdf.get_pdf(report_html)
 
    #           # Send the email with the report attached
    #           frappe.sendmail(
    #               recipients=[employee_email],
    #               subject=subject,
    #               message=message,
    #               attachments=[{
    #                   'fname': f"Payslip_{self.name}.pdf",
    #                   'fcontent': pdf_content
    #               }],
    #               now=True  # Send the email immediately
    #           )
    #           print("Payslip email sent to:", employee_email)
    #       else:
    #           frappe.throw(frappe._("Employee record not found or email is missing."))
    #   except Exception as e:
    #       frappe.log_error(message=str(e), title="Payslip Email Sending Error")
    #       frappe.msgprint(frappe._("An error occurred while sending the email. Please try again later."))
    #   print("email sending complete")
 
 
    
 
    # def on_submit(self):
    #   print("email sendinggggggggggggg")
        
    #   try:
    #       # Get the employee record linked to this payslip
    #       employee = frappe.get_doc("Employee", self.employee)  # 'employee' field in Payslip
            
    #       if employee and employee.email:
    #           # Get the employee email address from the Employee doctype
    #           employee_email = employee.email
                
    #           # Prepare the email content
    #           subject = f"Your Payslip for {self.period_start_date} - {self.period_end_date}"
    #           message = f"Dear {employee.name1},<br><br>"
    #           message += f"Your payslip for the period from {self.period_start_date} to {self.period_end_date} has been finalized.<br>"
    #           message += f"Total Salary: {self.total_salary}<br>"
    #           message += f"Total Deductions: {self.total_deductions}<br>"
    #           message += f"Net Salary: {self.net_salary}<br><br>"
    #           message += "Regards,<br>Your HR Team"
                
    #           # Generate the Payslip Report using your custom print format 'format1'
    #           report = frappe.get_doc("Payslip", self.name)
    #           report_html = report.run_method('get_print', 'format1')  # Use your custom format 'format1'
 
    #           # Optionally, you can convert the HTML to PDF (if needed) and attach it
    #           pdf_content = frappe.utils.pdf.get_pdf(report_html)
 
    #           # Send the email with the report attached
    #           frappe.sendmail(
    #               recipients=[employee_email],
    #               subject=subject,
    #               message=message,
    #               attachments=[{
    #                   'fname': f"Payslip_{self.name}.pdf",
    #                   'fcontent': pdf_content
    #               }],
    #               now=True  # Send the email immediately
    #           )
    #           print("Payslip email sent to:", employee_email)
    #       else:
    #           frappe.throw(frappe._("Employee record not found or email is missing."))
    #   except Exception as e:
    #       frappe.log_error(message=str(e), title="Payslip Email Sending Error")
    #       frappe.msgprint(frappe._("An error occurred while sending the email. Please try again later."))
    #   print("email sending complete")
 
 
    # def on_submit(self):
    #   print("email sendinggggggggggggg")
    #   # Get the employee record linked to this payslip
    #   employee = frappe.get_doc("Employee", self.employee)  # 'employee' field in Payslip
        
    #   if employee and employee.email:
    #       # Get the employee email address from the Employee doctype
    #       employee_email = employee.email
            
    #       # Prepare the email content
    #       subject = f"Your Payslip for {self.period_start_date} - {self.period_end_date}"
    #       message = f"Dear {employee.name1},<br><br>"
    #       message += f"Your payslip for the period from {self.period_start_date} to {self.period_end_date} has been finalized.<br>"
    #       message += f"Total Salary: {self.total_salary}<br>"
    #       message += f"Total Deductions: {self.total_deductions}<br>"
    #       message += f"Net Salary: {self.net_salary}<br><br>"
    #       message += "Regards,<br>Your HR Team"
            
    #       # Send the email
    #       frappe.sendmail(
    #           recipients=[employee_email],
    #           subject=subject,
    #           message=message,
    #           now=True  # Send the email immediately
    #       )
    #   print("email senddddddddddddddd")