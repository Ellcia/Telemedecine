% Charger le fichier "part1.csv"
data = readmatrix('part1.csv')
% Sélectionner les deux dernières colonnes
signal3 = data(:, 3);
signal4 = data(:, 4);

% Fenêtre de moyenne glissante (par exemple, une fenêtre de largeur 5)
window_size = 7;

% Appliquer la moyenne glissante aux signaux
smoothed_signal3 = smoothdata(signal3, 'movmean', window_size);
smoothed_signal4 = smoothdata(signal4, 'movmean', window_size);

% Créer un vecteur pour l'axe x
x = 1:length(signal3);

% Tracer les signaux originaux et les signaux lissés dans le même graphique
figure;
subplot(2, 1, 1);
plot(x, signal3, 'b', 'LineWidth', 2);
hold on;
plot(x, smoothed_signal3, 'g', 'LineWidth', 2);
title('Signal 3 - Original vs Lissé');
xlabel('Échantillons');
ylabel('Valeurs');
legend('Signal 3 Original', 'Signal 3 Lissé');
grid on;

subplot(2, 1, 2);
plot(x, signal4, 'r', 'LineWidth', 2);
hold on;
plot(x, smoothed_signal4, 'm', 'LineWidth', 2);
title('Signal 4 - Original vs Lissé');
xlabel('Échantillons');
ylabel('Valeurs');
legend('Signal 4 Original', 'Signal 4 Lissé');
grid on;
