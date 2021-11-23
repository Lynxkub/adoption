from flask import Flask, request, render_template, redirect, flash, session
from flask_debugtoolbar import DebugToolbarExtension  
from models import db, connect_db, Pet
from forms import PetForm


app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY']= 'secret'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug=DebugToolbarExtension(app)

connect_db(app)

@app.route('/', methods = ['GET', 'POST'])
def home_page():
    """Display all pets"""

    pets = Pet.query.all()

    return render_template('home.html', pets=pets)

@app.route('/add', methods = ['GET', 'POST'])
def add_pet():
    """Add a new pet to our adoption database"""

    form = PetForm()
    
    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        pet = Pet(name = name, species = species, photo_url = photo_url, age = age, notes = notes)
        db.session.add(pet)
        db.session.commit()
        return redirect('/')
    else:
        return render_template('add_pet.html', form=form)


@app.route('/<int:pet_id>')
def show_pet_page(pet_id):
    """Display Specific Pet with Details"""
    chosen_id=Pet.query.get(pet_id)

    return render_template('pet_page.html', chosen_id=chosen_id)

@app.route('/pet/<int:pet_id>/edit', methods = ['GET', 'POST'])
def edit_pet(pet_id):
    """Edit a pet page"""
    pet = Pet.query.get_or_404(pet_id)
    form = PetForm(obj=pet)

    if form.validate_on_submit():
        pet.name = form.name.data
        pet.species = form.species.data
        pet.photo_url = form.photo_url.data
        pet.age = form.age.data
        pet.notes = form.notes.data
        
        db.session.commit()
        return redirect('/')
    else:
        return render_template('edit_pet_form.html', form = form, pet=pet)

    # Edit pet form not saving changes to the database. Also, not sure if URL validation is working correctly. Need to test before submitting