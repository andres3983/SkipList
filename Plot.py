import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_style("whitegrid")
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (16, 10)
plt.rcParams['font.size'] = 11

data = {
    'nodes': [1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],
    'avg_proof_computation_us': [17.14, 18.88, 21.31, 22.68, 23.45, 24.82, 25.91, 26.73, 27.89, 28.52, 29.67],
    'avg_proof_verification_us': [33.32, 34.73, 38.45, 41.79, 44.12, 46.98, 49.35, 52.84, 55.27, 58.96, 61.43],
    'avg_gamma_storage_bytes': [156.24, 178.04, 191.77, 208.45, 224.33, 238.17, 254.92, 269.48, 286.71, 301.85, 318.24],
    'avg_proof_serialized_bytes': [600.07, 685.42, 828.74, 869.96, 912.48, 957.83, 1001.27, 1048.95, 1093.64, 1142.18, 1187.92],
    'std_proof_computation_us': [1.97, 2.07, 2.64, 3.81, 2.15, 1.89, 2.47, 1.92, 2.68, 1.84, 2.93],
    'std_proof_verification_us': [9.72, 3.11, 3.03, 2.46, 3.84, 2.97, 4.21, 2.68, 3.52, 4.18, 3.76],
    'std_gamma_storage_bytes': [50.40, 52.20, 54.35, 59.27, 57.18, 60.84, 62.47, 65.93, 67.28, 70.15, 71.62],
    'std_proof_serialized_bytes': [50.64, 165.04, 54.40, 59.30, 65.82, 71.48, 77.35, 83.91, 90.27, 96.84, 103.56] 
}

df = pd.DataFrame(data)
df['nodes_label'] = df['nodes'].apply(lambda x: f'{x//1024}K' if x >= 1024 else str(x))

fig, axes = plt.subplots(2, 2, figsize=(18, 12))
fig.suptitle('Skiplist Proof Performance Metrics', fontsize=20, fontweight='bold', y=0.995)

colors = sns.color_palette("rocket", 10)

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
