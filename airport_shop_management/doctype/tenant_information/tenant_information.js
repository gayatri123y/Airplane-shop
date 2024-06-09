// Copyright (c) 2024, Gayatri Yeole and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Tenant Information", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Tenant Information", {
    refresh: function(frm) {
        if (!frm.doc.tenant_id) {
            frm.set_value("tenant_id", generatetenantID());
        }
    }
});

function generatetenantID() {
    const numbers = '0123456789';
    let result = 'TI-';
    for (let i = 0; i < 4; i++) { 
        result += numbers.charAt(Math.floor(Math.random() * numbers.length));
    }

    return result;
}