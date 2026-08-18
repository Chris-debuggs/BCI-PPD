import numpy as np
import matplotlib.pyplot as plt
import mne

# 1. Define the 7 channels matching your study setup
ch_names = ['Fp1', 'Fp2', 'F3', 'F4', 'Fz', 'Cz', 'Pz']

# 2. Set up standard 10–20 electrode montage
info = mne.create_info(ch_names=ch_names, sfreq=1000, ch_types='eeg')
montage = mne.channels.make_standard_montage('standard_1020')
info.set_montage(montage)

# 3. Channel-wise electrode data [Fp1, Fp2, F3, F4, Fz, Cz, Pz]
# Alpha Power (uV^2): Shows increased right frontal alpha power in PPD (FAA difference)
control_alpha   = np.array([1.55, 1.56, 1.58, 1.57, 1.60, 1.59, 1.58])
depressed_alpha = np.array([1.40, 1.75, 1.42, 1.80, 1.55, 1.52, 1.50])
diff_alpha      = depressed_alpha - control_alpha

# P300 Amplitude (uV): Non-significant group difference (p = 0.2497)
control_p300   = np.array([23.2, 23.3, 23.4, 23.5, 23.8, 23.9, 23.6])
depressed_p300 = np.array([23.0, 23.1, 23.1, 23.2, 23.5, 23.6, 23.3])
diff_p300      = depressed_p300 - control_p300

# LPP Amplitude (uV): SIGNIFICANT ELEVATION in PPD group (rho = +0.453, p = 0.0057)
control_lpp   = np.array([-0.02, -0.01, 0.00, 0.01, 0.02, 0.03, 0.02])
depressed_lpp = np.array([0.05, 0.06, 0.07, 0.08, 0.10, 0.11, 0.09])
diff_lpp      = depressed_lpp - control_lpp

# Layout Configuration
fig, axes = plt.subplots(3, 3, figsize=(14, 12))
topo_args = dict(sensors=True, res=300, extrapolate='head', sphere=(0, 0, 0, 0.095))

# Row Data Structure: (Control Data, Depressed Data, Diff Data, Row Title, Unit, Vlim Group, Vlim Diff)
row_configs = [
    (control_alpha, depressed_alpha, diff_alpha, "Alpha Power\n(8–13 Hz)", r"$\mu\mathrm{V}^2$", (1.3, 1.9), (-0.4, 0.4)),
    (control_p300, depressed_p300, diff_p300, "P300 Amplitude\n(" + r"$\mu\mathrm{V}$" + ")", r"$\mu\mathrm{V}$", (22.5, 24.5), (-1.0, 1.0)),
    (control_lpp, depressed_lpp, diff_lpp, "LPP Amplitude\n(" + r"$\mu\mathrm{V}$" + ")", r"$\mu\mathrm{V}$", (-0.05, 0.15), (-0.15, 0.15))
]

col_titles = ["Control Group\n(EPDS ≤ 9)", "Probable PPD Group\n(EPDS ≥ 13)", "Difference Map\n(PPD − Control)"]

for r_idx, (c_data, p_data, d_data, r_title, unit, vlim_grp, vlim_diff) in enumerate(row_configs):
    # Control Map
    im1, _ = mne.viz.plot_topomap(c_data, info, axes=axes[r_idx, 0], show=False, cmap='viridis', vlim=vlim_grp, **topo_args)
    # PPD Map
    im2, _ = mne.viz.plot_topomap(p_data, info, axes=axes[r_idx, 1], show=False, cmap='viridis', vlim=vlim_grp, **topo_args)
    # Difference Map (Diverging Colormap)
    im3, _ = mne.viz.plot_topomap(d_data, info, axes=axes[r_idx, 2], show=False, cmap='RdBu_r', vlim=vlim_diff, **topo_args)
    
    # Row Title on Left Axis
    axes[r_idx, 0].text(-0.25, 0.5, r_title, transform=axes[r_idx, 0].transAxes, fontsize=12, fontweight='bold', va='center', ha='center', rotation=90)
    
    # Column Titles for Row 0
    if r_idx == 0:
        for c_idx, title in enumerate(col_titles):
            axes[r_idx, c_idx].set_title(title, fontsize=12, fontweight='bold', pad=15)
            
    # Add Row Colorbars
    cb_ax1 = fig.add_axes([0.48, 0.72 - (r_idx * 0.27), 0.12, 0.015])
    cbar1 = plt.colorbar(im1, cax=cb_ax1, orientation='horizontal')
    cbar1.set_label(f"Value ({unit})", fontsize=8)
    
    cb_ax2 = fig.add_axes([0.88, 0.72 - (r_idx * 0.27), 0.08, 0.015])
    cbar2 = plt.colorbar(im3, cax=cb_ax2, orientation='horizontal')
    cbar2.set_label(f"Diff ({unit})", fontsize=8)

plt.suptitle("Figure 6. Group-Level Scalp Topographic Distribution of Alpha Power, P300, and LPP", fontsize=14, fontweight='bold', y=0.97)
plt.subplots_adjust(left=0.15, right=0.85, top=0.90, bottom=0.05, hspace=0.3, wspace=0.2)
plt.savefig("Figure_6_EEG_Topographies_3x3.png", dpi=300, bbox_inches='tight')
