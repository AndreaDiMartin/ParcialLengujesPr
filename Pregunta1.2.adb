--Multiplicacion de matrices

with Ada.Text_IO; use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;
procedure jdoodle is
    Num : Natural;
    procedure matrixMult (N:Integer) is 
    
        matrix : array (1..N, 1..N) of Integer :
        mirror : array (1..N, 1..N) of Integer;
        mult : array(1..N,1..N) of Integer;
        res : Integer: =0 ;
        dig : Integer: = 0;
    
        begin
            
        for i in 1..N loop
            for j in 1..N loop
                get(dig);
                matrix(i,j) = dig;
            end loop;
        end loop;
            
        for i in 1..N loop
            for j in 1..N loop
                mirror(j,i):= matrix(i,j);
            end loop;
        end loop;
    
        for i in 1..N loop
            for j in 1..N loop
                res:=0;
                for k in 1..N loop
                    res := res + matrix(i,k)*mirror(k,j);
                end loop;
                mult(i,j) := res;
            end loop;
        end loop;
    
        for i in 1..N loop
            for j in 1..N loop
                put(mult(i,j));
            end loop;
            put_line("");
        end loop;
    end matrixMult;
    
    
begin
    get(Num)
    matrixMult(Num);
    
end jdoodle;
