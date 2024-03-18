#!/bin/bash

# Function to check if PostgreSQL is ready
wait_for_postgres() {
    echo "Waiting for PostgreSQL to be ready..."
    while ! nc -z $DB_HOST $DB_PORT; do
        sleep 1
    done
    echo "PostgreSQL is ready!"
}

# Run migrations after PostgreSQL is ready
run_migrations() {
    echo "Applying Django migrations..."
    python manage.py makemigrations
    python manage.py migrate
    echo "Django migrations applied successfully!"
}

# Main function
main() {
    wait_for_postgres
    run_migrations
    echo "Starting Django development server..."
}

# Execute main function
main "$@"
