import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib.image as mpimg
from matplotlib.offsetbox import OffsetImage, AnnotationBbox

fig, ax = plt.subplots(figsize=(10, 18))
ax.set_xlim(0, 10)
ax.set_ylim(-3.5, 16.2) # Shifted bottom bound down to -3.5
ax.axis('off')

# Box Drawing Helper
def draw_box(ax, x, y, w, h, title='', text='', bg='#EBF3FA', border='#2C3E50', fontsize=10):
    rect = patches.FancyBboxPatch((x, y), w, h, boxstyle="round,pad=0.05,rounding_size=0.12", 
                                  linewidth=1.5, edgecolor=border, facecolor=bg)
    ax.add_patch(rect)
    
    if title and text:
        ax.text(x + w/2, y + h - 0.2, title, weight='bold', ha='center', va='top', fontsize=fontsize, color='#1A252C')
        ax.text(x + w/2, y + 0.2, text, ha='center', va='bottom', fontsize=fontsize-1, color='#2C3E50')
    elif title:
        ax.text(x + w/2, y + h/2, title, weight='bold', ha='center', va='center', fontsize=fontsize, color='#1A252C')
    elif text:
        ax.text(x + w/2, y + h/2, text, ha='center', va='center', fontsize=fontsize, color='#2C3E50')

def draw_arrow(ax, y_start, y_end, x=5.0):
    ax.annotate('', xy=(x, y_end), xytext=(x, y_start),
                arrowprops=dict(arrowstyle="->", color='#2C3E50', lw=2, mutation_scale=15))

# Header Title
ax.text(5.0, 15.5, "Research Workflow for EEG-Based Depression Biomarker Identification\nin Postpartum Employed Mothers", 
        fontsize=13, fontweight='bold', ha='center', va='center', color='#1A252C')

# Step 1: Participant Recruitment
draw_box(ax, 2.0, 14.3, 6.0, 0.7, title="Participant Recruitment (N = 34)")
draw_arrow(ax, 14.3, 13.6)

# Step 2: EPDS Assessment
draw_box(ax, 2.0, 12.9, 6.0, 0.7, title="EPDS Assessment (Cut-offs: ≤9, 10–12, ≥13)")
draw_arrow(ax, 12.9, 12.2)

# Step 3: EEG Acquisition
draw_box(ax, 2.0, 11.2, 6.0, 1.0, title="EEG Acquisition", text="OpenBCI Cyton & Daisy (7 Channels: Fp1, Fp2, F3, F4, Fz, Cz, Pz)")
draw_arrow(ax, 11.2, 10.5)

# Step 4: Experimental Protocol (Container Box)
draw_box(ax, 1.5, 8.2, 7.0, 2.3, bg='#E8F8F5', border='#16A085')
ax.text(5.0, 10.2, "Experimental Protocol", weight='bold', ha='center', va='top', fontsize=11, color='#16A085')
draw_box(ax, 1.8, 8.4, 3.1, 1.4, title="Resting-State EEG", text="• Eyes Closed\n• Eyes Open", bg='#FFFFFF', border='#16A085', fontsize=9)
draw_box(ax, 5.1, 8.4, 3.1, 1.4, title="Emotional Task", text="• Positive Images\n• Negative Images\n• Neutral Images", bg='#FFFFFF', border='#16A085', fontsize=9)
draw_arrow(ax, 8.2, 7.5)

# Step 5: EEG Preprocessing (Container Box)
draw_box(ax, 1.5, 5.7, 7.0, 1.8, bg='#FEF9E7', border='#F39C12')
ax.text(5.0, 7.2, "EEG Preprocessing", weight='bold', ha='center', va='top', fontsize=11, color='#D35400')
draw_box(ax, 1.8, 5.9, 1.8, 0.8, title="Filtering", bg='#FFFFFF', border='#F39C12', fontsize=9)
ax.annotate('', xy=(4.0, 6.3), xytext=(3.6, 6.3), arrowprops=dict(arrowstyle="->", color='#F39C12', lw=1.5))
draw_box(ax, 4.0, 5.9, 2.0, 0.8, title="Artifact Removal", bg='#FFFFFF', border='#F39C12', fontsize=9)
ax.annotate('', xy=(6.3, 6.3), xytext=(6.0, 6.3), arrowprops=dict(arrowstyle="->", color='#F39C12', lw=1.5))
draw_box(ax, 6.3, 5.9, 1.8, 0.8, title="Segmentation", bg='#FFFFFF', border='#F39C12', fontsize=9)
draw_arrow(ax, 5.7, 5.0)

# Step 6: Feature Extraction
draw_box(ax, 1.5, 4.0, 7.0, 1.0, title="Feature Extraction (22 Features)", 
         text="Statistical, Frequency-Domain, Nonlinear, ERP Features", bg='#E8F8F5', border='#16A085')
draw_arrow(ax, 4.0, 3.3)

# Step 7: Statistical Analysis (Container Box)
draw_box(ax, 1.5, 1.5, 7.0, 1.8, bg='#EBF3FA', border='#2980B9')
ax.text(5.0, 3.0, "Statistical Analysis", weight='bold', ha='center', va='top', fontsize=11, color='#2980B9')
draw_box(ax, 1.8, 1.7, 3.1, 1.0, title="Correlation Analysis", text="Spearman Correlation (+ FDR)", bg='#FFFFFF', border='#2980B9', fontsize=8)
draw_box(ax, 5.1, 1.7, 3.1, 1.0, title="Group Comparison", text="Mann–Whitney U Test (+ Effect Size)", bg='#FFFFFF', border='#2980B9', fontsize=8)
draw_arrow(ax, 1.5, 0.85)

# INSERT IMAGE HERE (Scaled down and placed in a container)
try:
    img = mpimg.imread(r'C:\Users\cnevi\Projects\BCI-PPD\sample_image.png')
    # Reduced zoom to make the image much smaller
    imagebox = OffsetImage(img, zoom=0.25) 
    # Placement at x=5.0, y=-0.6, with a visible bounding box (square canvas)
    ab = AnnotationBbox(imagebox, (5.0, -0.3), frameon=False, 
                        bboxprops=dict(edgecolor='#2C3E50', facecolor='#FFFFFF', boxstyle="round,pad=0.8", lw=1.5))
    ax.add_artist(ab)
    
    # Draw arrow from image down to the final box
    # draw_arrow(ax, -1.5, -2.2)
except Exception as e:
    print(f"Error loading image: {e}")

# Step 8: Biomarker Identification (Lifted up above y=0)
draw_box(ax, 1.5, -2.5, 7.0, 0.8, title="Depression Biomarker Identification", 
         text="Primary: LPP | Secondary: Frontal Alpha Asymmetry, Signal Energy", bg='#FDEBD0', border='#E67E22')

plt.savefig("Research_Workflow_Diagram_PERFECT.png", dpi=300, bbox_inches='tight')