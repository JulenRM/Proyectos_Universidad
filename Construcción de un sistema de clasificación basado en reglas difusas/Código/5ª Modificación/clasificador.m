function [acc, MC] = clasificador(Xtrain, Ytrain, reglas, conjuntos,mod4)
    MC = zeros(3,3);
    acc = 0;
    for i = 1:length(Xtrain)
        compatibilidad = calcularCompatibilidad(Xtrain(i,:), reglas, conjuntos);
        asociacion = calcularAsociacion(compatibilidad,reglas);
        asocClase = calcularAsociacionClase(asociacion,mod4);
        [~, clase] = max(asocClase);
        if(clase == Ytrain(i))
            acc = acc+(1/length(Xtrain));
            MC(Ytrain(i),clase) = MC(Ytrain(i),clase)+1;
        else
            MC(Ytrain(i),clase) = MC(Ytrain(i),clase)+1;
        end
    end
end