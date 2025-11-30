import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_style("whitegrid")
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (16, 10)
plt.rcParams['font.size'] = 11

data = {
    'nodes': ['2^10', '2^11', '2^12', '2^13', '2^14', '2^15', '2^16', '2^17', '2^18', '2^19', '2^20'],
    'avg_proof_computation_us': [
        12.16, 14.81, 19.71, 21.51, 24.14, 26.62, 27.15, 29.47, 32.18, 33.85, 38.93
    ],
    'avg_proof_verification_us': [
        17.49, 20.93, 31.17, 33.61, 37.18, 40.20, 43.91, 47.63, 49.28, 55.71, 61.44
    ],
    'avg_gamma_storage_bytes': [
        161.25, 200.16, 307.95, 331.37, 354.61, 389.79, 442.23, 481.35, 486.74, 537.82, 615.29
    ],
    'avg_proof_serialized_bytes': [
        454.47, 552.86, 828.26, 888.01, 896.63, 992.84, 1171.36, 1276.52, 1294.18, 1435.67, 1687.93
    ],
    'std_proof_computation_us': [
        2.97, 6.96, 4.56, 3.84, 3.95, 3.20, 4.61, 6.73, 7.04, 9.37, 10.21
    ],
    'std_proof_verification_us': [
        5.46, 6.63, 6.38, 5.99, 6.02, 4.17, 7.58, 9.84, 10.12, 13.68, 15.47
    ],
    'std_gamma_storage_bytes': [
        62.06, 72.60, 68.21, 56.80, 46.75, 37.93, 80.26, 93.57, 97.84, 121.46, 138.72
    ],
    'std_proof_serialized_bytes': [
        157.70, 183.97, 174.11, 144.98, 119.63, 96.87, 205.20, 247.83, 253.15, 304.58, 342.91
    ],
    'max_proof_computation_us': [
        23.71, 48.38, 66.21, 49.71, 53.38, 54.67, 79.71, 103.24, 108.67, 115.83, 137.45
    ],
    'max_proof_verification_us': [
        26.67, 34.58, 43.25, 71.67, 92.33, 107.46, 118.75, 127.89, 133.24, 156.78, 189.53
    ],
    'max_gamma_storage_bytes': [
        256, 288, 352, 352, 384, 384, 512, 640, 672, 768, 960
    ],
    'max_proof_serialized_bytes': [
        696, 776, 942, 943, 1025, 1025, 1353, 1698, 1734, 1956, 2289
    ]
}

df = pd.DataFrame(data)
df['nodes_int'] = [2**i for i in range(10, 21)]
df['nodes_label'] = df['nodes']

fig, axes = plt.subplots(2, 2, figsize=(18, 12))
fig.suptitle('Skiplist Proof Performance Metrics', fontsize=20, fontweight='bold', y=0.995)

colors = sns.color_palette("rocket", 11)

ax1 = axes[0, 0]
bars1 = ax1.bar(range(len(df)), df['avg_proof_computation_us'], color=colors, edgecolor='black', linewidth=1.2, alpha=0.85)
ax1.errorbar(range(len(df)), df['avg_proof_computation_us'], yerr=df['std_proof_computation_us'], fmt='none', ecolor='darkred', capsize=5, capthick=2, alpha=0.8)
ax1.set_xlabel('Number of Nodes', fontsize=13, fontweight='bold')
ax1.set_ylabel('Time (µs)', fontsize=13, fontweight='bold')
ax1.set_title('Proof Computation Time', fontsize=15, fontweight='bold', pad=15)
ax1.set_xticks(range(len(df)))
ax1.set_xticklabels(df['nodes_label'], rotation=45, ha='right')
ax1.grid(axis='y', alpha=0.3, linestyle='--')
for i, (val, std) in enumerate(zip(df['avg_proof_computation_us'], df['std_proof_computation_us'])):
    ax1.text(i, val + std + 0.3, f'{val:.1f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

ax2 = axes[0, 1]
bars2 = ax2.bar(range(len(df)), df['avg_proof_verification_us'], color=colors, edgecolor='black', linewidth=1.2, alpha=0.85)
ax2.errorbar(range(len(df)), df['avg_proof_verification_us'], yerr=df['std_proof_verification_us'], fmt='none', ecolor='darkred', capsize=5, capthick=2, alpha=0.8)
ax2.set_xlabel('Number of Nodes', fontsize=13, fontweight='bold')
ax2.set_ylabel('Time (µs)', fontsize=13, fontweight='bold')
ax2.set_title('Proof Verification Time', fontsize=15, fontweight='bold', pad=15)
ax2.set_xticks(range(len(df)))
ax2.set_xticklabels(df['nodes_label'], rotation=45, ha='right')
ax2.grid(axis='y', alpha=0.3, linestyle='--')
for i, (val, std) in enumerate(zip(df['avg_proof_verification_us'], df['std_proof_verification_us'])):
    ax2.text(i, val + std + 1, f'{val:.1f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

ax3 = axes[1, 0]
bars3 = ax3.bar(range(len(df)), df['avg_gamma_storage_bytes'], color=colors, edgecolor='black', linewidth=1.2, alpha=0.85)
ax3.errorbar(range(len(df)), df['avg_gamma_storage_bytes'], yerr=df['std_gamma_storage_bytes'], fmt='none', ecolor='darkred', capsize=5, capthick=2, alpha=0.8)
ax3.set_xlabel('Number of Nodes', fontsize=13, fontweight='bold')
ax3.set_ylabel('Bytes', fontsize=13, fontweight='bold')
ax3.set_title('Gamma Storage Size', fontsize=15, fontweight='bold', pad=15)
ax3.set_xticks(range(len(df)))
ax3.set_xticklabels(df['nodes_label'], rotation=45, ha='right')
ax3.grid(axis='y', alpha=0.3, linestyle='--')
for i, (val, std) in enumerate(zip(df['avg_gamma_storage_bytes'], df['std_gamma_storage_bytes'])):
    ax3.text(i, val + std + 5, f'{val:.0f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

ax4 = axes[1, 1]
bars4 = ax4.bar(range(len(df)), df['avg_proof_serialized_bytes'], color=colors, edgecolor='black', linewidth=1.2, alpha=0.85)
ax4.errorbar(range(len(df)), df['avg_proof_serialized_bytes'], yerr=df['std_proof_serialized_bytes'], fmt='none', ecolor='darkred', capsize=5, capthick=2, alpha=0.8)
ax4.set_xlabel('Number of Nodes', fontsize=13, fontweight='bold')
ax4.set_ylabel('Bytes', fontsize=13, fontweight='bold')
ax4.set_title('Proof Serialized Size', fontsize=15, fontweight='bold', pad=15)
ax4.set_xticks(range(len(df)))
ax4.set_xticklabels(df['nodes_label'], rotation=45, ha='right')
ax4.grid(axis='y', alpha=0.3, linestyle='--')
for i, (val, std) in enumerate(zip(df['avg_proof_serialized_bytes'], df['std_proof_serialized_bytes'])):
    ax4.text(i, val + std + 20, f'{val:.0f}', ha='center', va='bottom', fontsize=9, fontweight='bold')

plt.tight_layout()
plt.savefig('skiplist_performance.png', dpi=300, bbox_inches='tight')
plt.show()
