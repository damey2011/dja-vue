# django-vue-starter
An extremely simplified Django + Vue Boilerplate project code. Combining both official starter boilerplates hence ease of use.

---

## Setup
> To create a new project based off this template. Clone it like below.

```bash
git clone https://github.com/damey2011/django-vue-starter.git
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
After you must have been done and you want to build your application, in the project root folder:
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
npm run build
echo 'yes' | npm run sync
```

All done! You just need to run only your django application now. 

---

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
