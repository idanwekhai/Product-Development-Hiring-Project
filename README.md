# Product Development Hiring Project

I built an insurance management system so users can be able to define risk types, risk types and appropriate fields for the risk they want to insure

The API was created using Django Rest Framework, and the frontend was made with Vuejs, this project was hosted on AWS lambda using zappa

## App Layout

### Data

The database was made using MySQL to create a dynamic data model, the data base has five tables field_types, risk_types, fields, risks and fields_by_risk. So users can define both the risks types for their risks and also the field types for the corresponding fields in the database. 

- https://github.com/idanwekhai/Product-Development-Hiring-Project/blob/master/docs/Model%20Diagram.JPG
- https://github.com/idanwekhai/Product-Development-Hiring-Project/blob/master/docs/my_project_subsystem.png

### API

- The API was built using the community best practices and TDD oriented, with that, the API was fully tested. The API was created using the framework Django 2.1.2 and python 3.6.

### Frontend

- The frontend was built using the modern javascript framework Vuejs, HTML5, CSS3 / Sass. 
- The app has three pages, one to make all CRUD API requests for Risk Types, one create the risks and their fields , and finally the main page, that get all risk fields and show them in a appropriate way.**(Not Finsished)** 
- All form submissions were handled properly**(My Mega Bonus)**

Here are a few frontend screens:

- https://github.com/idanwekhai/Product-Development-Hiring-Project/blob/master/docs/screenshots/screenshot1.JPG
- https://github.com/idanwekhai/Product-Development-Hiring-Project/blob/master/docs/screenshots/screenshot2.JPG

### Deployment***(mega bonus)**

- The App was deployed on AWS lambda using zappa

## How to execute 

1. Clone this project;

   ```bash
   $ git clone https://github.com/idanwekhai/Product-Development-Hiring-Project.git
   ```

2. populate the database with fixtures

   ```bash
   $ cd backend
   $ pip install -r requirements.txt
   $ python manage.py syncdata
   ```

3. start the backend dev server

   ```bash
   $ python manage.py runserver
   ```

4. start the frontend dev server

   ```bash
   $ cd frontend
   $ yarn serve
   ```

5. Access `http://localhost:8080` to open the frontend or `http://localhost:8000/api/v1` to open the API documentation.

   ## How to deploy project

   1. First create an account in AWS lambda

   2. Goto IAM role in AWS dashboard 

   3. Nagivate to Users. 

   4. Click on the Security credentials tab, and go down to Access Key, note down the `access_key_id`. `secret_access_key` is only visible when you are creating new user, so you need to note down both the access_key_id and secre_access_key at the time of user creation only. To generate a new access_key, click on the `create access key` button,.

   5. Create a folder called `.aws` at the root level of the project

      ```bash
      $ mkdir .aws
      ```

   6. Now, create a file called credentials and store the aws_access_key_id and aws_secret_access_key. The other specifics like default_region can also be stored. Firstly, to get the access credentials, do the following

      ```
      ###~/.aws/credentials
      [default]
      aws_access_key_id=[...]
      aws_secret_access_key=[...]
      ```

   7. install zappa

      ```bash
      $ pip install zappa
      ```

   8. initialize zappa

      ```bash
      $ zappa init
      ```

      It will output something like this, 

      ```
      ███████╗ █████╗ ██████╗ ██████╗  █████╗
      ╚══███╔╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗
        ███╔╝ ███████║██████╔╝██████╔╝███████║
       ███╔╝  ██╔══██║██╔═══╝ ██╔═══╝ ██╔══██║
      ███████╗██║  ██║██║     ██║     ██║  ██║
      ╚══════╝╚═╝  ╚═╝╚═╝     ╚═╝     ╚═╝  ╚═╝
      
      Welcome to Zappa!
      
      Zappa is a system for running server-less Python web applications on AWS Lambda and AWS API Gateway.
      This `init` command will help you create and configure your new Zappa deployment.
      Let's get started!
      
      Your Zappa configuration can support multiple production stages, like 'dev', 'staging', and 'production'.
      What do you want to call this environment (default 'dev'):
      ```

   9. lastly

      ```bash
      $ zappa deploy dev
      ```

      

   ## Link to Project

   1. Just access: https://u6h0ovhgul.execute-api.us-east-2.amazonaws.com/dev/api/v1/

   

   For questions or compliments, send me an email: kelvinidanwekhai@gmail.com

   
