#!/usr/bin/env bash
cd frontend/
npm run prebuild
npm run build
npm run sync
cd ..
python3 manage.py collectstatic --no-input
echo 'Synchronization Complete'
