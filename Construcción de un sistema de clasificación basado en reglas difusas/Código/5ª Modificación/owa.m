function agregacion = owa(conjunto,a,b)
    agregacion = 0;
    conjunto= sort(conjunto,'descend');
    for i = 1:length(conjunto)
        agregacion = agregacion+conjunto(i)*(operacionOWA(a,b,i/length(conjunto))-operacionOWA(a,b,(i-1)/length(conjunto)));
    end
end

function res = operacionOWA(a,b,x)
    if(x < a)
        res = 0;
    elseif(x > b)
        res = 1;
    else
        res = (x-a)/(b-a);
    end
end