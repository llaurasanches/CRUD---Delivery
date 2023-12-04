from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, ForeignKey

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)

class Cliente (db.Model): 
    __tablename__= 'cliente'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # CREATE TABLE `cliente` (`_id` INT AUTO_INCREMENT PRIMARY KEY)
    nome = db.Column(db.String)  # `nome` VARCHAR(255)
    cpf = db.Column(db.String)  # `cpf` VARCHAR(255)
    email = db.Column(db.String)  # `email` VARCHAR(255)
    telefoneResidencial = db.Column(db.String)  # `telefoneResidencial` VARCHAR(255)
    telefoneCelular = db.Column(db.String)  # `telefoneCelular` VARCHAR(255)
    cep = db.Column(db.String)  # `cep` VARCHAR(255)
    logradouro = db.Column(db.String)  # `logradouro` VARCHAR(255)
    numero = db.Column(db.String)  # `numero` VARCHAR(255)
    complemento = db.Column(db.String)  # `complemento` VARCHAR(255)
    cidade = db.Column(db.String)  # `cidade` VARCHAR(255)
    uf = db.Column(db.String)  # `uf` VARCHAR(255)
    
    def __init__(self, nome, cpf, email, telefoneResidencial, telefoneCelular, cep, logradouro, numero, complemento, cidade, uf):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefoneResidencial = telefoneResidencial
        self.telefoneCelular = telefoneCelular
        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cidade = cidade
        self.uf = uf


with app.app_context():
    db.create_all()

@app.route("/index")
def index():
    return render_template("index.html")

@app.route("/cadastrarCliente")
def cadastrarCliente ():
	return render_template("cadastroCliente.html")

@app.route("/cadastroCliente", methods=['GET', 'POST'])
def cadastroCliente():
    if request.method == "POST":
        nome = request.form.get("nome")
        cpf = request.form.get("cpf")
        email = request.form.get("email")
        telefoneResidencial = request.form.get("telefoneResidencial")
        telefoneCelular = request.form.get("telefoneCelular")
        cep = request.form.get("cep")
        logradouro = request.form.get("logradouro")
        numero = request.form.get("numero")
        complemento = request.form.get("complemento")
        cidade = request.form.get("cidade")
        uf = request.form.get("uf")

        if nome and cpf and email and telefoneResidencial and telefoneCelular and cep and logradouro and numero and complemento and cidade and uf:
            c = Cliente(nome, cpf, email, telefoneResidencial, telefoneCelular, cep, logradouro, numero, complemento, cidade, uf)
            db.session.add(c)
            db.session.commit()

    return redirect(url_for("index"))


@app.route("/listaCliente")
def listaCliente(): 
	clientes = Cliente.query.all()
	return render_template("listaCliente.html", clientes=clientes)

@app.route("/excluirCliente/<int:id>")
def excluirCliente(id):
	cliente = Cliente.query.filter_by(_id=id).first()

	db.session.delete(cliente)
	db.session.commit() 

	clientes = Cliente.query.all()
	return render_template("listaCliente.html", clientes=clientes)

@app.route("/atualizarCliente/<int:id>", methods=['GET', 'POST'])
def atualizarCliente(id):
    cliente = Cliente.query.filter_by(_id=id).first()

    if request.method == "POST":
        nome = request.form.get("nome")
        cpf = request.form.get("cpf")
        email = request.form.get("email")
        telefoneResidencial = request.form.get("telefoneResidencial")
        telefoneCelular = request.form.get("telefoneCelular")
        cep = request.form.get("cep")
        logradouro = request.form.get("logradouro")
        numero = request.form.get("numero")
        complemento = request.form.get("complemento")
        cidade = request.form.get("cidade")
        uf = request.form.get("uf")

        if nome and cpf and email and telefoneResidencial and telefoneCelular and cep and logradouro and numero and complemento and cidade and uf:
            cliente.nome = nome
            cliente.cpf = cpf
            cliente.email = email
            cliente.telefoneResidencial = telefoneResidencial
            cliente.telefoneCelular = telefoneCelular
            cliente.cep = cep
            cliente.logradouro = logradouro
            cliente.numero = numero
            cliente.complemento = complemento
            cliente.cidade = cidade
            cliente.uf = uf 

            db.session.commit()

            return redirect(url_for("listaCliente"))

    return render_template("atualizarCliente.html", cliente=cliente)

class Entregador (db.Model): 
    __tablename__= 'entregador'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # CREATE TABLE `entregador` (`_id` INT AUTO_INCREMENT PRIMARY KEY)
    nome = db.Column(db.String)  # `nome` VARCHAR(255)
    cpf = db.Column(db.String)  # `cpf` VARCHAR(255)
    email = db.Column(db.String)  # `email` VARCHAR(255)
    telefoneResidencial = db.Column(db.String)  # `telefoneResidencial` VARCHAR(255)
    telefoneCelular = db.Column(db.String)  # `telefoneCelular` VARCHAR(255)
    cep = db.Column(db.String)  # `cep` VARCHAR(255)
    logradouro = db.Column(db.String)  # `logradouro` VARCHAR(255)
    numero = db.Column(db.String)  # `numero` VARCHAR(255)
    complemento = db.Column(db.String)  # `complemento` VARCHAR(255)
    cidade = db.Column(db.String)  # `cidade` VARCHAR(255)
    uf = db.Column(db.String)  # `uf` VARCHAR(255)
   
    def __init__(self, nome, cpf, email, telefoneResidencial, telefoneCelular, cep, logradouro, numero, complemento, cidade, uf):
        self.nome = nome
        self.cpf = cpf
        self.email = email
        self.telefoneResidencial = telefoneResidencial
        self.telefoneCelular = telefoneCelular
        self.cep = cep
        self.logradouro = logradouro
        self.numero = numero
        self.complemento = complemento
        self.cidade = cidade
        self.uf = uf

with app.app_context():
    db.create_all()

@app.route("/cadastrarEntregador")
def cadastrarEntregador ():
    return render_template("cadastroEntregador.html")

@app.route("/cadastroEntregador", methods=['GET', 'POST'])
def cadastroEntregador ():
    if request.method == "POST":
        nome = request.form.get("nome")
        cpf = request.form.get("cpf")
        email = request.form.get("email")
        telefoneResidencial = request.form.get("telefoneResidencial")
        telefoneCelular = request.form.get("telefoneCelular")
        cep = request.form.get("cep")
        logradouro = request.form.get("logradouro")
        numero = request.form.get("numero")
        complemento = request.form.get("complemento")
        cidade = request.form.get("cidade")
        uf = request.form.get("uf")

        if nome and cpf and email and telefoneResidencial and telefoneCelular and cep and logradouro and numero and complemento and cidade and uf:
            c = Entregador (nome, cpf, email, telefoneResidencial, telefoneCelular, cep, logradouro, numero, complemento, cidade, uf)
            db.session.add(c)
            db.session.commit()


    return redirect (url_for("index"))

@app.route("/listaEntregador")
def listaEntregador(): 
    entregadores = Entregador.query.all()
    return render_template("listaEntregador.html", entregadores=entregadores)

@app.route("/excluirEntregador/<int:id>")
def excluirEntregador(id):
    entregador = Entregador.query.filter_by(_id=id).first()

    db.session.delete(entregador)
    db.session.commit() 

    entregadores = Entregador.query.all()
    return render_template("listaEntregador.html", entregadores=entregadores)

@app.route("/atualizarEntregador/<int:id>", methods=['GET', 'POST'])
def atualizarEntregador(id):
    entregador = Entregador.query.filter_by(_id=id).first()

    if request.method == "POST":
        nome = request.form.get("nome")
        cpf = request.form.get("cpf")
        email = request.form.get("email")
        telefoneResidencial = request.form.get("telefoneResidencial")
        telefoneCelular = request.form.get("telefoneCelular")
        cep = request.form.get("cep")
        logradouro = request.form.get("logradouro")
        numero = request.form.get("numero")
        complemento = request.form.get("complemento")
        cidade = request.form.get("cidade")
        uf = request.form.get("uf")

        if nome and cpf and email and telefoneResidencial and telefoneCelular and cep and logradouro and numero and complemento and cidade and uf:
            entregador.nome = nome
            entregador.cpf = cpf
            entregador.email = email
            entregador.telefoneResidencial = telefoneResidencial
            entregador.telefoneCelular = telefoneCelular
            entregador.cep = cep
            entregador.logradouro = logradouro
            entregador.numero = numero
            entregador.complemento = complemento
            entregador.cidade = cidade
            entregador.uf = uf 

            db.session.commit()

            return redirect(url_for("listaEntregador"))

    return render_template("atualizarEntregador.html", entregador=entregador)

class Pedido (db.Model): 
    __tablename__= 'pedido'
    _id = db.Column(db.Integer, primary_key=True, autoincrement=True)  # CREATE TABLE `pedido` (`_id` INT AUTO_INCREMENT PRIMARY KEY)
    nome = db.Column(db.String)  # `nome` VARCHAR(255)
    descricao = db.Column(db.String)  # `descricao` VARCHAR(255)
    valor = db.Column(db.Float)  # `valor` FLOAT

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor

with app.app_context():
    db.create_all()

@app.route("/cadastrarPedido")
def cadastrarPedido ():
    return render_template("cadastroPedido.html")

@app.route("/cadastroPedido", methods=['GET', 'POST'])
def cadastroPedido ():
    if request.method == "POST":
        nome = request.form.get("nome")
        descricao = request.form.get("descricao")
        valor = request.form.get("valor")

        if nome and descricao and valor:
            c = Pedido (nome, descricao, valor)
            db.session.add(c)
            db.session.commit()


    return redirect (url_for("index"))

@app.route("/listaPedido")
def listaPedido(): 
    pedidos = Pedido.query.all()
    return render_template("listaPedido.html", pedidos=pedidos)

@app.route("/excluirPedido/<int:id>")
def excluirPedido(id):
    pedido = Pedido.query.filter_by(_id=id).first()

    db.session.delete(pedido)
    db.session.commit() 

    pedidos = Pedido.query.all()
    return render_template("listaPedido.html", pedidos=pedidos)

@app.route("/atualizarPedido/<int:id>", methods=['GET', 'POST'])
def atualizarPedido(id):
    pedido = Pedido.query.filter_by(_id=id).first()

    if request.method == "POST":
        nome = request.form.get("nome")
        descricao = request.form.get("descricao")
        valor = request.form.get("valor")
        
        if nome and descricao and valor:
            pedido.nome = nome
            pedido.descricao = descricao
            pedido.valor = valor

            db.session.commit()

            return redirect(url_for("listaPedido"))

    return render_template("atualizarPedido.html", pedido=pedido)


if __name__ == '__main__':
    app.run(debug=True)
