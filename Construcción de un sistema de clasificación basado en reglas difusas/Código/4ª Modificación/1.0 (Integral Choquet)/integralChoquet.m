function agregacion = integralChoquet(conjunto)
    agregacion = 0;
    aux = 0;
    conjunto = sort(conjunto,'ascend');
    for i = 1:length(conjunto)
        agregacion = agregacion+((conjunto(i)-aux)*(size(conjunto,2)-aux));
        aux = aux+1;
    end
end