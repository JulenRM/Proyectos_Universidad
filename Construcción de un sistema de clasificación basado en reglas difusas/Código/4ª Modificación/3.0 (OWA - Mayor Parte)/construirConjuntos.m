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
    
    conjuntos.A(1,:) = trimf(conjuntos.R_A,[A1 A1 A2]);
    conjuntos.A(2,:) = trimf(conjuntos.R_A,[A1 A2 A3]);
    conjuntos.A(3,:) = trimf(conjuntos.R_A,[A2 A3 A3]);

    conjuntos.B(1,:) = trimf(conjuntos.R_B,[B1 B1 B2]);
    conjuntos.B(2,:) = trimf(conjuntos.R_B,[B1 B2 B3]);
    conjuntos.B(3,:) = trimf(conjuntos.R_B,[B2 B3 B3]);

    conjuntos.C(1,:) = trimf(conjuntos.R_C,[C1 C1 C2]);
    conjuntos.C(2,:) = trimf(conjuntos.R_C,[C1 C2 C3]);
    conjuntos.C(3,:) = trimf(conjuntos.R_C,[C2 C3 C3]);

    conjuntos.D(1,:) = trimf(conjuntos.R_D,[D1 D1 D2]);
    conjuntos.D(2,:) = trimf(conjuntos.R_D,[D1 D2 D3]);
    conjuntos.D(3,:) = trimf(conjuntos.R_D,[D2 D3 D3]);

    %figure;
    %plot(conjuntos.R_B,conjuntos.B(1,:),'b');
    %hold on;
    %plot(conjuntos.R_B,conjuntos.B(2,:),'r');
    %hold on;
    %plot(conjuntos.R_B,conjuntos.B(3,:),'y');
    %legend('D1','D2','D3');
    %title('Variable Ancho Petalo');
end