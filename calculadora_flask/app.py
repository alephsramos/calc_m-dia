from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calcular', methods=['POST'])
def calcular_media():
    av1 = float(request.form['v1'])
    av2 = float(request.form['v2'])
    md_bim = (av1 + av2)
    resultado = ('%.2f' % md_bim)
    return render_template('index.html', resultado=resultado, tipo_calculo='Média Bimestral')

@app.route('/calcular_media_prova', methods=['POST'])
def calcular_media_prova():
    md1 = float(request.form['md1'])
    v1 = float(request.form['v1'])

    # Calcular md2 necessário
    md2 = (18 - md1) / 2 
    v2 = md2 - v1
    

    resultado = ('%.2f' % v2)
    # Adicionando logs para depuração
    print(f"md1: {md1}, v1: {v1}, md2: {md2}, v2: {v2}")

    return render_template('index.html', resultado=resultado, tipo_calculo='Nota Necessária para a Última Prova')

@app.route('/calcular_media_final', methods=['POST'])
def calcular_media_final():
    md1 = float(request.form['md1'])
    md2 = float(request.form['md2'])
    md_final = (md1 + md2 * 2) / 3
    resultado = ('%.2f' % md_final)
    return render_template('index.html', resultado=resultado, tipo_calculo='Média Final')

@app.route('/calcular_media_recuperacao', methods=['POST'])
def calcular_media_recuperacao():
    md1 = float(request.form['md1'])
    md2 = float(request.form['md2'])
    md_recuperacao = (md1 + md2) / 2
    resultado = ('%.2f' % md_recuperacao)
    return render_template('index.html', resultado=resultado, tipo_calculo='Nota Necessária para Passar na Recuperação')

if __name__ == '__main__':
    app.run(debug=True)
