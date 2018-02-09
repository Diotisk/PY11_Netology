import osa
import os
# import requests
# from pprint import pprint
# from xml.etree.ElementTree import fromstring


def read_file(path_name):
    file_path = os.path.abspath(path_name)
    with open(file_path) as file:
        content = file.readlines()
    return content


def get_average_temps_celsius(path_name):
    client = osa.Client("http://www.webservicex.net/ConvertTemperature.asmx?WSDL")
    temps_f_list = read_file(path_name)
    result_temps_f_list = []
    temps_c_list = []

    for temp_f_line in temps_f_list:
        temp_f = temp_f_line.strip().split()
        for i in temp_f:
            if i.isdigit():
                result_temps_f_list.append(i)

    for temp in result_temps_f_list:
        temp_c = client.service.ConvertTemp(Temperature=temp, FromUnit="degreeFahrenheit", ToUnit="degreeCelsius")
        temps_c_list.append(temp_c)

    return sum(temps_c_list) / len(temps_c_list)

# print(get_average_temps_celsius("temps.txt"))


def get_ticket_costs(path_name):
    client = osa.Client("http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL")
    routes_list = read_file(path_name)
    costs_rub_list = []

    for route in routes_list:
        route_by_parts = route.strip().split()  # each line with route as list
        route_cost_rub = client.service.ConvertToNum(fromCurrency=route_by_parts[2], toCurrency="RUB",
                                                     amount=int(route_by_parts[1]),
                                                     rounding=True)
        costs_rub_list.append(route_cost_rub)
    return round(sum(costs_rub_list))

# print(get_ticket_costs("currencies.txt"))

# code from the lesson

# client = osa.Client("http://www.dneonline.com/calculator.asmx?WSDL")
#
# def add(l, r):
#     return client.service.Add(l, r)

# help(client.service)


# def add(n1, n2):
#     response = requests.post("http://www.dneonline.com/calculator.asmx?op=Add",
#                          headers={
#                              "Content-Type": "text/xml; charset=utf-8"
#                          },
#                          data="""<?xml version="1.0" encoding="utf-8"?>
#                                 <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
#                                       xmlns:xsd="http://www.w3.org/2001/XMLSchema"
#                                       xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#                                   <soap:Body>
#                                     <Add xmlns="http://tempuri.org/">
#                                       <intA>""" + str(n1) + """</intA>
#                                       <intB>""" + str(n2) + """</intB>
#                                     </Add>
#                                   </soap:Body>
#                                 </soap:Envelope>"""
#                          )
#     return int(fromstring(response.text)[0][0][0].text)
