function conjuntos = construirConjuntos(X)
    A = X(:,1);
    B = X(:,2);
    C = X(:,3);
    D = X(:,4);

    A1 = min(A);
    A3 = max(A);
    A2 = round((A1+A3)/2,1);

    B1 = min(B);
    B3 = max(B);
    B2 = round((B1+B3)/2,1);

    C1 = min(C);
    C3 = max(C);
    C2 = round((C1+C3)/2,1);

    D1 = min(D);
    D3 = max(D);
    D2 = round((D1+D3)/2,1);

    conjuntos.R_A = round(A1:0.1:A3,1);
    conjuntos.R_B = round(B1:0.1:B3,1);
    conjuntos.R_C = round(C1:0.1:C3,1);
    conjuntos.R_D = round(D1:0.1:D3,1);
    
    conjuntos.A(1,:) = gaussmf(conjuntos.R_A,[std(A) A1]);
    conjuntos.A(2,:) = gaussmf(conjuntos.R_A,[std(A) A2]);
    conjuntos.A(3,:) = gaussmf(conjuntos.R_A,[std(A) A3]);

    conjuntos.B(1,:) = gaussmf(conjuntos.R_B,[std(B) B1]);
    conjuntos.B(2,:) = gaussmf(conjuntos.R_B,[std(B) B2]);
    conjuntos.B(3,:) = gaussmf(conjuntos.R_B,[std(B) B3]);

    conjuntos.C(1,:) = gaussmf(conjuntos.R_C,[std(C) C1]);
    conjuntos.C(2,:) = gaussmf(conjuntos.R_C,[std(C) C2]);
    conjuntos.C(3,:) = gaussmf(conjuntos.R_C,[std(C) C3]);

    conjuntos.D(1,:) = gaussmf(conjuntos.R_D,[std(D) D1]);
    conjuntos.D(2,:) = gaussmf(conjuntos.R_D,[std(D) D2]);
    conjuntos.D(3,:) = gaussmf(conjuntos.R_D,[std(D) D3]);

    %figure;
    %plot(conjuntos.R_B,conjuntos.B(1,:),'b');
    %hold on;
    %plot(conjuntos.R_B,conjuntos.B(2,:),'r');
    %hold on;
    %plot(conjuntos.R_B,conjuntos.B(3,:),'y');
    %legend('D1','D2','D3');
    %title('Variable Ancho Petalo');
end