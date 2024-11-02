from django.dispatch import Signal, receiver

# Define a signal
my_signal = Signal()

# Receiver function
@receiver(my_signal)
def my_receiver(sender, **kwargs):
    print("Receiver executed")

# Function that sends the signal
def send_signal():
    print("Sending signal")
    my_signal.send(sender=None)

# Calling the function
send_signal()
