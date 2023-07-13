# build_files.sh
echo "Building the project"
pip install -r requirements.txt

echo "Collect static"
python3.9 manage.py collectstatic --noinput --clear