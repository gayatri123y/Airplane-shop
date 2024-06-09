// Copyright (c) 2024, Gayatri Yeole and contributors
// For license information, please see license.txt

// frappe.ui.form.on("Shop", {
// 	refresh(frm) {

// 	},
// });
frappe.ui.form.on("Shop", {
    refresh: function(frm) {
        if (!frm.doc.shop_id) {
            frm.set_value("shop_id", generateShopID());
        }
    }
});
function generateShopID() {
    const alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    const numbers = '0123456789';
    let result = 'ShopID-';
    result += alphabet.charAt(Math.floor(Math.random() * alphabet.length));
    for (let i = 0; i < 4; i++) { 
        result += numbers.charAt(Math.floor(Math.random() * numbers.length));
    }

    return result;
}