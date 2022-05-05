import pandas as pd
import pickle
from keras.models import load_model


def cargarPipeline(nombreArchivo):
    with open(nombreArchivo+'.pickle', 'rb') as handle:
        pipeline = pickle.load(handle)
    return pipeline


def cargarNN(nombreArchivo):
    model = load_model(nombreArchivo+'.h5')
    print("Red Neuronal Cargada desde Archivo")
    return model


# Se carga el Pipeline de Preprocesamiento
nombreArchivoPreprocesador = 'pipePreprocesadores'
pipe = cargarPipeline(nombreArchivoPreprocesador)
print('Pipeline de Preprocesamiento Cargado')
# Se carga la Red Neuronal
modeloOptimizado = cargarNN('modeloRedNeuronalBase')
# Se integra la Red Neuronal al final del Pipeline
pipe.steps.append(['modelNN', modeloOptimizado])
print('Red Neuronal integrada al Pipeline')


def predecirNuevoCliente(age, job, marital, education, default,
                         balance, housing, loan, contact, day,
                         month, duration, campaign, pdays, previous, poutcome):
    cnames = ['age', 'job', 'marital', 'education', 'default',
              'balance', 'housing', 'loan', 'contact', 'day',
              'month', 'duration', 'campaign', 'pdays', 'previous', 'poutcome']
    Xnew = [age, job, marital, education, default,
            balance, housing, loan, contact, day,
            month, duration, campaign, pdays, previous, poutcome]
    Xnew_Dataframe = pd.DataFrame(data=[Xnew], columns=cnames)
    pred = (pipe.predict(Xnew_Dataframe) > 0.5).astype("int32")
    pred = pred.flatten()[0]  # de 2D a 1D
    return pred
