#!/usr/bin/env bash
cd src/
python3 manage.py update_front_end_static_url
cd frontend/
npm run build
cd ..
python3 manage.py run_frontend_build_corr
python3 manage.py collectstatic --no-input
echo 'Synchronization Complete'
