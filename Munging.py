# Imports.
import pandas as pd
import re

# Formats phone numbers.
def format_number(phone):
    result = re.fullmatch(r'(\d{3})(\d{3})(\d{4})', phone)
    if len(phone) > 13:
        phone = ''
    return '-'.join(result.groups()) if result else phone

# Formats zips.
def format_zip(zip):
    if len(zip) < 5 or len(zip) > 9 :
        zip = ' '
        return zip
    elif len(zip) == 9:
        zip = zip[:5] + "-" + zip[5:]
        return zip
    else:    
        return zip

# Formats email.
def format_email(email):
    for i in email:
        if '@' not in email or '.' not in email:
            email = ''
            return email
        else:
            return email

def format_review(review):
    review = 'Y'
    return review
            
# Holds customer info.
customer_info = [['Jim Bean', '32955', '3219300203', 'jimbean@icloud.com', 'N'],
                 ['Steve Adams', '11143', '1234567890', 'steve@gmail.com', 'N'],
                 ['Thomas Jefferson', '456907259', '4443336666', 'tom@gmail.com', 'N'],
                 ['John Bomb', '11124', '8569631265', 'john@gmail.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N'],
                 ['Mike Shaney', '224560000', '8885551234', 'mike@yahoo.com', 'N']]

# Assign column data frame.
customer_infoFormat = pd.DataFrame(customer_info, columns = ['Name', 'Zip', 'Phone','Email', 'Review?'])

# Correcs data.
corrected_phone = customer_infoFormat['Phone'].map(format_number)
corrected_zip = customer_infoFormat['Zip'].map(format_zip)
corrected_email = customer_infoFormat['Email'].map(format_email)

# Replace original data with formatted data.
customer_infoFormat['Phone'] = corrected_phone
customer_infoFormat['Zip'] = corrected_zip
customer_infoFormat['Email'] = corrected_email

for i in customer_infoFormat:
    if '' or ' ' in customer_infoFormat:
        corrected_review = customer_infoFormat['Review'].map(format_review)
        customer_info['Review'] = corrected_review

# Prints to standard I/O.
print(customer_infoFormat)
