--Andrea Diaz
--Pregunta 1.1

--Packages a importar
with Ada.Strings;       use Ada.Strings;
with Ada.Strings.Fixed; use Ada.Strings.Fixed;
with Ada.Strings.Maps;  use Ada.Strings.Maps;
with Ada.Text_IO; use Ada.Text_IO;
with Ada.Integer_Text_IO; use Ada.Integer_Text_IO;

--Procedimiento main
procedure rotacion is
    --Declaramos Chain para guardar el string del usuario, Last para guardar el numero de caracteres y Num para tomar el numero de posiciones a mover
    Chain: String(1..100) := (others => ' ');
    Last: Natural;
    Num: Natural;
    
 --Procedimiento para rotar Num posiciones el string Chain
procedure toTheLeft (S:String; L:Natural) is
    --Se define Dupe para tomar el primer caracter de la cadena de caracteres
    --Sub es para guardar desde el segundo caracter hasta el ultimo de Chain
    --SS guarda el string modificado 
    Dupe: String(1..1);
    Sub: String(1..Last-1);
    SS : String:=S;
    begin
    --Este loop se realiza la cantidad de rotaciones necesarias.
    --Primero se divide el string desde el segundo caracater hasta el ultimo y se guarda en Sub, el primer caracter luego se apenda al final
    for I in 1 .. Num loop
        Sub:= SS(SS'first+1..L);
        Dupe:= SS(1..1);
        Overwrite(SS,1,Sub);
        Overwrite(SS,L,Dupe);
    end loop;
    put("Resultado = ");
    put(SS);
    end toTheLeft;
    

    
begin
    --Toma el input del usuario
    put("Ingrese un cadena de caracteres y numero para la cantidad de rotacions: ");
    Get_Line(Chain,Last);
    get(Num);
    put_line(Chain);
    ToTheLeft(Chain,Last);
    
    
end rotacion;