function main(dataset,mod1,mod2,mod3,mod4)
    %% Particiones de datos
    if(mod1==0)
        partition.indexes.train = [1:25 51:75 101:125];
        partition.indexes.test = [26:50 76:100 126:150];
    elseif(mod1==1)
        partition.indexes.train = [1:25 51:75 101:150];
        partition.indexes.test = [26:50 76:100];
    elseif(mod1==2)
        partition.indexes.train = [1:40 51:90 101:140];
        partition.indexes.test = [41:50 91:100 141:150];
    end
    partition.X.train = dataset.X(partition.indexes.train,:);
    partition.Y.train = dataset.Y(partition.indexes.train);
    partition.X.test = dataset.X(partition.indexes.test,:);
    partition.Y.test = dataset.Y(partition.indexes.test);
    
    %% Construir conjuntos difusos
    conjuntos = construirConjuntos(dataset.X,mod2);
    
    %% Construir Reglas
    reglas = construirReglas(partition.X.train,partition.Y.train, conjuntos,mod3);
    %a = array2table(reglas,"VariableNames",["Pert. A","Pert. B","Pert. C","Pert. D","Grado Certeza","Clase"]);
    
    %% Clasificar
    [acc, MC] = clasificador(partition.X.test,partition.Y.test, reglas, conjuntos,mod4);
    
    %% Mostrar resultados finales
    fprintf('El porcentaje de acierto total es un %d%% (%d)\n',round(acc*100,2),acc);
    aux = array2table(MC,"VariableNames",["Clase 1","Clase 2","Clase 3"],"RowNames",["Clase 1","Clase 2","Clase 3"]);
    table(aux,'VariableNames',{'Valor predicho'},'RowNames',{'_','Val. real','-'})
end