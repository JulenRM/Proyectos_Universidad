function asocClase = calcularAsociacionClase(asociacion,mod4)
    asocClase = [];
    for i = 1:3
        aux = asociacion(find(asociacion(:,2)==i),1);
        aux = reshape(aux,[1,length(aux)]);
        aux = aux(aux>0);
        if(mod4==0)
            aux = mean(aux);
        elseif(mod4==1)
            aux = integralChoquet(aux);
        elseif(mod4==2)
            aux = owa(aux,0,0.5);
        elseif(mod4==3)
            aux = owa(aux,0.3,0.8);
        elseif(mod4==4)
            aux = owa(aux,0.5,1);
        end
        if(isnan(aux))
            asocClase = [asocClase,0];
        else
            asocClase = [asocClase,aux];
        end
    end
end