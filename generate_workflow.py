import matplotlib.pyplot as plt
import matplotlib.patches as patches
import os

def create_workflow():
    fig, ax = plt.subplots(figsize=(10, 16))
    ax.axis('off')
    
    # Coordinates and sizes
    box_width = 6
    box_height = 0.8
    center_x = 5
    
    y_start = 14.5
    y_step = -1.6
    
    def draw_box(ax, x, y, width, height, text, bg_color='#E5F0FA', edge_color='#2C3E50', text_size=12, fontweight='normal'):
        rect = patches.FancyBboxPatch(
            (x - width/2, y - height/2), width, height,
            boxstyle="round,pad=0.1,rounding_size=0.1",
            linewidth=1.5, edgecolor=edge_color, facecolor=bg_color
        )
        ax.add_patch(rect)
        ax.text(x, y, text, ha='center', va='center', fontsize=text_size, fontweight=fontweight, color='#2C3E50', wrap=True)

    def draw_arrow(ax, x, y_from, y_to):
        ax.annotate('', xy=(x, y_to), xytext=(x, y_from),
                    arrowprops=dict(arrowstyle="->", color='#2C3E50', lw=2, mutation_scale=20))

    # Title
    ax.text(center_x, y_start + 1.2, "Research Workflow for EEG-Based Depression Biomarker Identification\nin Postpartum Employed Mothers", 
            ha='center', va='center', fontsize=16, fontweight='bold', color='#2C3E50')
    
    # 1. Participant Recruitment
    y_current = y_start
    draw_box(ax, center_x, y_current, box_width, box_height, "Participant Recruitment")
    
    # 2. EPDS Assessment
    draw_arrow(ax, center_x, y_current - box_height/2, y_current + y_step + box_height/2)
    y_current += y_step
    draw_box(ax, center_x, y_current, box_width, box_height, "EPDS Assessment")

    # 3. EEG Acquisition
    draw_arrow(ax, center_x, y_current - box_height/2, y_current + y_step + box_height/2)
    y_current += y_step
    draw_box(ax, center_x, y_current, box_width, box_height, "EEG Acquisition\n(OpenBCI Cyton & Daisy + 7 Channels)", bg_color='#F0F4F8')

    # 4. Experimental Protocol
    draw_arrow(ax, center_x, y_current - box_height/2, y_current + y_step + box_height/2 - 0.4)
    y_current += (y_step - 0.4)
    protocol_height = 2.2
    
    # Outer box for protocol
    rect_proto = patches.FancyBboxPatch(
        (center_x - box_width/2 - 0.2, y_current - protocol_height/2), box_width + 0.4, protocol_height,
        boxstyle="round,pad=0.1,rounding_size=0.1",
        linewidth=1.5, edgecolor='#2C3E50', facecolor='#E8F5E9'
    )
    ax.add_patch(rect_proto)
    ax.text(center_x, y_current + protocol_height/2 - 0.3, "Experimental Protocol", ha='center', va='center', fontsize=12, fontweight='bold', color='#2C3E50')
    
    # Inner boxes
    draw_box(ax, center_x - 1.6, y_current - 0.2, 2.8, 1.2, "Resting-State EEG\n• Eyes Closed\n• Eyes Open", bg_color='#FFFFFF', text_size=10)
    draw_box(ax, center_x + 1.6, y_current - 0.2, 2.8, 1.2, "Emotional Stimulus Task\n• Positive Images\n• Negative Images\n• Neutral Images", bg_color='#FFFFFF', text_size=10)

    # 5. EEG Preprocessing
    draw_arrow(ax, center_x, y_current - protocol_height/2, y_current + y_step - protocol_height/2 + box_height/2)
    y_current += y_step - 0.2
    preproc_height = 1.6
    
    # Outer box for preprocessing
    rect_preproc = patches.FancyBboxPatch(
        (center_x - box_width/2 - 0.2, y_current - preproc_height/2), box_width + 0.4, preproc_height,
        boxstyle="round,pad=0.1,rounding_size=0.1",
        linewidth=1.5, edgecolor='#2C3E50', facecolor='#FFF3E0'
    )
    ax.add_patch(rect_preproc)
    ax.text(center_x, y_current + preproc_height/2 - 0.3, "EEG Preprocessing", ha='center', va='center', fontsize=12, fontweight='bold', color='#2C3E50')
    
    # Inner flow
    draw_box(ax, center_x - 2, y_current - 0.2, 1.6, 0.6, "Filtering", bg_color='#FFE0B2', text_size=10)
    ax.annotate('', xy=(center_x - 1.1, y_current - 0.2), xytext=(center_x - 1.2, y_current - 0.2), arrowprops=dict(arrowstyle="->", color='#2C3E50', lw=1.5))
    draw_box(ax, center_x, y_current - 0.2, 1.8, 0.6, "Artifact Removal", bg_color='#FFE0B2', text_size=10)
    ax.annotate('', xy=(center_x + 1, y_current - 0.2), xytext=(center_x + 0.9, y_current - 0.2), arrowprops=dict(arrowstyle="->", color='#2C3E50', lw=1.5))
    draw_box(ax, center_x + 2, y_current - 0.2, 1.6, 0.6, "Segmentation", bg_color='#FFE0B2', text_size=10)

    # 6. Feature Extraction
    draw_arrow(ax, center_x, y_current - preproc_height/2, y_current + y_step - preproc_height/2 + box_height/2 + 0.4)
    y_current += y_step - 0.4
    draw_box(ax, center_x, y_current, box_width, box_height, "Feature Extraction\n(Time, Frequency, Non-Linear Features)", bg_color='#E8F5E9')

    # 7. Statistical Analysis
    draw_arrow(ax, center_x, y_current - box_height/2, y_current + y_step + box_height/2)
    y_current += y_step
    stat_height = 1.6
    
    # Outer box for statistical analysis
    rect_stat = patches.FancyBboxPatch(
        (center_x - box_width/2 - 0.2, y_current - stat_height/2), box_width + 0.4, stat_height,
        boxstyle="round,pad=0.1,rounding_size=0.1",
        linewidth=1.5, edgecolor='#2C3E50', facecolor='#E5F0FA'
    )
    ax.add_patch(rect_stat)
    ax.text(center_x, y_current + stat_height/2 - 0.3, "Statistical Analysis", ha='center', va='center', fontsize=12, fontweight='bold', color='#2C3E50')
    
    # Inner flow
    draw_box(ax, center_x - 1.5, y_current - 0.2, 2.5, 0.6, "Correlation Analysis\n(Spearman)", bg_color='#FFFFFF', text_size=10)
    ax.annotate('', xy=(center_x + 0.1, y_current - 0.2), xytext=(center_x - 0.25, y_current - 0.2), arrowprops=dict(arrowstyle="->", color='#2C3E50', lw=1.5))
    draw_box(ax, center_x + 1.5, y_current - 0.2, 2.5, 0.6, "Group Comparison\n(Mann-Whitney U)", bg_color='#FFFFFF', text_size=10)

    # 8. Biomarker Identification
    draw_arrow(ax, center_x, y_current - stat_height/2, y_current + y_step + box_height/2)
    y_current += y_step
    draw_box(ax, center_x, y_current, box_width, box_height, "Depression Biomarker Identification\n(e.g., LPP, Alpha Power)", bg_color='#FFB74D', fontweight='bold')

    plt.xlim(0, 10)
    plt.ylim(y_current - 1, y_start + 2)
    
    out_path = 'Research_Workflow_Diagram.png'
    plt.savefig(out_path, dpi=300, bbox_inches='tight')
    print(f"Workflow diagram successfully saved to {os.path.abspath(out_path)}")
    plt.close()

if __name__ == '__main__':
    create_workflow()
