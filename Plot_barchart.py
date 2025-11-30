import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman', 'Times', 'DejaVu Serif']
plt.rcParams['font.size'] = 9
plt.rcParams['axes.linewidth'] = 0.8
plt.rcParams['grid.linewidth'] = 0.5
plt.rcParams['lines.linewidth'] = 1.2
plt.rcParams['xtick.major.width'] = 0.8
plt.rcParams['ytick.major.width'] = 0.8
plt.rcParams['legend.fontsize'] = 8
plt.rcParams['legend.frameon'] = True
plt.rcParams['legend.edgecolor'] = 'black'
plt.rcParams['legend.fancybox'] = False
plt.rcParams['legend.framealpha'] = 1.0

# Data
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
    ]
}

df = pd.DataFrame(data)
x_pos = range(len(df))

colors = {
    'computation': '#2E5090',    # Blue
    'verification': '#C65D47',   # Red-orange
    'gamma': '#2F7F4F',          # Green
    'serialized': '#8B6914'      # Gold/brown
}

fig, axes = plt.subplots(2, 2, figsize=(7, 5.5))

# Plot 1: Proof Computation Time
ax1 = axes[0, 0]
bars1 = ax1.bar(x_pos, df['avg_proof_computation_us'], 
                color=colors['computation'], 
                edgecolor='black', linewidth=0.5, alpha=0.7)
ax1.errorbar(x_pos, df['avg_proof_computation_us'], 
             yerr=df['std_proof_computation_us'], 
             fmt='none', ecolor='black', capsize=2.5, 
             linewidth=0.7, alpha=0.8)
ax1.set_xlabel('Number of Nodes')
ax1.set_ylabel('Time (μs)')
ax1.set_title('(a) Proof Computation Time', fontsize=9, loc='left', pad=8)
ax1.set_xticks(x_pos[::2])
ax1.set_xticklabels(df['nodes'][::2], rotation=0)
ax1.grid(True, axis='y', alpha=0.3, linestyle='-', linewidth=0.5, color='gray')
ax1.set_axisbelow(True)
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

# Plot 2: Proof Verification Time
ax2 = axes[0, 1]
bars2 = ax2.bar(x_pos, df['avg_proof_verification_us'], 
                color=colors['verification'], 
                edgecolor='black', linewidth=0.5, alpha=0.7)
ax2.errorbar(x_pos, df['avg_proof_verification_us'], 
             yerr=df['std_proof_verification_us'], 
             fmt='none', ecolor='black', capsize=2.5, 
             linewidth=0.7, alpha=0.8)
ax2.set_xlabel('Number of Nodes')
ax2.set_ylabel('Time (μs)')
ax2.set_title('(b) Proof Verification Time', fontsize=9, loc='left', pad=8)
ax2.set_xticks(x_pos[::2])
ax2.set_xticklabels(df['nodes'][::2], rotation=0)
ax2.grid(True, axis='y', alpha=0.3, linestyle='-', linewidth=0.5, color='gray')
ax2.set_axisbelow(True)
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)

# Plot 3: Gamma Storage Size
ax3 = axes[1, 0]
bars3 = ax3.bar(x_pos, df['avg_gamma_storage_bytes'], 
                color=colors['gamma'], 
                edgecolor='black', linewidth=0.5, alpha=0.7)
ax3.errorbar(x_pos, df['avg_gamma_storage_bytes'], 
             yerr=df['std_gamma_storage_bytes'], 
             fmt='none', ecolor='black', capsize=2.5, 
             linewidth=0.7, alpha=0.8)
ax3.set_xlabel('Number of Nodes')
ax3.set_ylabel('Size (Bytes)')
ax3.set_title('(c) Gamma Storage Size', fontsize=9, loc='left', pad=8)
ax3.set_xticks(x_pos[::2])
ax3.set_xticklabels(df['nodes'][::2], rotation=0)
ax3.grid(True, axis='y', alpha=0.3, linestyle='-', linewidth=0.5, color='gray')
ax3.set_axisbelow(True)
ax3.spines['top'].set_visible(False)
ax3.spines['right'].set_visible(False)

# Plot 4: Proof Serialized Size
ax4 = axes[1, 1]
bars4 = ax4.bar(x_pos, df['avg_proof_serialized_bytes'], 
                color=colors['serialized'], 
                edgecolor='black', linewidth=0.5, alpha=0.7)
ax4.errorbar(x_pos, df['avg_proof_serialized_bytes'], 
             yerr=df['std_proof_serialized_bytes'], 
             fmt='none', ecolor='black', capsize=2.5, 
             linewidth=0.7, alpha=0.8)
ax4.set_xlabel('Number of Nodes')
ax4.set_ylabel('Size (Bytes)')
ax4.set_title('(d) Proof Serialized Size', fontsize=9, loc='left', pad=8)
ax4.set_xticks(x_pos[::2])
ax4.set_xticklabels(df['nodes'][::2], rotation=0)
ax4.grid(True, axis='y', alpha=0.3, linestyle='-', linewidth=0.5, color='gray')
ax4.set_axisbelow(True)
ax4.spines['top'].set_visible(False)
ax4.spines['right'].set_visible(False)

plt.tight_layout()

#Save as PNG
plt.savefig('skiplist_bar_performance.png', dpi=300, bbox_inches='tight')  
plt.show()

# Figure captions
print("\n" + "="*80)
print("ACM FIGURE CAPTION:")
print("="*80)
print("\nFigure 1: Skiplist proof performance metrics for varying node counts (2^10 to")
print("2^20). (a) Proof computation time demonstrates near-linear growth from 12.16 μs")
print("to 38.93 μs. (b) Verification time increases from 17.49 μs to 61.44 μs, with")
print("verification consistently requiring approximately 1.5× computation time.")
print("(c) Gamma storage and (d) serialized proof sizes show logarithmic scaling with")
print("skiplist size, with serialized proofs requiring 2-3× more space than gamma")
print("storage. Error bars indicate ±1 standard deviation.")
print("="*80)

print("\nFIGURE DESCRIPTION (for ACM accessibility requirements):")
print("="*80)
print("Four bar charts showing skiplist proof performance. Top left: computation time")
print("increases from 12μs to 39μs. Top right: verification time increases from 17μs")
print("to 61μs. Bottom left: gamma storage grows from 161 to 615 bytes. Bottom right:")
print("serialized proof size grows from 454 to 1688 bytes. All charts show increasing")
print("trends with error bars representing standard deviation.")
print("="*80)
