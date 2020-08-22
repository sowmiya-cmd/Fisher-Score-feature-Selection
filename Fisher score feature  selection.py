Fisher Score Feature selection
fisher_score = chi2(X_train, y_train)
fisher_score
p_values = pd.Series(fisher_score[1])

p_values.sort_values(ascending=False)
