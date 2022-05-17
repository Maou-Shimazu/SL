echo Creating User sl
psql -U postgres -c "CREATE USER sl WITH SUPERUSER;"
echo sl database created
echo Creating database sl....
psql -U postgres -c "CREATE DATABASE sl OWNER sl;" 
echo Database Created!