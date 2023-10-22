data = readmatrix('output.csv');
% Charger le fichier CSV

% Supprimer la première colonne de zéros
data = data(:, 2:end);

% Créer un vecteur pour l'axe x
x = 1:size(data, 1);

% Points de découpe
cut_points = [2655, 5019, 7384];

% Créer une figure
figure;

% Parcourir les signaux
for i = 1:4
    signal = data(:, i);
    
    % Sélectionner les parties correspondant aux signaux que vous voulez enregistrer
    part1 = data(1:cut_points(1), :);
    part2 = data(cut_points(1)+1:cut_points(2), :);
    part3 = data(cut_points(2)+1:cut_points(3), :);
    part4 = data(cut_points(3)+1:end, :);
    

    % Créer un vecteur pour l'axe x de chaque partie
    x_part1 = 1:length(part1);
    x_part2 = (1:length(part2)) + cut_points(1);
    x_part3 = (1:length(part3)) + cut_points(2);
    x_part4 = (1:length(part4)) + cut_points(3);
    
    % Tracer chaque partie dans un sous-graphique
    subplot(4, 1, i);
    plot(x_part1, part1, 'r', 'LineWidth', 2);
    hold on;
    plot(x_part2, part2, 'g', 'LineWidth', 2);
    plot(x_part3, part3, 'b', 'LineWidth', 2);
    plot(x_part4, part4, 'm', 'LineWidth', 2);
    
    % Titre et étiquettes
    title(['Colonne ', num2str(i)]);
    xlabel('Échantillons');
    ylabel('Valeurs');
    grid on;
    
    % Ajouter des légendes
    legend('Montée1', 'Descente', 'Montée2', 'Repos');
end

% Ajuster la disposition des sous-graphiques
sgtitle('Découpage des signaux en quatre parties');

% Réduire l'espacement entre les sous-graphiques
tightfig;


