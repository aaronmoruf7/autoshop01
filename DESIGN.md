# Introduction
My auto shop finance application consisted of using
- flask (python)
- SQL database
- HTML
- CSS
- Javascript

Let's examine how I implemented each of the following features, and why I made the design decisions I did:

# Overall:
Firstly, this is the my first time actually creating my own web application, so I decided to use flask as I was familiar with it from class.
I also knew how to easily incorporate flask with app routes, web pages and databases which were all crucial for the functionality of my app.

# Registration Page
My registration form is loaded from my forms.py and displayed via html. When the desired username is entered, the SQL database is checked to see whether the name was take or not. Also, both password and password confirmation must match to be registered succesfully. The password that is stored in the database is hashed for security purposes. After entering all the data correctly, you are automatically logged in.

# Login Page
My login form is loaded from my forms.py and displayed via html. When the username and password are entered, the SQL database is checked to see whether they were correct or not. If they are, you are logged in succesfully. If not, an error message will appear.

# Change Password Page
My change password form is loaded from my forms.py and displayed via html. When the old password, new password and password confirmation are entered, the SQL database is checked to see whether the old password is correct. The new password and confirmation must also match, else an error wil appear. Once the new password is implemented it will be hashed and updated in the database.

# Logout
Logging out, is as simple as clearing the session and redirecting the user back to the login page.

# Home Page
For the home page, in order to display the financial summary at the top, a calculation function is used from helpers.py, and the summary is displayed via html. The recent transactions are retrieved from the SQL database and displayed via html. For the interactive graph, I needed to fetch monthly data from my SQl database which was why I had to use commands such as "SELECT strftime('%Y-%m', date) AS month". The interactive functionality of the graph was produced through java script, some of which I sourced online. The data for my graph was passed from flask, including the labels and data points.

# Income/Expense/Customer Page
The income/expense/customer pages simply retrieve data from my SQL database specific to the user and display the transactions/customers databases via html. They also contains search bars with live search functionality (no need to press enter). This functionaity comes from javascript, some of which I sourced online. This function simply retrieved the search input value and filtered the transactions/customers based on the search (hid and showed only transactions related to the search input value).

# Add Income/Expense Page
The add income/expense/customer page retrieve data from a form (via my forms.py which is displayed via html). All the fields must be input else an error message will be given. Then the data is inserted into the database to reflect in the transaction/customer tables as well as the financial summary in the home page.

# Delete Income/Expense/Customer Functions
When any delete button is pressed and confirmed, the specific transaction/customer id is retireved. In order to retrieve this information a hidden form was used for each delete button. This hidden transaction id is then used to find the corresponding entry in the SQL database. Once it is found, the transaction/customer will be deleted permanently.

# Receipt Generation
All the receipt data is retrieved from the html forms. The total cost and discount amounts are found through simple calculation and all of the information is passed into the receipt template html. Then the html from the receipt template is converted to pdf using pdfkt, having downloaded "wkhtmltopdf" into my system. I also tried to use "report lab" to render this receipt pdf but "wkhtmltopdf" was much easier as I was able to design my receipt using html.

# CSS
I mostly used bootstrap to design my web app, as well as importing my font from google fonts. I included Bootstrap datepicker to ensure ease of use and consistency with date entry. I also included bootstrap javascript so I can add responsiveness to my bootstrap designs. My CSS style sheet was mainly used for ensuring the appropriate font appearances as well as the designs of my tables and navigation bar.


