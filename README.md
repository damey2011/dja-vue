# django-vue-starter
An extremely simplified Django + Vue Boilerplate project code. Combining both official starter boilerplates hence ease of use.

Demo here (Master Branch) [https://dja-vue.herokuapp.com](https://dja-vue.herokuapp.com)

---

## Setup
> To create a new project based off this template. Clone it like below.

```bash
git clone https://github.com/damey2011/dja-vue.git
```

> To use the preconfigured tailwind in your project

```bash
git clone -b feature/tailwind https://github.com/damey2011/dja-vue.git
```

There is not much settings that need to be done, infact, no setting.

### For Development 
While in the root directory:
- Setup Virtual Environment 

  ```bash
  virtualenv -p python3 env
  ```
- Activate Virtual Environment

  ```bash
    source env/bin/activate
  ```
- Install requirements

  ```bash
  pip install -r requirements.txt
  ```
- Run Django Server

  ```bash
  python manage.py runserver
  ```
  This starts at port 8000 except stated otherwise.
  
- Navigate into `frontend` and install dependencies

  ```bash
  cd frontend && npm install
  ```
- Start the node server

  ```bash
  npm run serve
  ```
  This starts at port 8080.
  
From here, you could continue with your development work.

### For production
After you must have been done and you want to build your application, in the project root folder on your local machine:
Run 

```bash
./sync_frontend.sh
```

If you can't run this, make the file executable first by running

```bash
chmod u+x sync_frontend.sh
```
Then try again.

If you still have issues overall running this `sync_frontend.sh`, you could do it one after the other by running:

```bash
cd frontend/
npm run prebuild
npm run build
npm run sync
python manage.py collectstatic
```

While on your server, you might have to run the collect static again because the static folder is ignored repo-wise by default
for size reasons. `python manage.py collectstatic`


All done! You just need to run only your django application now. 

```bash
python manage.py runserver
```

---

### Pre-installed packages

- **Allauth**: You can find the documentation [here](https://django-allauth.readthedocs.io/en/latest/)
- **Django Rest Auth**: This also depends on allauth, and you can find the documentation [Here](https://django-rest-auth.readthedocs.io/en/latest/)
- **Django Yasg**: For documentation of the API, you can view this already at *http://YOURHOST/redocs/* as soon as you have deployed. Documentation is [here](https://github.com/axnsan12/drf-yasg)

### Directory Description

> apps

This contains your django applications

> frontend

This contains the Vue project standalone, you don't have any business with this folder in production, you might even choose not to ship it 
along your software after you must have built your project.

> project

This contains your project `settings.py`, base `urls.py` and `wsgi.py`. You might choose to edit this to suit your needs, probably to the 
name of your own project.

> static

As usual with django, contains your assets; images, fonts, css, scripts etc. After running build, your necessary assets are copied here
automatically.

> templates

Still has the same meaning as the regular templates folder. The entry file `index.html` is copied/contained here after build.

---

### Requirements

- Python 3

---

If you encounter any other problem, please create an issue. Thank you
