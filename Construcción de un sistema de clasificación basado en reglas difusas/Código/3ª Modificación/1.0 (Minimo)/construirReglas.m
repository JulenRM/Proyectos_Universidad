function reglas = construirReglas(Xtrain,Ytrain, conjuntos)
    reglasAux = [];
    reglas = [];
    for i = 1:length(Xtrain)
        [valA,argA] = max(conjuntos.A(:,find(conjuntos.R_A==Xtrain(i,1))));
        [valB,argB] = max(conjuntos.B(:,find(conjuntos.R_B==Xtrain(i,2))));
        [valC,argC] = max(conjuntos.C(:,find(conjuntos.R_C==Xtrain(i,3))));
        [valD,argD] = max(conjuntos.D(:,find(conjuntos.R_D==Xtrain(i,4))));
        valGrado = min(min(valA,valB),min(valC,valD)); %Usada la T-norma del minimo
        valClase = Ytrain(:,i);
        reglasAux = [reglasAux;argA argB argC argD valGrado valClase];
    end

    for i = 1:length(reglasAux)
        mask = ismember(reglasAux(:,1:4),reglasAux(i,1:4),'rows');
        aux = reglasAux(mask,:);
        [~,argMax] = max(aux(:,5));
        if(sum(reglas) == 0)
            reglas = [reglas;aux(argMax,:)];
        elseif(sum(ismember(reglas,aux(argMax,:),'rows'))==0)
            reglas = [reglas;aux(argMax,:)];
        end
    end
end