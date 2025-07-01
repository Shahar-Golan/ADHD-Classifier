from sklearn.metrics import precision_recall_curve, average_precision_score
import matplotlib.pyplot as plt
from sklearn.metrics import precision_score, recall_score
from running_models import rf_pipe, X_test_rf, y_test_rf
from under_sampling import model_bal, X_test_final_bal, y_test_final_bal

probs = rf_pipe.predict_proba(X_test_rf)

precision_pos, recall_pos, _ = precision_recall_curve(y_test_rf, probs[:, 1])
ap_pos = average_precision_score(y_test_rf, probs[:, 1])

y_zero = (y_test_rf == 0).astype(int)
precision_neg, recall_neg, _ = precision_recall_curve(y_zero, probs[:, 0])
ap_neg = average_precision_score(y_zero, probs[:, 0])

plt.figure(figsize=(8, 6))
plt.plot(recall_pos, precision_pos, lw=2, label=f"ADHD (1)    AP = {ap_pos:.2f}")
plt.plot(recall_neg, precision_neg, lw=2, label=f"No ADHD (0) AP = {ap_neg:.2f}")
plt.xlabel("Recall")
plt.ylabel("Precision")
plt.title("Precision–Recall Curves for Both Classes")
plt.legend(loc="best")
plt.grid(True)
plt.tight_layout()
plt.show()


def plot_threshold_metrics(model, X, y, title, thresholds=[0.5, 0.6, 0.7, 0.8]):
    y_scores = model.predict_proba(X)[:, 1]
    prec_adhd = []
    rec_adhd = []
    prec_no = []
    rec_no = []

    for thr in thresholds:
        y_pred = (y_scores >= thr).astype(int)
        prec_adhd.append(precision_score(y, y_pred, pos_label=1))
        rec_adhd.append(recall_score(y, y_pred, pos_label=1))
        prec_no.append(precision_score(y, y_pred, pos_label=0))
        rec_no.append(recall_score(y, y_pred, pos_label=0))

    plt.figure(figsize=(10, 6))
    plt.plot(thresholds, prec_adhd, marker='o', label='Precision ADHD')
    plt.plot(thresholds, rec_adhd, marker='o', label='Recall ADHD')
    plt.plot(thresholds, prec_no, marker='o', label='Precision No ADHD')
    plt.plot(thresholds, rec_no, marker='o', label='Recall No ADHD')
    plt.xlabel('Probability Threshold')
    plt.ylabel('Score')
    plt.title(title)
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # ─── Cell 4: run threshold evaluation on both original & balanced test sets ───
    # Usage example:
    title1 = "Original Dataset"
    plot_threshold_metrics(rf_pipe, X_test_rf, y_test_rf, title1)

    title2 = "Balanced Dataset"
    plot_threshold_metrics(model_bal, X_test_final_bal, y_test_final_bal, title2)
