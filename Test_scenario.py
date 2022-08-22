# Testing scenarios
## Test Scenario Workflow
Test scenario describes a set of test cases (tester interactions) that should be performed to confirm
functionality fully working on Application.
Test of the Application will be made by Marta Haluszka 20.08.2022 on the Windows 10, Chrome browser, version 104.0.5112.81.
#### Dictionary
**Application** - set of functionality consisting of 2 web pages: Main Page and Results Page (see below),
Search Bar component and its functionality.
API - Application programing interface, a service that processes the data submitted by the User and
returns responses based on the provided inputs.
Main Page - home page of the Application where Search Bar takes prominent space and location just
below navigation.
Results Page - page to which the User is redirected to display all results with filtering options.
Search Bar - text input that displays Search Results based on text provided by the User.
Search Button - visual element on the page in form of a magnifying glass used to invoke the search
functionality located to the far right side of the Search Bar and integral part of the Search Bar.
Search Bar Search Results - results displayed below the Search Bar input.
Filter - available on Results Page, a menu on the left side allowing to refine Search Results based on
predefined, dynamic, chainable presets.
Suggestion - Suggested search term provided by API to the User based on the current Query of the
Search Bar.
Query - text provided by the User in input of the Search Bar.

#### Initial state
Initial state by default should always be:
1. Freshly reloaded Main Page.
2. Empty Search Bar with no Query.
3. Deselected Filters if the test starts on the Results Page.
4. Query Parameters are cleared.
#### Performing the test
Describes all actions performed by a User starting from Initial state.
All tests performed should have screenshots provided to confirm results of the test.
#### Verifying expectations
Test case will define expected results - these should be compared with results seen during the test
and such comparison will define the result of the test.
1. Testing basic Search Bar functionality
a. Search Bar allows to input text in the field.
b. Search Bar will not display results if the response from API is empty.
c. Search Bar will redirect the User to Results Page if a Query is provided when clicking
Search Button (magnifying glass on right side of Search Bar).
d. Search Bar will redirect the User to Results Page if a Query is provided when pressing.
Enter
2. Testing Search Bar Search Results
a. Search Bar Search Results will display a type of result provided
b. Search Bar Search Results will display 3 categories of results:
   - Suggestion.
   - Extensions.
   - Filters.
c. User can interact with results with a mouse (highlights selection on mouse over) or
keyboard.
d. If Search Bar Search Results require more space to display results than available
within browser’s Viewport height Search Bar Search Results will be displayed with a
scrollbar
#### Result of the test
If defined expectations and actual results match, the test should be defined as PASSED if not FAILED.
If a test FAILED it MUST be repeated and if FAILURE can be reproduced it should be documented with
a description and screenshots showing exactly what steps are needed to reproduce the error.
If the test sometimes FAILS and sometimes PASSES it should be marked as FAILED to note that
it’s not clear what causes it to FAIL. Then it would be very advisable to include Network tab results for
All test results should have screenshots provided to confirm results of the test.
To test functionality of the Search bar tester will type some inputs to Search Bar and confirm this by using:
   a) the enter button on the keyboard,
   b) the magnifying glass icon,
   c) the mouse.
#### Test cases
1. Correct inputs that are contained in the API, confirm this by using:
   a) the enter button on the keyboard,
   b) the magnifying glass icon,
   c) the mouse.
2. Incorrect inputs that are contained in the API, confirm this by using:
   a) the enter button on the keyboard,
   b) the magnifying glass icon,
   c) the mouse.
3. Correct inputs that are not contained in the API, confirm this by using:
   a) the enter button on the keyboard,
   b) the magnifying glass icon,
   c) the mouse.
4. Incorrect inputs that are not contained in the API, confirm this by using:
   a) the enter button on the keyboard,
   b) the magnifying glass icon,
   c) the mouse.
5. Correct inputs that are contained in the API,check all 3 categories of results using the keyboard and the mouse:
   a) Suggestion,
   b) Extensions,
   c) Filters.
6. Correct inputs that are contained in the API, check show up and working of Search Results scrollbar, using:
   a) the keyboard,
   b) the mouse.
7. Incorrect inputs, check working of Suggestion.
   a) full incorrect words,
   b) minor typos in words.
9.Regression checking of other functions of the web application.
