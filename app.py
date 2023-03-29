from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

friends_dict = [
   
]


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template(
        "index.html", pageTitle="Web form template", friends=friends_dict
    )


@app.route("/add", methods=["POST"])
def add():
    print("inside add function")
    if request.method == "POST":

        form = request.form

        Title = form["Title"]
        Author = form["Author"]
        Pages = form["Pages"]
        read = form["read"]
        activities = form.getlist("activities")  # this is a PYthon list
        Option = form["Option"]

        print(Title)
        print(Author)
        print(Pages)
        print(read)
        print(activities)
        print(Option)

        activities_string = ", ".join(activities)  # make the Python list into a string

        friend_dict = {
            "Title": Title,
            "Author": Author,
            "Pages": Pages,
            "read": read,
            "activities": activities_string,
            "Option": Option,
        }

        print(friend_dict)
        friends_dict.append(
            friend_dict
        )  # append this dictionary entry to the larger friends dictionary
        print(friends_dict)
        return redirect(url_for("index"))
    else:
        return redirect(url_for("index"))
    

@app.route("/about", methods=["GET"])
def about():
    return render_template("about.html", pageTitle="About my Web form",)



if __name__ == "__main__":
    app.run(debug=True)
