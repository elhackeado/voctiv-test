# voctiv-test
Docker compose project for voctiv test, using flask, postgres, nginx and docker.


#TO RUN THE PROJECT
1. Clone the repository -  git clone https://github.com/elhackeado/voctiv-test.git
2. Move to directory - cd voctiv-test
3. Run project using docker compose command - docker-compose up
4. Run url on browser to create the "accounts" table - http://<hostIP>:9000/script
5. You will be able to see the the result that table is created in the postgres database.
  #OPTIONAL API
  http://<hostIP>:9000/showtalbes    - to show all the tables in the postgres db
  http://<hostIP>:9000/deletetable   - to delete the "accounts" table in the postgres db
  
