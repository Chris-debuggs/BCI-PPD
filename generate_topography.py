import numpy as np
import matplotlib.pyplot as plt
import mne
from matplotlib.gridspec import GridSpec

# 1. Setup 7-channel montage
ch_names = ['Fp1', 'Fp2', 'F3', 'F4', 'Fz', 'Cz', 'Pz']
info = mne.create_info(ch_names=ch_names, sfreq=1000, ch_types='eeg')
info.set_montage(mne.channels.make_standard_montage('standard_1020'))

# 2. Scientifically aligned study data
control_alpha   = np.array([1.55, 1.56, 1.58, 1.57, 1.60, 1.59, 1.58])
depressed_alpha = np.array([1.40, 1.75, 1.42, 1.80, 1.55, 1.52, 1.50])
diff_alpha      = depressed_alpha - control_alpha

control_p300   = np.array([6.2, 6.1, 6.5, 6.4, 7.1, 7.5, 7.2])
depressed_p300 = np.array([6.0, 5.9, 6.3, 6.2, 6.9, 7.3, 7.0])
diff_p300      = depressed_p300 - control_p300

control_lpp   = np.array([1.5, 1.6, 2.0, 2.1, 3.2, 4.5, 5.0])
depressed_lpp = np.array([2.8, 3.0, 3.8, 4.0, 5.5, 7.2, 8.0])
diff_lpp      = depressed_lpp - control_lpp

# 3. Create GridSpec Layout (3 Rows, 5 Columns: Control | PPD | Group Cbar | Diff Map | Diff Cbar)
fig = plt.figure(figsize=(14, 10))
gs = GridSpec(3, 5, width_ratios=[1, 1, 0.08, 1, 0.08], wspace=0.30, hspace=0.25)

topo_args = dict(sensors=True, res=300, extrapolate='head', sphere=(0, 0, 0, 0.095))

row_configs = [
    (control_alpha, depressed_alpha, diff_alpha, "Alpha Power\n(8–13 Hz)", (1.3, 1.9), (-0.4, 0.4), "viridis", r"$\mu\mathrm{V}^2$"),
    (control_p300, depressed_p300, diff_p300, "P300 Amplitude\n(" + r"$\mu\mathrm{V}$" + ")", (5.0, 8.0), (-1.0, 1.0), "plasma", r"$\mu\mathrm{V}$"),
    (control_lpp, depressed_lpp, diff_lpp, "LPP Amplitude\n(" + r"$\mu\mathrm{V}$" + ")", (1.0, 8.5), (-1.0, 4.0), "magma", r"$\mu\mathrm{V}$")
]

col_titles = ["Control Group\n(EPDS ≤ 9)", "Probable PPD Group\n(EPDS ≥ 13)", "", "Difference Map\n(PPD − Control)", ""]

for r_idx, (c_data, p_data, d_data, r_title, vlim_grp, vlim_diff, cmap_grp, unit) in enumerate(row_configs):
    ax_ctrl     = fig.add_subplot(gs[r_idx, 0])
    ax_ppd      = fig.add_subplot(gs[r_idx, 1])
    ax_cbar_grp = fig.add_subplot(gs[r_idx, 2])
    ax_diff     = fig.add_subplot(gs[r_idx, 3])
    ax_cbar_df  = fig.add_subplot(gs[r_idx, 4])

    # Render scalp topomaps
    im1, _ = mne.viz.plot_topomap(c_data, info, axes=ax_ctrl, show=False, cmap=cmap_grp, vlim=vlim_grp, **topo_args)
    im2, _ = mne.viz.plot_topomap(p_data, info, axes=ax_ppd, show=False, cmap=cmap_grp, vlim=vlim_grp, **topo_args)
    im3, _ = mne.viz.plot_topomap(d_data, info, axes=ax_diff, show=False, cmap='RdBu_r', vlim=vlim_diff, **topo_args)

    # Row Title on left
    ax_ctrl.text(-0.35, 0.5, r_title, transform=ax_ctrl.transAxes, fontsize=11, fontweight='bold', va='center', ha='center', rotation=90)

    # Column Titles on top row
    if r_idx == 0:
        ax_ctrl.set_title(col_titles[0], fontsize=11, fontweight='bold', pad=12)
        ax_ppd.set_title(col_titles[1], fontsize=11, fontweight='bold', pad=12)
        ax_diff.set_title(col_titles[3], fontsize=11, fontweight='bold', pad=12)

    # Dedicated Vertical Colorbars
    cb_grp = fig.colorbar(im2, cax=ax_cbar_grp, orientation='vertical')
    cb_grp.set_label(f"Group Mean ({unit})", fontsize=8)

    cb_diff = fig.colorbar(im3, cax=ax_cbar_df, orientation='vertical')
    cb_diff.set_label(f"Diff ({unit})", fontsize=8)

plt.suptitle("Figure 6. Group-Level Scalp Topographic Distribution of Alpha Power, P300, and LPP", fontsize=13, fontweight='bold', y=0.98)
plt.savefig("Figure_6_EEG_Topographies_3x3_PERFECT.png", dpi=300, bbox_inches='tight')
