import osa

client = osa.Client("http://www.dneonline.com/calculator.asmx?WSDL")

def add(l, r):
    return client.service.Add(l, r)

# help(client.service)



# import requests
# from pprint import pprint
# from xml.etree.ElementTree import fromstring
#
# def add(n1, n2):
#     response = requests.post("http://www.dneonline.com/calculator.asmx?op=Add",
#                          headers={
#                              "Content-Type": "text/xml; charset=utf-8"
#                          },
#                          data="""<?xml version="1.0" encoding="utf-8"?>
#                                 <soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
#                                   <soap:Body>
#                                     <Add xmlns="http://tempuri.org/">
#                                       <intA>""" + str(n1) + """</intA>
#                                       <intB>""" + str(n2) + """</intB>
#                                     </Add>
#                                   </soap:Body>
#                                 </soap:Envelope>"""
#                          )
#     return int(fromstring(response.text)[0][0][0].text)
#
print(add(5, 10))
