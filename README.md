# PlanX.one-test
My test project for a PlanX.one company.

## Installation
For project installation you should enter:

    git@github.com:eeeelya/PlanX.one-test.git

## Launch

    cd cost_manager 
    chmod +x entrypoint.sh
    sudo docker-compose up --build

After that you can create a superuser.

    sudo docker exec -it web_server python manage.py createsuperuser

## Usage 

You can access the application by this url:
    
    http://localhost:8000/

If you want to know more about API:

    http://localhost:8000/swagger/ 
    or     
    http://localhost:8000/redoc/ 