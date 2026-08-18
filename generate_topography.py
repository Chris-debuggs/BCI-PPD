import numpy as np
import matplotlib.pyplot as plt
import mne
import os

def create_topography():
    # 1. Define your 7 electrode names matching the standard 10–20 system
    ch_names = ['Fp1', 'Fp2', 'F3', 'F4', 'Fz', 'Cz', 'Pz']

    # 2. Create MNE info structure and apply standard 10–20 electrode coordinates
    info = mne.create_info(ch_names=ch_names, sfreq=1000, ch_types='eeg')
    montage = mne.channels.make_standard_montage('standard_1020')
    info.set_montage(montage)

    # 3. Channel-wise mean values for your 7 electrodes [Fp1, Fp2, F3, F4, Fz, Cz, Pz]
    # DUMMY DATA FOR ALPHA POWER
    control_alpha   = np.array([1.2, 1.3, 1.5, 1.4, 1.6, 1.8, 2.0])  
    depressed_alpha = np.array([1.1, 2.8, 1.2, 2.9, 1.5, 1.4, 1.3])  
    diff_alpha      = depressed_alpha - control_alpha                

    # DUMMY DATA FOR P300 AMPLITUDE
    control_p300   = np.array([3.5, 3.6, 4.0, 4.2, 6.0, 8.5, 9.0])
    depressed_p300 = np.array([2.5, 2.6, 3.0, 3.2, 4.0, 5.0, 5.5])
    diff_p300      = depressed_p300 - control_p300

    # DUMMY DATA FOR LPP AMPLITUDE
    control_lpp    = np.array([2.0, 2.1, 2.5, 2.7, 4.5, 6.0, 7.5])
    depressed_lpp  = np.array([1.2, 1.3, 1.6, 1.8, 2.5, 3.0, 3.5])
    diff_lpp       = depressed_lpp - control_lpp

    # 4. Set up figure layout (3 rows, 3 columns)
    fig, axes = plt.subplots(3, 3, figsize=(14, 14))

    # Common plot settings for 7-channel interpolation
    topo_args = dict(
        sensors=True,           # Draw electrode dots
        res=300,                # Image resolution
        extrapolate='head',     # Extrapolate smooth color gradient to head boundary
        sphere=(0, 0, 0, 0.095) # Standard head sphere outline
    )

    # --- ROW 1: ALPHA POWER ---
    im1, _ = mne.viz.plot_topomap(
        control_alpha, info, axes=axes[0, 0], show=False, 
        cmap='viridis', vlim=(1.0, 3.0), **topo_args
    )
    axes[0, 0].set_title('Control Group\n(EPDS ≤ 9)', fontsize=12, fontweight='bold')
    axes[0, 0].set_ylabel('Alpha Power\n(8-13 Hz)', fontsize=14, fontweight='bold', labelpad=40)

    im2, _ = mne.viz.plot_topomap(
        depressed_alpha, info, axes=axes[0, 1], show=False, 
        cmap='viridis', vlim=(1.0, 3.0), **topo_args
    )
    axes[0, 1].set_title('Probable PPD Group\n(EPDS ≥ 13)', fontsize=12, fontweight='bold')

    im3, _ = mne.viz.plot_topomap(
        diff_alpha, info, axes=axes[0, 2], show=False, 
        cmap='RdBu_r', vlim=(-2.0, 2.0), **topo_args
    )
    axes[0, 2].set_title('Difference Map\n(PPD − Control)', fontsize=12, fontweight='bold')

    # Add colorbars for Row 1
    cbar1 = plt.colorbar(im2, ax=axes[0, 1], orientation='vertical', fraction=0.046, pad=0.04)
    cbar1.set_label(r'Absolute Power ($\mu\mathrm{V}^2$)', fontsize=10)
    
    cbar2 = plt.colorbar(im3, ax=axes[0, 2], orientation='vertical', fraction=0.046, pad=0.04)
    cbar2.set_label(r'Power Diff ($\Delta\mu\mathrm{V}^2$)', fontsize=10)


    # --- ROW 2: P300 AMPLITUDE ---
    im4, _ = mne.viz.plot_topomap(
        control_p300, info, axes=axes[1, 0], show=False, 
        cmap='plasma', vlim=(2.0, 10.0), **topo_args
    )
    axes[1, 0].set_ylabel('P300 Amplitude\n(μV)', fontsize=14, fontweight='bold', labelpad=40)

    im5, _ = mne.viz.plot_topomap(
        depressed_p300, info, axes=axes[1, 1], show=False, 
        cmap='plasma', vlim=(2.0, 10.0), **topo_args
    )

    im6, _ = mne.viz.plot_topomap(
        diff_p300, info, axes=axes[1, 2], show=False, 
        cmap='RdBu_r', vlim=(-4.0, 4.0), **topo_args
    )
    
    # Add colorbars for Row 2
    cbar3 = plt.colorbar(im5, ax=axes[1, 1], orientation='vertical', fraction=0.046, pad=0.04)
    cbar3.set_label(r'Amplitude ($\mu\mathrm{V}$)', fontsize=10)
    
    cbar4 = plt.colorbar(im6, ax=axes[1, 2], orientation='vertical', fraction=0.046, pad=0.04)
    cbar4.set_label(r'Amplitude Diff ($\Delta\mu\mathrm{V}$)', fontsize=10)


    # --- ROW 3: LPP AMPLITUDE ---
    im7, _ = mne.viz.plot_topomap(
        control_lpp, info, axes=axes[2, 0], show=False, 
        cmap='magma', vlim=(1.0, 8.0), **topo_args
    )
    axes[2, 0].set_ylabel('LPP Amplitude\n(μV)', fontsize=14, fontweight='bold', labelpad=40)

    im8, _ = mne.viz.plot_topomap(
        depressed_lpp, info, axes=axes[2, 1], show=False, 
        cmap='magma', vlim=(1.0, 8.0), **topo_args
    )

    im9, _ = mne.viz.plot_topomap(
        diff_lpp, info, axes=axes[2, 2], show=False, 
        cmap='RdBu_r', vlim=(-4.0, 4.0), **topo_args
    )
    
    # Add colorbars for Row 3
    cbar5 = plt.colorbar(im8, ax=axes[2, 1], orientation='vertical', fraction=0.046, pad=0.04)
    cbar5.set_label(r'Amplitude ($\mu\mathrm{V}$)', fontsize=10)
    
    cbar6 = plt.colorbar(im9, ax=axes[2, 2], orientation='vertical', fraction=0.046, pad=0.04)
    cbar6.set_label(r'Amplitude Diff ($\Delta\mu\mathrm{V}$)', fontsize=10)


    plt.suptitle('Figure 6. Group-Level Scalp Topographic Distribution of Alpha Power, P300, and LPP', 
                 fontsize=18, fontweight='bold', y=0.95)
    plt.subplots_adjust(wspace=0.3, hspace=0.3)

    # Save high-resolution vector image for paper submission
    out_path = 'Figure_6_EEG_Topographies_3x3.png'
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    print(f"Topography grid successfully saved to {os.path.abspath(out_path)}")
    plt.close()

if __name__ == '__main__':
    create_topography()
