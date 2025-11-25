import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

sns.set_style("whitegrid")
sns.set_palette("husl")
plt.rcParams['figure.figsize'] = (16, 10)
plt.rcParams['font.size'] = 11

data = {
    'nodes': [2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576],
    'avg_proof_computation_us': [15.2, 18.9, 21.8, 26.3, 29.1, 35.2, 39.8, 46.3, 52.1, 58.7],
    'avg_proof_verification_us': [28.5, 32.7, 36.2, 41.8, 45.3, 51.9, 57.2, 64.8, 71.3, 78.1],
    'avg_gamma_storage_bytes': [178.3, 195.7, 209.1, 226.4, 243.2, 258.9, 274.6, 290.1, 307.5, 322.8],
    'avg_proof_serialized_bytes': [895.2, 1025.8, 1142.3, 1288.9, 1405.2, 1558.7, 1663.4, 1812.5, 1921.8, 2078.3],
    'std_proof_computation_us': [2.3, 1.8, 3.2, 2.9, 4.1, 3.8, 5.2, 6.1, 5.8, 7.5],
    'std_proof_verification_us': [1.9, 2.5, 2.3, 3.4, 3.1, 4.5, 4.2, 5.8, 6.3, 6.8],
    'std_gamma_storage_bytes': [54.2, 56.8, 61.3, 68.9, 74.2, 79.8, 86.5, 92.1, 98.7, 105.3],
    'std_proof_serialized_bytes': [42.3, 58.9, 51.2, 73.8, 82.1, 95.3, 88.7, 118.4, 121.9, 142.6]
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

print("✓ Visualization saved as 'skiplist_performance.png'")
print(f"✓ Analyzed {len(df)} benchmark results from {df['nodes'].min():,} to {df['nodes'].max():,} nodes")
