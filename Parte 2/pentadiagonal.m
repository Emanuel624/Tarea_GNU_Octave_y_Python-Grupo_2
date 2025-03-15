% Funcion que crea una Matriz Pentadiagonal, en
% donde todos los elementos que estan fuera de la
% diagonal principal y las dos diagonales adyacentes
% por encima y por debajo de esta son igual a cero.

clc; clear; close all;

function A = pentadiagonal(m, a, b, c, d, e)
    % Condicion 1. Verificar que m sea un entero positivo y m >= 5
    if ~isscalar(m) || m < 5 || floor(m) ~= m
        error('El valor de m debe ser un entero positivo mayor o igual a 5.');
    end

    % Condicion 2. Verificar tamaños de los vectores
    if length(a) ~= m
        error('El vector a debe tener tamaño m.');
    end
    if length(b) ~= m-1 || length(c) ~= m-1
        error('Los vectores b y c deben tener tamaño (m-1).');
    end
    if length(d) ~= m-2 || length(e) ~= m-2
        error('Los vectores d y e deben tener tamaño (m-2).');
    end

    % Construccion de la matriz pentadiagonal
    A = zeros(m, m); %Matriz donde todos los elementos son cero

    for i = 1:m
        A(i, i) = a(i);       % Diagonal Principal a
        if i < m
            A(i, i+1) = c(i); % Diagonal Superior  b
            A(i+1, i) = b(i); % Diagonal Inferior  c
        end
        if i < m-1
            A(i, i+2) = e(i); % Segunda Diagonal Superior e
            A(i+2, i) = d(i); % Segunda Diagonal Inferior d
        end
    end
end

% Casos de Ejemplo para la Matriz Pentadiagonal.

%Ejemplo 1.
m = 5;
a = [10; 20; 30; 40; 50];
b = [-1; -2; -3; -4];
c = [1; 2; 3; 4];
d = [-5; -6; -7];
e = [5; 6; 7];

A = pentadiagonal(m, a, b, c, d, e);
disp('Matriz resultante:');
disp(A);

%Ejemplo 2.
m = 6;
a = [2; 4; 6; 8; 10; 12];
b = [-1; -1; -1; -1; -1];
c = [1; 1; 1; 1; 1];
d = [-2; -2; -2; -2];
e = [2; 2; 2; 2];

A = pentadiagonal(m, a, b, c, d, e);
disp('Matriz resultante:');
disp(A);






