import exercicio

def test_true():
  assert exercicio.resposta(-2) == True

def test_false():
  assert exercicio.resposta(7) == False
