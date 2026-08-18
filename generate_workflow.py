import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(10, 14))
ax.set_xlim(0, 10)
ax.set_ylim(0, 14)
ax.axis('off')

# Box Drawing Helper
def draw_box(ax, x, y, w, h, text, bg_color='#EBF3FA', border_color='#2C3E50', title='', fontsize=10, bold_title=True):
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.1,rounding_size=0.15", 
                                  linewidth=1.5, edgecolor=border_color, facecolor=bg_color)
    ax.add_patch(rect)
    
    if title and text:
        ax.text(x + w/2, y + h - 0.3, title, weight='bold' if bold_title else 'normal',
                ha='center', va='top', fontsize=fontsize+1, color='#1A252C')
        ax.text(x + w/2, y + 0.3, text, ha='center', va='bottom', fontsize=fontsize-1, color='#2C3E50')
    else:
        main_text = title if title else text
        ax.text(x + w/2, y + h/2, main_text, weight='bold' if bold_title else 'normal',
                ha='center', va='center', fontsize=fontsize, color='#1A252C')

# Arrow Helper (Box-to-Box)
def draw_arrow(ax, x1, y1, x2, y2):
    ax.annotate('', xy=(x2, y2), xytext=(x1, y1),
                arrowprops=dict(arrowstyle="->", color='#2C3E50', lw=2, mutation_scale=15))

# Workflow Step Definitions
# Step 1: Participant Recruitment
draw_box(ax, 2.0, 12.8, 6.0, 0.8, "", title="Participant Recruitment (N = 34)", bg_color='#EBF3FA')
draw_arrow(ax, 5.0, 12.8, 5.0, 12.1)

# Step 2: EPDS Assessment
draw_box(ax, 2.0, 11.3, 6.0, 0.8, "", title="EPDS Assessment (Cut-offs: ≤9, 10–12, ≥13)", bg_color='#EBF3FA')
draw_arrow(ax, 5.0, 11.3, 5.0, 10.6)

# Step 3: EEG Acquisition
draw_box(ax, 2.0, 9.8, 6.0, 0.8, "OpenBCI Cyton & Daisy (7 Channels: Fp1, Fp2, F3, F4, Fz, Cz, Pz)", 
         title="EEG Acquisition", bg_color='#EBF3FA')
draw_arrow(ax, 5.0, 9.8, 5.0, 9.1)

# Step 4: Experimental Protocol (Container)
draw_box(ax, 1.5, 7.3, 7.0, 1.8, "", title="Experimental Protocol", bg_color='#E8F8F5', border_color='#16A085')
draw_box(ax, 1.8, 7.5, 3.1, 1.1, "• Eyes Closed\n• Eyes Open", title="Resting-State EEG", bg_color='#FFFFFF', border_color='#16A085', fontsize=9)
draw_box(ax, 5.1, 7.5, 3.1, 1.1, "• Positive Images\n• Negative Images\n• Neutral Images", title="Emotional Task", bg_color='#FFFFFF', border_color='#16A085', fontsize=9)
draw_arrow(ax, 5.0, 7.3, 5.0, 6.6)

# Step 5: EEG Preprocessing (Container)
draw_box(ax, 1.5, 5.3, 7.0, 1.3, "", title="EEG Preprocessing", bg_color='#FEF9E7', border_color='#F39C12')
draw_box(ax, 1.8, 5.5, 1.9, 0.6, "", title="Filtering", bg_color='#FFFFFF', border_color='#F39C12', fontsize=8)
draw_arrow(ax, 3.7, 5.8, 4.0, 5.8)
draw_box(ax, 4.0, 5.5, 2.0, 0.6, "", title="Artifact Removal", bg_color='#FFFFFF', border_color='#F39C12', fontsize=8)
draw_arrow(ax, 6.0, 5.8, 6.3, 5.8)
draw_box(ax, 6.3, 5.5, 1.9, 0.6, "", title="Segmentation", bg_color='#FFFFFF', border_color='#F39C12', fontsize=8)
draw_arrow(ax, 5.0, 5.3, 5.0, 4.6)

# Step 6: Feature Extraction (Fixed Categories including ERP)
draw_box(ax, 1.5, 3.8, 7.0, 0.8, "(Statistical, Frequency-Domain, Nonlinear, ERP Features)", 
         title="Feature Extraction (22 Features)", bg_color='#E8F8F5', border_color='#16A085')
draw_arrow(ax, 5.0, 3.8, 5.0, 3.1)

# Step 7: Statistical Analysis (Container)
draw_box(ax, 1.5, 1.6, 7.0, 1.5, "", title="Statistical Analysis", bg_color='#EBF3FA', border_color='#2980B9')
draw_box(ax, 1.8, 1.8, 3.1, 0.8, "Spearman Correlation (+ FDR)", title="Correlation Analysis", bg_color='#FFFFFF', border_color='#2980B9', fontsize=8)
draw_box(ax, 5.1, 1.8, 3.1, 0.8, "Mann–Whitney U Test (+ Effect Size)", title="Group Comparison", bg_color='#FFFFFF', border_color='#2980B9', fontsize=8)
draw_arrow(ax, 5.0, 1.6, 5.0, 0.9)

# Step 8: Biomarker Identification (Fixed Target Labels)
draw_box(ax, 1.5, 0.1, 7.0, 0.8, "Primary: LPP | Secondary: FAA, Signal Energy", 
         title="Depression Biomarker Identification", bg_color='#FDEBD0', border_color='#E67E22')

plt.title("Research Workflow for EEG-Based Depression Biomarker Identification\nin Postpartum Employed Mothers", 
          fontsize=13, fontweight='bold', pad=20, color='#1A252C')

plt.savefig("Research_Workflow_Diagram.png", dpi=300, bbox_inches='tight')
