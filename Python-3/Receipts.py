# Codecademy based project

loveseat_description = '''Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white.'''
loveseat_price = 254.00

sofa_description = '''Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black.'''
sofa_price = 180.50

lamp_description = '''Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade.'''
lamp_price = 52.15

sales_tax = .088


customer_one_total = 0
customer_one_itemization = "";

customer_one_total += loveseat_price
customer_one_itemization += loveseat_description

customer_one_total += lamp_price
customer_one_itemization += lamp_description


customer_one_tax = customer_one_total * sales_tax
customer_one_total += customer_one_tax


print("Customer One Items:" + customer_one_itemization)
print("Customer One Total:" + str(customer_one_total))
