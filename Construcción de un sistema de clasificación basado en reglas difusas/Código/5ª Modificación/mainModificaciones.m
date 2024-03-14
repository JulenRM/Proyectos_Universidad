%% Cargar datos
load('iris.mat')
dataset.X = round(iris.features,1);
dataset.Y = (1:3)*[strcmp(iris.label,'Iris-setosa'); strcmp(iris.label,'Iris-versicolor'); strcmp(iris.label, 'Iris-virginica')];

%% Seleccionar que modificaciones realizar, la número 0 se trata de lo realizado originalmente.
fprintf("\nMod 0: Trabajo original (Distribución original 50/50)\nMod 1: Primera modificación distribución 66,67/33,33\nMod 2: Segunda modificacion distribución 80/20\n\n")
mod1 = str2num(input("Selecciona modificación 1: ","s"));

fprintf("\nMod 0: Trabajo original (Conjuntos difusos Triangulares)\nMod 1: Conjuntos difusos Gaussianos\n\n")
mod2 = str2num(input("Selecciona modificación 2: ","s"));

fprintf("\nMod 0: Trabajo original (T-norma producto)\nMod 1: T-norma minimo\nMod 2: T-norma Lukasiewicz\nMod 3: T-norma Drastica\n\n")
mod3 = str2num(input("Selecciona modificación 3: ","s"));

fprintf("\nMod 0: Trabajo original (Agregación media aritmetica)\nMod 1: Agregación Integral Choquet\nMod 2: Agregacion OWA (Al menos la mitad)\nMod 3: Agregación OWA (La mayor parte de)\nMod 4: Agregación OWA (La mayor cantidad posible)\n\n")
mod4 = str2num(input("Selecciona modificación 4: ","s"));

main(dataset,mod1,mod2,mod3,mod4)