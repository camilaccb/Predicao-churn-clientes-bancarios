from sklearn.metrics import recall_score
from model.pipeline import Pipeline

class Avaliador:

    def avaliar(pipeline, x_test, y_test):
        """ Faz uma predição e avalia o modelo.
        """
        predicoes = Pipeline.preditor(pipeline, x_test)
        return recall_score(y_test, predicoes)