# Rate My Professor

RateMyProf is a Django application to show the true faces of the professors of the IIT KGP realm.  

## Installation

Clone the repository 

```bash
git clone https://github.com/DefCon-007/rateMyProfessor
```

Change directory to the project source 

```bash
cd rateMyProfessor
```

Install pipenv using pip

```bash
pip install pipenv
```

Use pipenv to install dependancies. 

```bash
pipenv install --dev
```

Make a copy of `config-template.ini` in the same directory named `config.ini` and add the required values. 

```bash
cp rateMyProf/config-template.ini rateMyProf/config.ini
vim rateMyProf/config.ini
```

Open pipenv shell and launch the Django server
```bash
pipenv shell
python rateMyProf/manage.py runserver
```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)