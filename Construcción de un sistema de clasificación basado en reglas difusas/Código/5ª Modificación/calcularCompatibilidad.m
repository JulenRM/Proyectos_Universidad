function compatibilidad = calcularCompatibilidad(Xtrain, reglas, conjuntos)
    compatibilidad = [];
    for j = 1:length(reglas)
        A = conjuntos.A(reglas(j,1),find(conjuntos.R_A==Xtrain(1)));
        B = conjuntos.B(reglas(j,2),find(conjuntos.R_B==Xtrain(2)));
        C = conjuntos.C(reglas(j,3),find(conjuntos.R_C==Xtrain(3)));
        D = conjuntos.D(reglas(j,4),find(conjuntos.R_D==Xtrain(4)));
        compatibilidad = [compatibilidad,A*B*C*D]; %Usada la T-norma del producto
    end
end