% Charger le fichier CSV
data = readmatrix('output.csv');

% Supprimer la première colonne de zéros
data = data(:, 2:end);

% Points de découpe
cut_points = [2655, 5019, 7384];

% Initialiser quatre matrices pour stocker les parties découpées
part1 = [];
part2 = [];
part3 = [];
part4 = [];

% Parcourir les signaux
for i = 1:4
    signal = data(:, i);
    
    % Découper le signal en quatre parties
    part1(:, end+1) = signal(1:cut_points(1));
    part2(:, end+1) = signal(cut_points(1)+1:cut_points(2));
    part3(:, end+1) = signal(cut_points(2)+1:cut_points(3));
    part4(:, end+1) = signal(cut_points(3)+1:end);
end

% Enregistrer les matrices dans des fichiers CSV distincts
writematrix(part1, 'part1.csv');
writematrix(part2, 'part2.csv');
writematrix(part3, 'part3.csv');
writematrix(part4, 'part4.csv');
