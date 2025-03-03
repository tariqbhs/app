from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'votre_cle_secrete'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        nom_complet = request.form['nom_complet']
        ville = request.form['ville']
        email = request.form['email']
        
        if not nom_complet or not ville or not email:
            flash('Tous les champs sont obligatoires.')
            return render_template('form.html', nom_complet=nom_complet, ville=ville, email=email)
        
        if '@' not in email or '.' not in email:
            flash('Veuillez entrer un email valide.')
            return render_template('form.html', nom_complet=nom_complet, ville=ville, email=email)
        
        return redirect(url_for('confirmation', nom_complet=nom_complet, ville=ville, email=email))
    
    return render_template('form.html')

@app.route('/confirmation')
def confirmation():
    nom_complet = request.args.get('nom_complet')
    ville = request.args.get('ville')
    email = request.args.get('email')
    return render_template('confirmation.html', nom_complet=nom_complet, ville=ville, email=email)

if __name__ == '__main__':
    app.run(debug=True)