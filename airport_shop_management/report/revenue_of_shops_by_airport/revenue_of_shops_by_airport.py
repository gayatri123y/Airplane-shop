# Copyright (c) 2024, Gayatri Yeole and contributors
# For license information, please see license.txt



import frappe

def execute(filters=None):
    columns = get_columns()
    data = get_data(filters)
    total_revenue = sum(d[1] for d in data)
    data_list = [list(row) for row in data]
    total_row = ["Total", total_revenue]
    chart = get_chart(data_list, total_revenue)

    report_summary = [{
        "value": total_revenue,
        "indicator": "Light Green" if total_revenue > 0 else "Red",
        "label": "Total Revenue",
        "datatype": "Currency",
        "currency": "INR"
    }]
    
    # Append total row to data_list if needed
    # data_list.append(total_row)
    
    return columns, data_list, total_revenue, chart, report_summary

def get_data(filters):
    # Fetch data from the database
    data = frappe.db.sql("""
        SELECT
            COALESCE(sla.airport, 'Other') as airport,
            SUM(IFNULL(sla.total_rent, 0)) as revenue
        FROM
            `tabShop Lease Agreement` as sla
        GROUP BY
            sla.airport
        ORDER BY
            revenue DESC;
        """)
    return data

def get_chart(data, total_revenue):
    # Prepare data for the chart
    chart = {
        "data": {
            "labels": [d[0] for d in data],  # Include all airports
            "datasets": [
                {
                    "name": "Revenue",
                    "values": [d[1] for d in data]  # Include all revenues
                }
            ]
        },
        "type": "pie",
        "center": {
            "text": "Total Revenue",
            "subtext": frappe.format_value(total_revenue, dict(fieldtype='Currency')),
            "style": {
                "fill": "green",
                "font-size": "14px",
                "font-weight": "bold"
            }
        }
    }
    
    return chart

def get_columns():
    # Define columns for the report
    return [
        {
            "label": "Airport",
            "fieldname": "airport",
            "fieldtype": "Data",
            "width": 200
        },
        {
            "label": "Revenue",
            "fieldname": "revenue",
            "fieldtype": "Currency",
            "width": 200
        }
    ]
