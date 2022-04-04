import pandas as pd
from xml.dom.minidom import parseString

record = pd.read_csv("example.csv")

record_list = record.values.tolist()


def get_node_value(node):
    return node.childNodes[0].data


for record in record_list:
    forename = record[0]
    surname = record[1]

    xml_doc = parseString(record[2])

    company_node = xml_doc.getElementsByTagName("Company")[0]
    employee_node = company_node.getElementsByTagName("Employee")[0]
    email_node = employee_node.getElementsByTagName("Email")[0]
    address_node = employee_node.getElementsByTagName("Address")[0]
    city_node = address_node.getElementsByTagName("City")[0]

    email = get_node_value(email_node)
    city = get_node_value(city_node)

    print(
        f"Forename: {forename}, Surname: {surname}, Email: {email}, City: {city}")
