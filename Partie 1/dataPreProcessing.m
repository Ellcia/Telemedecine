function dataPreProcessing(inputFile, date, cutPoints)
    % Charger le fichier CSV
    data = readmatrix('data_csv_raw\'+inputFile+'.csv');

 % Supprimer la première colonne de zéros
    data = data(:, 2:end);

    numCuts = length(cutPoints);

    % Initialiser des cellules pour stocker les parties découpées
    parts = cell(1, numCuts + 1);
    
    % Parcourir les signaux
    for i = 1:size(data, 2)
        signal = data(:, i);
        
        % Découper le signal en parties
        for j = 1:numCuts
            if j == 1
                parts{j}(:, end+1) = signal(1:cutPoints(j));
            else
                parts{j}(:, end+1) = signal(cutPoints(j-1)+1:cutPoints(j));
            end
        end
        
        % Dernière partie
        parts{numCuts + 1}(:, end+1) = signal(cutPoints(end)+1:end);
    end

    % Appliquer le filtrage et la lissage à chaque partie
    cutoff_frequency = 2;
    sampling_frequency = 50;
    order = 4;
    window_size = 5;
    
% Générer la date de départ
    dateStart = datetime(date, 'InputFormat', 'yyyy-MM-dd_HH-mm-ss');

    for i = 1:numCuts + 1
        parts{i} = filterData(parts{i}, cutoff_frequency, sampling_frequency, order, window_size);
        if i == 1
            newDateStr=date;
        end

        if i > 1
            % Calculer le décalage de temps en secondes pour le nom du fichier
            timeOffset = (size(parts{i-1}, 1) / sampling_frequency)

            % Ajouter le décalage de temps à la date de départ
            newDate = dateStart + seconds(timeOffset);

            % Mettre à jour la date de départ pour le fichier suivant
            dateStart = newDate;

            % Convertir la nouvelle date en format de chaîne avec le bon ordre
            newDateStr = string(newDate, 'yyyy-MM-dd_HH-mm-ss');
        end

        % Générer le nom du fichier de sortie avec la date modifiée
        outputFile = 'data_csv_processed\'+ inputFile + '_'+ num2str(i)+ '_'+ newDateStr+ '.csv';

        % Enregistrer la partie dans le fichier de sortie
        writematrix(parts{i}, outputFile);
    end
end