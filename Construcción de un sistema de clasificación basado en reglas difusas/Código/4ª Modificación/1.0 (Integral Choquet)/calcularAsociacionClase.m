function asocClase = calcularAsociacionClase(asociacion)
    asocClase = [];
    for i = 1:3
        aux = asociacion(find(asociacion(:,2)==i),1);
        aux = reshape(aux,[1,length(aux)]);
        aux = aux(aux>0);
        aux = integralChoquet(aux);
        if(isnan(aux))
            asocClase = [asocClase,0];
        else
            asocClase = [asocClase,aux];
        end
    end
end