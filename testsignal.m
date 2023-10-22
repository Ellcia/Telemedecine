% Afficher les fichiers CSV générés
for i = 1:4
    % Charger le fichier CSV
    filename = ['part', num2str(i), '.csv'];
    data = readmatrix(filename);
    
    % Créer un vecteur pour l'axe x
    x = 1:size(data, 1);
    
    % Parcourir les signaux
    figure;
    for j = 1:4
        signal = data(:, j);
        
        % Tracer le signal dans un sous-graphique
        subplot(4, 1, j);
        plot(x, signal, 'LineWidth', 2);
        
        % Titre et étiquettes
        title(['Colonne ', num2str(j)]);
        xlabel('Échantillons');
        ylabel('Valeurs');
        grid on;
    end
    
    % Ajuster la disposition des sous-graphiques
    sgtitle(['Graphiques pour le fichier ', num2str(i)]);
end
