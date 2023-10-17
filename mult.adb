--Andrea Diaz
--Pregunta 1.2

--Packages a importar
with Ada.Text_IO; use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;

--Definimos el procedimento main
procedure mult is
    --Num guarda el tamaño de las matrices
    Num : Natural;
    --Procedimiento que realiza la multiplicacion
    procedure matrixMult (N:Integer) is 
        --Definimos las matrices a utilizar y algunas variables para guardar resultados
        matrix : array (1..N, 1..N) of Integer;
        mirror : array (1..N, 1..N) of Integer;
        mult : array(1..N,1..N) of Integer;
        res : Integer;
        dig : Integer;
    
        begin
        --loop para armar matriz y tomar el input   
        for i in 1..N loop
            for j in 1..N loop
                get(dig);
                matrix(i,j) := dig;
            end loop;
        end loop;
        --Loop para armar la transpuesta
        for i in 1..N loop
            for j in 1..N loop
                mirror(j,i):= matrix(i,j);
            end loop;
        end loop;
        --Loop para realizar multiplicacion
        for i in 1..N loop
            for j in 1..N loop
                res:=0;
                for k in 1..N loop
                    res := res + matrix(i,k)*mirror(k,j);
                end loop;
                mult(i,j) := res;
            end loop;
        end loop;
        --loop para imprimir resultado
        for i in 1..N loop
            for j in 1..N loop
                put(mult(i,j));
            end loop;
            put_line("");
        end loop;
    end matrixMult;
    
--Tomamos el input para el tamaño de la matriz    
begin
    get(Num);
    matrixMult(Num);
    
end mult;