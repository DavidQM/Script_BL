function [H13, Tz, Lz] = zero_crossing(p, fs, h, zp)

% ========================================================================
% ------------------->>>       ZERO-CROSSING       <<<--------------------
% ========================================================================
% +----------------------------------------------------------------------+
% |                       Autor: Daniel S. Pelaez Z.                     |
% |                     e-mail: dspelaez@unal.edu.co                     |
% |                          Fecha: Febrero, 2013                          |
% |                                                                      |
% |               Universidad Nacional de Colombia sede Medellin         |
% |      Grupo de Investigacion en Oceanografia e Ingenieria Costera     |
% |                              OCEANICOS                               |
% +----------------------------------------------------------------------+
%
% Esta funcion calcula la altura de ola significante, el periodo de pasos
% ascendentes por cero y la longitud de onda asociada a ese periodo.
%
% Versiones:
% ----------
%  -  2014/02/23 ---> Primera version del script
%  -  2014/02/23 ---> Corrige por profundidad wave-by-wave
%
% Datos de entrada:
% -----------------
%  -  Burst de serie de tiempo de presion (p)
%  -  Frecuencia de muestreo
%  -  Profundidad del equipo
%
% Datos de salida:
% ----------------
%  -  Espectro en frecuencias
%  -  Vector de frecuencias
%
% ========================================================================

% Forzar a ser vector columna
p = p(:);

% Vector de tiempo
ts = 1./fs;
t = 1:ts:length(p);

% Calculos de los puntos
% ----------------------
% Re-muestro del vector
ratio = 100;
pp = resample(p, ratio, 1);
tt = linspace(1, 1024, length(pp));

% Encontrar el indice con los ceros
x  = diff(sign(pp));
ix_up = find(x > 0);

% Encontrar la altura y el periodo de cada ola
for i = 1:length(ix_up) - 1
    a = ix_up(i);
    b = ix_up(i+1);
    Hp(i,1) = max(pp(a:b)) - min(pp(a:b));
    T(i,1)  = tt(b) - tt(a);
end

% Relacion de dispesion
% ---------------------
% Calculo del n�mero de onda usando la relaci�n de dispersi�n de la teor�a
% lineal resuelta con un m�todo iterativo (punto fijo) sin tener en cuenta
% el efecto doppler de las corrientes en la frecuencia de las olas.
%         2
%        w  =  g*k * tanh(k*h) ---> w  = 2*pi*f
g = 9.8;
f = 1./T;
w = 2*pi*f;
k0 = (w.^2)/g;
for cnt = 1:100
    k = (w.^2)./(g*tanh(k0*h));
    k0 = k;
end

% Funcion de transferencia
% ------------------------
Kp = cosh(k*h)./cosh(k*zp);
Kp(Kp > 10) = 10;


% Calculos de los parametros
% --------------------------
H = Kp.*Hp;
H0 = sort(H, 'descend');
H13 = mean(H0(ceil(length(H0)/3)));

Tz = mean(T);
Lz = mean(2*pi./k);

% -----------------------  Fin de zero_crossing  ----------------------- %