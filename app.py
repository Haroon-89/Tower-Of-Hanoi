import matplotlib
matplotlib.use('Agg')  # Set non-interactive backend to avoid Tkinter issues
from flask import Flask, render_template, request, url_for
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os
import time

app = Flask(__name__)

ANIM_PATH = "static/animation.gif"

# Function to draw the rods
def draw_tower(rods, move_count, n):
    scale = 3  # Increased scale for better visibility of small disks
    bar_height = 1.0  # Slightly taller bars for clearer separation
    half_max = (n * scale) / 2
    spacing = n * scale + 6  # Adjusted spacing for gap with larger scale
    num_pegs = len(rods)
    plt.figure(figsize=(14, 7))  # Larger figure for better absolute sizing
    plt.title(f"Tower of Hanoi - Move {move_count}")
    colors = ['red', 'green', 'blue', 'orange', 'purple', 'brown', 'gray']
    
    for i, rod_name in enumerate(rods.keys()):
        rod = rods[rod_name]
        x_center = i * spacing
        
        for j, disk in enumerate(rod):
            disk_width = disk * scale
            plt.barh(y=j, width=disk_width, height=bar_height, 
                     left=x_center - disk_width / 2,
                     color=colors[disk % len(colors)], edgecolor='black')
        plt.text(x_center, -1, rod_name, fontsize=14, ha='center')
    
    min_x = -half_max - 2
    max_x = (num_pegs - 1) * spacing + half_max + 2
    plt.xlim(min_x, max_x)
    plt.ylim(-2, n + 3)  # Extra padding top and bottom
    plt.axis('off')
    plt.tight_layout()

    filename = f"frame_{move_count}.png"
    plt.savefig(filename, bbox_inches='tight', dpi=100)
    plt.close()
    return filename


# Recursive Hanoi logic (also records frames)
def tower_of_hanoi(n, source, auxiliary, target, rods, move_count, frames):
    if n == 1:
        disk = rods[source].pop()
        rods[target].append(disk)
        move_count[0] += 1
        frame = draw_tower(rods, move_count[0], n)
        frames.append(frame)
        return
    
    tower_of_hanoi(n - 1, source, target, auxiliary, rods, move_count, frames)
    disk = rods[source].pop()
    rods[target].append(disk)
    move_count[0] += 1
    frame = draw_tower(rods, move_count[0], n)
    frames.append(frame)
    tower_of_hanoi(n - 1, auxiliary, source, target, rods, move_count, frames)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            n = int(request.form['disks'])
            if n < 1 or n > 6:
                return render_template('index.html', error="Enter a number between 1 and 6.")

            rods = {'A': list(range(n, 0, -1)), 'B': [], 'C': []}
            move_count = [0]
            frames = []

            # Draw initial state
            frames.append(draw_tower(rods, move_count[0], n))

            # Run algorithm and record frames
            tower_of_hanoi(n, 'A', 'B', 'C', rods, move_count, frames)

            # Build animation with balanced speed (1 FPS = 1 second per frame)
            images = [imageio.imread(frame) for frame in frames]
            imageio.mimsave(ANIM_PATH, images, fps=1.0)  # 1 FPS for 1 second per frame—reasonable pace

            # Clean up temporary frames
            for frame in frames:
                os.remove(frame)

            return render_template('result.html', n=n, total_moves=move_count[0],
                                   gif_path=url_for('static', filename='animation.gif'))

        except ValueError:
            return render_template('index.html', error="Please enter a valid integer.")
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)