from flask import Flask, render_template, request, redirect
from users import User

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route('/users')
def all_users():
    users = User.get_all()
    return render_template("users.html", all_users = users)


# whenever we create something, we need to display that html page, so we need a rout for that. And we need a post route to actually process this.

# create user - display route
@app.route('/users/new')
def new():
    return render_template("create_user.html")


# create user - post route
@app.route('/user/create', methods=["POST"])
def create_user():
    # data = {
    #     "first_name": request.form("first_name"),
    #     "last_name": request.form("last_name"),
    #     "email": request.form("email"),
    # }

    # because we already lined up our query in users.py to database, we don't need to write the data request one by one.
    User.save(request.form)
    return redirect('/users')





# edit user - display route
@app.route('/users/<int:id>/edit')
def edit_user(id):
    data = {
        "id": id
    }
    return render_template('edit_user.html', user=User.get_one(data))



# edit user - post route
@app.route('/users/<int:id>/update', methods=["POST"])
def update_user(id):
    User.update(request.form)
    return redirect('/users')



# delete user
# @app.route('/users/delete')
# def delete():
#     return redirect('/users/<id>')


@app.route('/user/<int:id>/destroy')
def destroy(id):
    data ={
        'id': id
    }
    User.destroy(data)
    return redirect('/users')



# #show individual user
@app.route('/users/<int:id>/show')
def show_user(id):
    data = {
        "id":id
    }
    return render_template('show_user.html', user=User.get_one(data))



if __name__ == "__main__":
    app.run(debug=True)