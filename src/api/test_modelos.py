from model.carregador import Carregador
from model.pipeline import Pipeline
from model.avaliador import Avaliador

# To run: pytest -v test_modelos.py

# Instanciação das Classes
carregador = Carregador()
pipeline = Pipeline()
avaliador = Avaliador()

# Parâmetros    
dados_x_test = "./MachineLearning/data/x_test_dataset_churning.csv"
dados_y_test = "./MachineLearning/data/y_test_dataset_churning.csv"

# Carga dos dados
x = Carregador.carregar_dados(dados_x_test)
y = Carregador.carregar_dados(dados_y_test)
    
# Método para testar o modelo de Randon Forest a partir do arquivo correspondente
def test_modelo_rf():  
    # Importando a pipeline que usa o modelo de randon forest
    rf_path = './MachineLearning/models/churn_modelling_pipeline_rf.pkl'
    pipeline_rf = pipeline.carrega_pipeline(rf_path)

    # Obtendo as métricas do modelo usando o algoritmo Randon Forest
    recall_rf = Avaliador.avaliar(pipeline_rf, x, y)
    
    # Testando as métricas do modelo usando o algoritmo de Randon Forest
    assert recall_rf >= 0.7



# Método para testar o modelo de Knn a partir do arquivo correspondente
def test_modelo_knn():  
    # Importando a pipeline que usa o modelo de knn
    knn_path = './MachineLearning/models/churn_modelling_pipeline_knn.pkl'
    pipeline_knn = pipeline.carrega_pipeline(knn_path)

    # Obtendo as métricas do modelo usando o algoritmo knn
    recall_knn = Avaliador.avaliar(pipeline_knn, x, y)
    
    # Testando as métricas do modelo usando o algoritmo de knn
    assert recall_knn >= 0.7
