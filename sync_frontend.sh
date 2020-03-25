#!/usr/bin/env bash
cd frontend/
npm run build
echo 'yes' | npm run sync
# The yes is for the collect static prompt
echo 'Synchronization Complete'
