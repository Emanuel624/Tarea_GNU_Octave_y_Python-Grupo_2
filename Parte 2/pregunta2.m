%Fernando Fuchs Mora.
%Javier Tenorio Cervantes.
%Randall Bolaños Lopez.
%Emanuel Chavarría Hernández.

% Programa para resolver el sistema de ecuaciones Ax = h
% haciendo uso de la Funcion de la Matriz Pentadiagonal.
clc; clear; close all;

m = 2500;
a = 2 * (1:m)';         %Diagonal Principal
b = -((2:m) / 3)';      %Diagonal Inferior
c = ((1:m-1) / 3)';     %Diagonal Superior
d = -((3:m) / 2)';      %Segunda diagonal Inferior
e = ((1:m-2) / 2)';     %Segunda diagonal Superior
h = (2 * (1:m) - 5)';   %Vector del Sistema

% Llamar a la Funcion Pentadiagonal con los parametros definidos
A = pentadiagonal(m, a, b, c, d, e);

% Resolver el sistema de ecuaciones establecido
x = A \ h;

% Calcular el error de la solucion haciendo uso
% del vector del sistema Ax = h
% Error utilizando la Norma Euclideana "norm"

disp('La solución del sistema presenta un Error de:');
error = norm(A * x - h, 2);
disp(error);

