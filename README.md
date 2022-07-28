# drf-product-store
Simple product store project using Django REST framework
## Installation
clone the repository:
```
git clone https://github.com/Shizuku-Asami/drf-product-store.git
```
then `cd` into the cloned project:
```
cd ./drf-product-store
```
create a virtual environment (Windows):
```
python -m venv venv
```
If you're on Linux (Assuming you have python3.10):
```
python3.10 -m venv venv
```
activate the virtual environment:
```
source venv/Scripts/activate
```
For Linux users:
```
source venv/bin/activate
```
and run:
```
pip install -r requirements.txt
```
create a `.env` file in the project's root and type the following:
```
SECRET_KEY="your_secret_key"
DEBUG=True
```
and finally start the server using
```
python manage.py runserver
```
