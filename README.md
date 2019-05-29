# Todo API with Flask

## Installation

1. python3 -m venv venv / virtualenvwrapper / or create your own Virtual Environment
2. activate the venv
3. pip install -r requirements.txt
4. python manage.py migrate

**Important:**
1. Make sure you clear all your cache
2. Make sure you clear all your cookies for localhost / 127.0.0.1
3. python manage.py runserver

A fellow student of yours in the Full Stack JavaScript Techdegree has just taken the Angular Basics course and has a pretty nice working Angular.js Todo app. They went a little farther and used the ng-resource plugin which allows the application to work automatically using RESTful practices. However, they don’t have experience yet on the server side of things. But you do. Can you help them out?

The ability to provide a back-end for a client-side app is a great skill to have, and you will encounter the need to do this throughout your journey. As long as their app is functioning they will be happy.

I’ve started the shell of the project for you and the app currently serves the Angular app. Remember to use your developer tools in your browser to see what is being attempted.

You got this!

## App Features

- This API is versioned, all routes should be prefixed with /api/v1
- When the app first starts it will attempt to fetch all Todos in the system. Handle the request and return all the Todos.
- Look at the browser tool to see what is being requested and how and create the appropriate route
- When a Todo is created and the save link is clicked, it will make a request to the server. Handle the request by creating a Todo and setting the proper status code.
- Look at the browser tool to see what is being requested and how and create the appropriate route
- When a previously saved Todo is updated and the save link is clicked, it will make a request to the server. Handle the request by updating the existing Todo.
- Look at the browser tool to see what is being requested and how and create the appropriate route.
- When a previously saved Todo is deleted and the save link is clicked, it will make a request to the server. Handle the deletion and return a blank response and the proper status code.
- Unit test the app.
- Write unit tests to test that each view is displaying the correct information. Write unit tests to test that the models, classes, and other functions behave as expected.
- Testing coverage over 75%