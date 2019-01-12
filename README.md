# Kernael92's Neighborhood
# https://kernelhood.herokuapp.com/



## Built By [Kernael Apuko](https://github.com/kernael92/)

## Description
This is an application that allows authenticated users to find a list of different businesses in their nighborhod,set a profile about them, a general location as well as their nighborhood name,find contact information for health department and police authoroties near their neighborhood,view details of a single neighborhood as well as create posts that will be visible to everyone in their neighborhood.

## User Stories
These are the behaviours/features that the application implements for use by a user.

Users would like to:
* Sign in to the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
* Only view details of a single neighborhood.

## Admin Abilities
These are the behaviours/features that the application implements for use by the admin.

Admin should:
* Sign in to the application
* Create a profile and create posts.
* Create neighborhoods
* Update  post details.
* Create a list of businesses.


## Specifications
| Behaviour | Input | Output |
| :---------------- | :---------------: | ------------------: |
| Admin Authentication | **On demand** | Access Admin dashboard |
| Display all posts | **Home page** | Clickable image to view the details of a single post |
| clickable image to view the details of a single business| 
| To post a post  | **Through Admin dashboard** | Add the title, image, description and neighborhood|
| To edit profile | **Through Admin dashboard** | Redirected to the  profile settings and edit the profile picture,neighborhood as well as the bio|
| To delete a profile,business,Neighborhood or post  | **Through Admin dashboard** | click on any of the  objects and confirm by delete button|
| To search  | **Enter text in search bar** | Users can search by name of the neighborhood |


## SetUp / Installation Requirements
### Prerequisites
* python3.6
* pip
* virtualenv
* Requirements.txt
* Django authentication

### Cloning
* In your terminal:

        $ git clone https://github.com/kernael92/kernel-instagram
        $ cd kernel-instagram

## Running the Application
* Creating the virtual environment

        $ python3.6 -m venv --without-pip virtual
        $ source virtual/bin/activate
        $ curl https://bootstrap.pypa.io/get-pip.py | python

* Installing Django and other Modules

        $ see Requirements.txt

* To run the application, in your terminal:

        $ python3.6 manage.py runserver

## Testing the Application
* To run the tests for the class files:

        $ python3.6 manage.py test awards

## Technologies Used
* Python3.6
* Django and postgresql

## License

Copyright (c) 2018 Kernael92

------------

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
