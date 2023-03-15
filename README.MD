# Schema Migrations Workshop Repo

Sample project to help drive home the mechanics of the schema migration. This will serve as part of the onboarding docs! 

[Schema Migration Blog Post](./Blogs-post.md)

# Quickstart 

[Goose Quickstart](./goose_quickstart.md)

## Prerequisites

- https://github.com/pressly/goose - Goose migration tool

- docker - Used for testing database migrations locally


0. Bring up MySQL database via Docker

```
docker-compose up
```

1. display the current status of migrations

goose -dir database mysql "user:password@/database?parseTime=true" status

```
2023/03/13 12:41:52     Applied At                  Migration
2023/03/13 12:41:52     =======================================
2023/03/13 12:41:52     Pending                  -- 20230313120026_add_user.sql
2023/03/13 12:41:52     Pending                  -- 20230313120058_add_pets.sql
```

2. apply all available migrations

```
goose -dir database mysql "user:password@/database?parseTime=true" up   
```

You should see: 

```
2023/03/13 12:42:22 OK   20230313120026_add_user.sql (20.13ms)
2023/03/13 12:42:22 OK   20230313120058_add_pets.sql (23.25ms)
2023/03/13 12:42:22 goose: no migrations to run. current version: 20230313120058
```
2. goose -dir database mysql "user:password@/database?parseTime=true" down

```
goose -dir database mysql "user:password@/database?parseTime=true" down  

2023/03/13 12:42:40 OK   20230313120058_add_pets.sql (17.32ms)
```

goose -dir database mysql "user:password@/database?parseTime=true" status

```
2023/03/13 12:42:43     Applied At                  Migration
2023/03/13 12:42:43     =======================================
2023/03/13 12:42:43     Mon Mar 13 19:42:22 2023 -- 20230313120026_add_user.sql
2023/03/13 12:42:43     Pending                  -- 20230313120058_add_pets.sql
```


# Local Application Development

Navigate to schema-migrations folder. 

1. Run 
    docker-compose up
2. Run 
    python3 api.py
3. Navigate to
     http://0.0.0.0:8000/v1/users
4. Should throw error: 
    Database users does not exist
5. Run goose up 
    goose -dir database mysql "user:password@/database?parseTime=true" status
6. Run goose up
    goose -dir database mysql "user:password@/database?parseTime=true" up
7. Verify that all migrations successfully completed with OK 
8.  Navigate to
     http://0.0.0.0:8000/v1/users
9. You should see [] 
10. Add new user by running the following curl command in the terminal:
```
curl -X 'POST' \
  'http://0.0.0.0:8000/users?name=Hello&email=hello@meow.com' \
  -H 'accept: application/json' \
  -d ''
```
11. Navigate to http://0.0.0.0:8000/users
You should see the new user. 


You can see the API documentation by navigating to:
- http://0.0.0.0:8000/docs



## You have 45 minutes to complete the following

Don't worry about completing all the steps within the given time, just identify what is slowing you down and write down anything that was not clear.

Instructions:

You have 45 minutes to complete the tasks listed below. Don't worry if you can't finish all of them, just try your best and focus on completing them accurately.

-   Create a new schema migration to add a new entity called 'alien' with the following properties: 'name', 'planet', and 'coordinates'. To apply the migration, run the command 'goose up'.
-   Modify the existing API (in api.py) to version 2.0 so that the endpoint can be accessed using the URL: [http://0.0.0.0:8000/v2/users](http://0.0.0.0:8000/v2/users).
-   Update the Version-2-0.md file to reflect the changes you made.
-   Ensure that you update app = FastAPI(version="1.1.0") to the appropriate version.
-   Once you have completed the tasks, create a pull request and tag someone from release management.
-   Send a meme of your choice to the release management channel once you are done!
-   You will be added to the "certified-deployer-guild" mailing list!

If you encounter any issues or have questions, please don't hesitate to ask for help. Focus on understanding the instructions clearly, and take notes if needed to help you stay organized and keep track of your progress. Good luck!

![deployed](https://media.giphy.com/media/3og0IAQG2BtR13joe4/giphy-downsized.gif)