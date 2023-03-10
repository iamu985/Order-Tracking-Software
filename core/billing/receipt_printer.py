from escpos.printer import Usb
from .conf import A, B, INTERFACE, EP_IN, EP_OUT, LOGO
from PIL import Image


def get_logo():
    # Get logo here
    logo = Image.open(LOGO)
    logo = logo.resize((logo.width // 2, logo.height // 2)).convert("1")
    return logo


def print_receipt():
    p = Usb(A, B, INTERFACE, EP_IN, EP_OUT)
    p.image(get_logo())
    p.text(f"{'-'*32}\n")
    p.text("HomeTown Pizzeria and Restaurant\n")
    p.text("Singhmari, Darjeeling\n")
    p.text('Ph no: 1234567890\n')
    p.text(f'orderID: 1234567890\n')
    p.text(f'TableNo: 1\n')
    p.text("Cashier: John Doe\n")
    p.text(f"{'-'*32}\n")
    p.text('{:10} {:>5} {:>15}\n'.format('Item', 'Qty', 'Price'))
    p.text('{:10} {:>2} {:>15}\n'.format('Chicken Fried', '1', 'Rs. 100'))
    p.text('{:10} {:>5} {:>15}\n'.format('Thaipo', '2', 'Rs. 200'))
    p.text(f"{'-'*32}\n")
    p.text('Thank you for coming!\n')
    p.text('Visit Again!\n')
    p.close()
