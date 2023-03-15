# Schema Migrations Workshop Repo

Sample project to help drive home the mechanics of the schema migration. This will serve as part of the onboarding docs! 

[Schema Migration Blog Post](./Blogs-post.md)

# Quickstart 

[Goose Quickstart](./goose_quickstart.md)

## Prerequisites

- https://github.com/pressly/goose - Goose migration tool

- docker - Used for testing database migrations locally


# Local Application Development


1.  Navigate to the `schema-migrations` folder in your terminal.
    
2.  Run `docker-compose up` to start the Docker container.
    
3.  Run `python3 api.py` to start the API.
    
4.  Open your web browser and navigate to `http://0.0.0.0:8000/v1/users`. You should see an error message saying that the database "users" does not exist.
    
5.  Run the following command to check the status of the migrations:
    
    ```
    goose -dir database mysql "user:password@/database?parseTime=true" status
    ```
    
6.  Run the following command to apply the migrations:
    
     ```
    goose -dir database mysql "user:password@/database?parseTime=true" up
    ```
    
7.  Verify that all migrations completed successfully with an "OK" message.
    
8.  Navigate to `http://0.0.0.0:8000/v1/users`. You should see an empty array `[]`.
    
9.  To add a new user, run the following `curl` command in the terminal:
    
     ```
    curl -X 'POST' \   'http://0.0.0.0:8000/users?name=Hello&email=hello@meow.com' \   -H 'accept: application/json' \   -d 
     ```
    
    This will create a new user with the name "Hello" and email "[hello@meow.com](mailto:hello@meow.com)".
    
10.  Navigate to `http://0.0.0.0:8000/users`. You should now see the new user in the array.
    
11.  To view the API documentation, navigate to `http://0.0.0.0:8000/docs` in your web browser.
    

Make sure to follow each step carefully to ensure that the migrations and API are set up correctly, and feel free to ask for help if you encounter any issues. Happy coding!


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