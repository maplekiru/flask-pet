"""Flask app for adopt app."""

from flask import Flask, render_template, redirect, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import db, connect_db, Pet

from forms import NewPetForm, EditPetForm

from secret_keys import secret_config_key 

app = Flask(__name__)

app.config['SECRET_KEY'] = secret_config_key 

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)
db.create_all()

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.route('/')
def list_pets():
    """Make a list of pets with links to their profiles."""

    pets = Pet.query.all()
    return render_template('pets.html', pets=pets)


@app.route('/add', methods=["GET", "POST"])
def add_pet():
    """Pet add form; handle adding."""

    form = NewPetForm()
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name=name,
                  species=species,
                  photo_url=photo_url,
                  age=age,
                  notes=notes
                  )

        db.session.add(pet)
        db.session.commit()
        #make message just message (sep of concerns)
        flash(f"<p class= 'alert alert-success'> {name} Added! </p>")
        return redirect("/")

    else:
        return render_template(
            "pets_new_form.html", form=form)


@app.route('/<int:pet_id>', methods=["GET", "POST"])
def pet_profile(pet_id):
    """
    Show information about the given pet.

    Have a form to edit pet information.
    """

    pet = Pet.query.get_or_404(pet_id)

    form = EditPetForm(obj=pet)
    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data 
        pet.available = form.available.data

        db.session.commit()

        flash(f"<p class= 'alert alert-success'> {pet.name} editted! </p>")
        return redirect(f"/{pet_id}")

    else:
        return render_template("pets_display_edit_form.html",
                               pet=pet,
                               form=form)
