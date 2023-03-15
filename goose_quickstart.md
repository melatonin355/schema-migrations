# Goose Migration tool Information

Goose is a database migration tool for Golang applications. It allows developers to create and manage database schema changes in a safe and automated way. Here are the steps to use Goose:

## Install Goose:
You can install Goose using Go's package manager by running the following command:

### Mac Homebrew

Install via homebrew:

```
brew install goose
```

### Linux

```
curl -fsSL \
    https://raw.githubusercontent.com/pressly/goose/master/install.sh |\
    sh 
```

# Resources 
- https://pressly.github.io/goose/installation/


## Commands

Here are some common commands:

-   `goose create migration <migration_name>` - create a new migration with the given name
-   `goose up` - apply all available migrations
-   `goose down` - undo the last applied migration
-   `goose status` - display the current status of migrations
-   `goose redo` - undo the last migration and then reapply it
-   `goose reset` - undo all applied migrations
-   `goose fix` - apply any available fixes to migrations

You will have to modify above command as such if you are using the sampme migration repo:

```
goose -dir database mysql "user:password@/database?parseTime=true" status
```