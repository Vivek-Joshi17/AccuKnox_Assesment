# AccuKnox_Assesment
<br>
Question1 :
<br>
Solution : Django signals are executed synchronously. when a signal is sent, Django will wait for the signal handlers before moving on.
<br>
<br>
Code: synAsync.py
<br>
<br>
Question2 :  
<br>
Solution : Django signals run in the same thread as the caller. We can confirm this by printing the thread ID of the caller and the signal receiver.
<br>
<br>
Code: threadCall.py
<br>
<br>
Question3 :
<br>
Solution : Django signals execute within the same database transaction as the caller if the signal is sent within an atomic block. If an exception is raised in the signal handler, it will roll back the transaction.
<br>
<br>
Code: databaseTransaction\Singnals-app\signals.py
<br>
<br>
Question4 :
<br>
Solution : The Rectangle class allows us to create instances representing rectangles with length and width. Additionally, instances of Rectangle are iterable and will return {'length': <value>} and {'width': <value>} in sequence when iterated over.
<br>
Code: customClass.py
