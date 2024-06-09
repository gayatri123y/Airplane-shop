# Copyright (c) 2024, Gayatri Yeole and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document


# class ShopLeaseAgreement(Document):
# 	pass

import frappe 
from frappe.model.document import Document
from datetime import datetime 

class ShopLeaseAgreement(Document):
    def default_rent(self):  
        default_rent_amount = frappe.get_single("Global Configuration").default_rent
        return default_rent_amount

    def calculate_total_rent(self):
        lease_start_date = datetime.strptime(self.lease_start_date, "%Y-%m-%d")
        lease_end_date = datetime.strptime(self.lease_end_date, "%Y-%m-%d")
        rent_amount = float(self.rent_amount) if self.rent_amount else 0.0

        total_months = (lease_end_date.year - lease_start_date.year) * 12 + (lease_end_date.month - lease_start_date.month) + 1

        total_rent = rent_amount * total_months

        return total_rent

    def before_save(self):
        if not self.rent_amount:
            self.rent_amount = self.default_rent()
    
        self.total_rent = self.calculate_total_rent()

