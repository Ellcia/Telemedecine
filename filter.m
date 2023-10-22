% Charger le fichier CSV
data = readmatrix('output.csv');

% Supprimer la première colonne de zéros
data = data(:, 2:end);

% Points de découpe
cut_points = [2655, 5019, 7384];

% Fréquence de coupure et ordre du filtre
cutoff_frequency = 0.1;  % Fréquence de coupure en Hz
filter_order = 5;      % Ordre du filtre

% Créer une figure
figure;

% Parcourir les signaux
for i = 1:2  % Traitez uniquement les deux premiers signaux (Montée1)
    signal = data(:, i);
    
    % Extraire la première partie du signal jusqu'à x = 2655
    part1 = signal(1:cut_points(1));
    
    % Créer un vecteur pour l'axe x de la première partie
    x_part1 = 1:length(part1);
    
    % Concevoir le filtre passe-bas
    fs_part1 = 50;  % Fréquence d'échantillonnage de la première partie du signal
    lp_filter = designfilt('lowpassfir', 'FilterOrder', filter_order, 'CutoffFrequency', cutoff_frequency, 'SampleRate', fs_part1);

    % Appliquer le filtre à la première partie du signal
    %filtered_part1 = filter(lp_filter, part1);
    %filtered_part1=lowpass(part1,0.0001,50)
    h = fir1(25,0.4)
    filtered_part1=filter(h,part1)
    
    % Tracer le signal original et le signal filtré
    subplot(2, 1, i);
    plot(x_part1, part1, 'r', 'LineWidth', 2);  % Signal original en rouge
    hold on;
    plot(x_part1, filtered_part1, 'b', 'LineWidth', 2);  % Signal filtré en bleu
    
    % Titre et étiquettes
    title(['Colonne ', num2str(i), ' (Montée1)']);
    xlabel('Échantillons');
    ylabel('Valeurs');
    grid on;
    
    % Ajouter des légendes
    legend('Signal Original', 'Signal Filtré');
end

% Ajuster la disposition des sous-graphiques
sgtitle('Filtrage des deux premiers signaux (Montée1) jusqu''à x = 2655');

% Réduire l'espacement entre les sous-graphiques
tightfig;
