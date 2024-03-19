### Model: User
- creates 2 attr by default,
```commandline
created_at
updated_at
```
- subclasses from the base class will have these methods too and the 2 attr 
```commandline
    def save(self):
        """
        Save the instance to the database and update the updated_at attribute.
        """
    def to_dict(self):
        """
        Return a dictionary representation of the instance.
        """
```

### Model: User
```commandline
Example usage
    user1 = User(username='user1', email='user1@example.com', password='password1')
    user2 = User(username='user2', email='user2@example.com', password='password2')

    # Save users to the database
    user1.save()
    user2.save()

    # Retrieve all users from the database
    all_users = User.query.all()
    print("All Users:")
    for user in all_users:
        print(user.to_dict())

    # Retrieve a user by username
    specific_user = User.query.filter_by(username='user1').first()
    print("\nSpecific User:")
    print(specific_user.to_dict())
```