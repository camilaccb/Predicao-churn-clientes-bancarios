import pickle

class Pipeline:
    
    def carrega_pipeline(self,path):
        """Carregamos o pipeline construido durante a fase de treinamento
        """
        
        with open(path, 'rb') as file:
             pipeline = pickle.load(file)
        return pipeline
    
    def preditor(model, x_input):
        """Realiza a predição de churn de um cliente com base no modelo treinado
        """
        churn_prediction = model.predict(x_input)
        return churn_prediction