
import frappe
from frappe.utils.data import get_url

# def redirect_after_login(login_manager):
#     frappe.logger().info("Redirect function called!")
#     print("reditrect callingggggggg")
# if frappe.session.user != "Guest":
#         frappe.logger().info("Custom redirect triggered!")
#         frappe.local.response["redirect_to"] = get_url("/employee")

def redirect_after_login(*args, **kwargs):  # Ignore login_manager
    user = frappe.session.user  # Get logged-in user
    frappe.logger().info(f"Redirecting {user} to Employee Portal.")
    print("redirect callinggggggggggg")

    if user != "Guest":
        frappe.local.response["redirect_to"] = get_url("/employee")