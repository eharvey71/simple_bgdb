# simple_bgdb

## To Do

- [ ] Add proper error handling on both the front and back-end.
  - [ ] What if a title has more than one designer?
  - [ ] Handle an invalid payload where the title, designer, publsiher, and/or played is missing?
- [ ] Where should showMessage should be set to false? Make Updates.
- [ ] Refactor the for loop in the remove_game helper so that it's more Pythonic.
- [ ] Instead of deleting on the button click, add a confirmation alert.
- [ ] Display a "No games! Please add one." message when no games are present in the table.
- [ ] Handle the case of an id not existing or if the payload isn't correct
- [ ] Try using the same modal for handling both POST and PUT requests / edit+add modals
- [ ] Clean the Games component up by moving the methods that make HTTP calls to a utils or services file.
- [ ] Try to combine some of the methods that contain similar logic, like handleAddSubmit and handleEditSubmit
- [ ] Use the Alert component to display errors.
- [ ] Refactor the alert to be [https://getbootstrap.com/docs/5.2/components/alerts/#dismissing](dismissible).
- [ ] Implement database (with ORM?)
- [ ] Add Authentication
- [ ] Individual User Accounts
- [ ] Add more game info fields.
- [ ] Report: All Games: PDF and CSV Export

## Long-term To Do

- [ ] Add BGG integration for pulling in game metadata.
- [ ] Stats / Analytics pages
- [ ] Add Option to Buy/Sell Games - Stripe - Amazon - BGG - NobleKnight
- [ ] Wysiwyg Editor (?)
- [ ] [https://github.com/mjhea0/flaskr-tdd](Test Driven Development)
