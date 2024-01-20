# Order form app

This project is a simple test to try out Django and Vue.

##Backend
The backend is implemented in the Python-based Django framework, which uses a SQLite database to store data. In addition to managing the order data, the backend application also handles the emailing of shipping notifications. Requests can only be submitted from an allowed IP address.

##Frontend
The frontend is written in Vue 3. The frontend downloads all the data from the database when opened, and uses it to create a table of subscriptions with columns that can be sorted by content. It is not currently possible to enter new orders in the frontend. However, each order can be opened in the modal window to view its contents and send the order as a pdf file to the email address selected from the drop-down menu or download the pdf file. The list of mail recipients comes from the database in the employees table. The pdf will display the order information and the barcode in Code128 format. If you press the send button without selecting a recipient, an error message is displayed. If the backend application has sent out the email, the frontend application displays a popup message and changes the status of the order form in both the database and the frontend application data (pending -> delivered).
