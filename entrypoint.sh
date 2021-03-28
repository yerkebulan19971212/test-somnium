# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
python manage.py makemigrations
echo "Apply database migrations"
python manage.py migrate