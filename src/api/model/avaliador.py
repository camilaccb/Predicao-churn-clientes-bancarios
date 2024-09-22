from sklearn.metrics import recall_score
from model.pipeline import Pipeline

class Avaliador:

    def avaliar(pipeline, x_test, y_test):
        """ Faz uma predição e avalia o modelo. Poderia parametrizar o tipo de
        avaliação, entre outros.
        """
        predicoes = Pipeline.preditor(pipeline, x_test)
        
        # Caso o seu problema tenha mais do que duas classes, altere o parâmetro average
        return recall_score(y_test, predicoes)