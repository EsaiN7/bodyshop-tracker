from app import create_app, objDB
from app.models import User

app = create_app()
app.app_context().push()

test_user = User(username="testuser", role="employee")
test_user.set_password("password123")
objDB.session.add(test_user)
objDB.session.commit()
print("Test user created!")
