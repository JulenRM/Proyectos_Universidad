%% Cargar datos
load('iris.mat')
dataset.X = round(iris.features,1);
dataset.Y = (1:3)*[strcmp(iris.label,'Iris-setosa'); strcmp(iris.label,'Iris-versicolor'); strcmp(iris.label, 'Iris-virginica')];

%% Particiones de datos
partition.indexes.train = [1:40 51:90 101:140];
partition.X.train = dataset.X(partition.indexes.train,:);
partition.Y.train = dataset.Y(partition.indexes.train);
partition.indexes.test = [41:50 91:100 141:150];
partition.X.test = dataset.X(partition.indexes.test,:);
partition.Y.test = dataset.Y(partition.indexes.test);

%% Construir conjuntos difusos
conjuntos = construirConjuntos(dataset.X);

%% Construir Reglas
reglas = construirReglas(partition.X.train,partition.Y.train, conjuntos);
%a = array2table(reglas,"VariableNames",["Pert. A","Pert. B","Pert. C","Pert. D","Grado Certeza","Clase"]);

%% Clasificar
[acc, MC] = clasificador(partition.X.test,partition.Y.test, reglas, conjuntos);

%% Mostrar resultados finales
fprintf('El porcentaje de acierto total es un %d%% (%d)\n',round(acc*100,2),acc);
aux = array2table(MC,"VariableNames",["Clase 1","Clase 2","Clase 3"],"RowNames",["Clase 1","Clase 2","Clase 3"]);
table(aux,'VariableNames',{'Valor predicho'},'RowNames',{'_','Val. real','-'})