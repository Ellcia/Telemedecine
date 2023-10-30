function [filteredData] = filterData(data, cutoff_frequency, sampling_frequency, order, window_size)
    % Sélectionner les colonnes correspondantes
    signal1 = data(:, 1);
    signal2 = data(:, 2);
    signal3 = data(:, 3);
    signal4 = data(:, 4);

    % Créer le filtre passe-bas
    [b, a] = butter(order, cutoff_frequency / (sampling_frequency / 2), 'low');

    % Appliquer le filtre aux signaux
    filtered_signal1 = filter(b, a, signal1);
    filtered_signal2 = filter(b, a, signal2);

    % Appliquer la moyenne glissante aux signaux
    smoothed_signal3 = smoothdata(signal3, 'movmean', window_size);
    smoothed_signal4 = smoothdata(signal4, 'movmean', window_size);

    % Remplacer les colonnes originales par les versions filtrées et lissées
    filteredData = data;
    filteredData(:, 1) = filtered_signal1;
    filteredData(:, 2) = filtered_signal2;
    filteredData(:, 3) = smoothed_signal3;
    filteredData(:, 4) = smoothed_signal4;

    % Affichage des graphiques
%     x = 1:length(signal1);
%     figure;
%     subplot(2, 1, 1);
%     plot(x, signal1, 'b', 'LineWidth', 2);
%     hold on;
%     plot(x, filtered_signal1, 'g', 'LineWidth', 2);
%     title('Signal 1 - Original vs Filtré');
%     xlabel('Échantillons');
%     ylabel('Valeurs');
%     legend('Signal 1 Original', 'Signal 1 Filtré');
%     grid on;
% 
%     subplot(2, 1, 2);
%     plot(x, signal2, 'r', 'LineWidth', 2);
%     hold on;
%     plot(x, filtered_signal2, 'm', 'LineWidth', 2);
%     title('Signal 2 - Original vs Filtré');
%     xlabel('Échantillons');
%     ylabel('Valeurs');
%     legend('Signal 2 Original', 'Signal 2 Filtré');
%     grid on;
% 
%     % Affichage des graphiques pour les autres signaux
%     x = 1:length(signal3);
%     figure;
%     subplot(2, 1, 1);
%     plot(x, signal3, 'b', 'LineWidth', 2);
%     hold on;
%     plot(x, smoothed_signal3, 'g', 'LineWidth', 2);
%     title('Signal 3 - Original vs Lissé');
%     xlabel('Échantillons');
%     ylabel('Valeurs');
%     legend('Signal 3 Original', 'Signal 3 Lissé');
%     grid on;
% 
%     subplot(2, 1, 2);
%     plot(x, signal4, 'r', 'LineWidth', 2);
%     hold on;
%     plot(x, smoothed_signal4, 'm', 'LineWidth', 2);
%     title('Signal 4 - Original vs Lissé');
%     xlabel('Échantillons');
%     ylabel('Valeurs');
%     legend('Signal 4 Original', 'Signal 4 Lissé');
%     grid on;
end

