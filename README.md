# VakomsTask

Test task for Vakoms by Max Dubchak

## Project configuration
1. Clone this repository.
2. Activate virtual environment.
#### Backend
1. Go to the folder `requirements.txt` and run command to install required dependencies:
    ```
    $ pip install -r requirements.txt
    ```
2. Create new sql database
    ```
    mysql> CREATE DATABASE <db_name>;
    ```
3. Go to the folder with `settings.py`, create file local_settings.py and add following fields there:
    ```
    # skip DOMAIN if you plan to use 127.0.0.1:8000
    DOMAIN = '<domain>' 
    EMAIL_HOST_USER = '<email host user>'
    EMAIL_HOST_PASS = '<email host pass>'
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'HOST': '<Host>',
            'USER': '<db_user>',
            'PASSWORD': '<db_password>',
            'NAME': '<db_name>',
        }
    }
    ``` 
4. In folder with `manage.py` file run migrate: 
    ```
    $ python manage.py migrate
    ```

5. In same folder (folder with `manage.py`) run
    ```
    $ python manage.py runserver
    ```
