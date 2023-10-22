data = readmatrix('output2.csv');
% Charger le fichier CSV

% Supprimer la première colonne de zéros
data = data(:, 2:end);

% Créer un vecteur pour l'axe x
x = 1:size(data, 1);

% Points de découpe
cut_points = [2216, 4949, 7250, 9892];

% Créer une figure
figure;

% Parcourir les signaux
for i = 1:5
    signal = data(:, i);
    
    % Découper le signal en quatre parties
    part1 = signal(1:cut_points(1));
    part2 = signal(cut_points(1)+1:cut_points(2));
    part3 = signal(cut_points(2)+1:cut_points(3));
    part4 = signal(cut_points(3)+1:cut_points(4));
    part5 = signal(cut_points(4)+1:end);

    
    % Créer un vecteur pour l'axe x de chaque partie
    x_part1 = 1:length(part1);
    x_part2 = (1:length(part2)) + cut_points(1);
    x_part3 = (1:length(part3)) + cut_points(2);
    x_part4 = (1:length(part4)) + cut_points(3);
    x_part5 = (1:length(part5)) + cut_points(4);

    
    % Tracer chaque partie dans un sous-graphique
    subplot(5, 1, i);
    plot(x_part1, part1, 'r', 'LineWidth', 2);
    hold on;
    plot(x_part2, part2, 'g', 'LineWidth', 2);
    plot(x_part3, part3, 'b', 'LineWidth', 2);
    plot(x_part4, part4, 'm', 'LineWidth', 2);
    plot(x_part5, part5, 'y', 'LineWidth', 2);

    
    % Titre et étiquettes
    title(['Colonne ', num2str(i)]);
    xlabel('Échantillons');
    ylabel('Valeurs');
    grid on;
    
    % Ajouter des légendes
    legend('Descente1', 'Montée1', 'Descente2', 'Montée2','Repos');
end

% Ajuster la disposition des sous-graphiques
sgtitle('Découpage des signaux en 5 parties');

% Réduire l'espacement entre les sous-graphiques
tightfig;
