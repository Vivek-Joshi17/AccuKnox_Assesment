import os
import django
from django.dispatch import Signal, receiver
from django.db import transaction


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'databaseTransaction.settings') 
django.setup()  

my_signal = Signal()

@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Receiver executed")
    raise Exception("Receiver exception")

def send_signal():
    try:
        with transaction.atomic():
            print("Sending signal")
            my_signal.send(sender=None)
    except Exception as e:
        print(f"Exception caught: {e}")

# Calling the function
send_signal()
