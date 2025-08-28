import more_itertools as mit
import numpy as np

y_pred_test = clf_t.predict(data_test) # predictions (time-series with values 1 and 0, one value per window) 
y_t_test = anom_test # test (time-series with values 1 and 0, one value per window)

l_anom = 1 # minimum of overlapped anomalies between test and predicted sequences.

# Selection of anomalies
print("Selecting anomalies")

result_row = {
        'false_positives': 0,
        'false_negatives': 0,
        'true_positives': 0,
        'fp_sequences': [],
        'tp_sequences': [],
        'num_true_anoms': 0,
        #'train_df': [*list(train_df_puntual['chan_id']), *list(train_df_change['chan_id']), *list(train_df_frequency['chan_id']), *list(train_df_magnitude['chan_id']), *list(train_df_wave['chan_id'])],
        #'test_df': [*list(test_df_puntual['chan_id']), *list(test_df_change['chan_id']), *list(test_df_frequency['chan_id']), *list(test_df_magnitude['chan_id']), *list(test_df_wave['chan_id'])],
    }

matched_true_seqs = []

# ground truth
i_true_anom = [i for i, j in enumerate(y_t_test) if j == 1]
groups_true = [list(group) for group in mit.consecutive_groups(i_true_anom)]
seq_true = [(int(g[0]), int(g[-1])) for g in groups_true] #if not g[0] == g[-1]]
result_row['num_true_anoms'] = len(seq_true)
result_row['num_detectors'] = 1

# predicted
i_anom = [i for i, j in enumerate(y_pred_test) if j == 1]
groups = [list(group) for group in mit.consecutive_groups(i_anom)]
E_seq = [(int(g[0]), int(g[-1])) for g in groups ] #if not g[0] == g[-1]]

#print("E_seq: ", E_seq)

if len(E_seq) == 0:
    result_row['false_negatives'] = result_row['num_true_anoms']
else:
    i=0
    while(i<len(E_seq)):
        e = E_seq[i]
        ind1 = e[0]
        ind2 = e[1]
        if(i>0):
            inda1 = E_seq[i-1][0]
            inda2 = E_seq[i-1][1]
            #print("Anterior: "+ str(E_seq[i-1])+"Actual", str(e))
            if(ind1<=inda2+l_anom):
                #print("Sii")
                E_seq[i-1] = (inda1,ind2)
                del E_seq[i]
            else: i=i+1
        else: i=i+1

    true_indices_grouped = [list(range(e[0], e[1]+1)) for e in seq_true]
    true_indices_flat = set([i for group in true_indices_grouped for i in group])

    for e_seq in E_seq:
        i_anom_predicted = set(range(e_seq[0], e_seq[1]+1))

        matched_indices = list(i_anom_predicted & true_indices_flat)
        valid = True if len(matched_indices) > 0 else False

        if valid:
            result_row['tp_sequences'].append(e_seq)
            true_seq_index = [i for i in range(len(true_indices_grouped)) if
                          len(np.intersect1d(list(i_anom_predicted), true_indices_grouped[i])) > 0]

            if not true_seq_index[0] in matched_true_seqs:
                matched_true_seqs.append(true_seq_index[0])
                result_row['true_positives'] += 1

        else:
            result_row['fp_sequences'].append([e_seq[0], e_seq[1]])
            result_row['false_positives'] += 1

    result_row['false_negatives'] = len(np.delete(seq_true, matched_true_seqs, axis=0))
result_row['anomaly_sequences'] = seq_true

results.append(result_row)
    #result_df = pd.DataFrame(results)

    #with open('results_lw_{}_nf_{}.csv'.format(l_w,npersegFFT),'w') as f:
    #    f.write('\n')    
    #result_df.to_csv('results_lw_{}_nf_{}.csv'.format(l_w,npersegFFT), index = False, header = False, mode='a')
    #result_df.to_csv('results_lw_{}_nf_{}_lanom_{}.csv'.format(l_w,npersegFFT,l_anom),index=False)

    #print("Saving ...")