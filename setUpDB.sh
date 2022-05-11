args="--host=localhost --dbname=sl --username=sl"

echo -e "Creating user sl.....\n"
sudo -u postgres createuser --superuser --pwprompt sl
echo -e "User Created!\n"

echo -e "Creating database sl.....\n"
sudo -u postgres createdb --owner=sl sl
echo -e "Database Created!\n"
echo -e "Restarting server and starting psql....\n"
sudo service postgresql restart

psql $args