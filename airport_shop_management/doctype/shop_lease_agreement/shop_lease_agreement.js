// Copyright (c) 2024, Gayatri Yeole and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Shop Lease Agreement", {
// 	refresh(frm) {

// 	},
// });

frappe.ui.form.on("Shop Lease Agreement", {
    refresh: function(frm) {
        if (!frm.doc.lease_agreement_id) {
            frm.set_value("lease_agreement_id", generateID());
        }
    }
});

function generateID() {
    const numbers = '0123456789';
    let result = 'LAI-';
    for (let i = 0; i < 4; i++) { 
        result += numbers.charAt(Math.floor(Math.random() * numbers.length));
    }

    return result;
}