from flask import Flask, render_template, request, url_for
import matplotlib.pyplot as plt
import imageio.v2 as imageio
import os
import time

app = Flask(__name__)

ANIM_PATH = "static/animation.gif"

# Function to draw the rods
def draw_tower(rods, move_count, n):
    plt.figure(figsize=(8, 5))
    plt.title(f"Tower of Hanoi - Move {move_count}")
    colors = ['red', 'green', 'blue', 'orange', 'purple', 'brown', 'gray']
    
    max_width = n + 1
    for i, rod_name in enumerate(rods.keys()):
        rod = rods[rod_name]
        x_center = i * (max_width + 3)
        
        for j, disk in enumerate(rod):
            disk_width = disk * 2
            plt.barh(y=j, width=disk_width, height=0.8, 
                     left=x_center - disk_width / 2,
                     color=colors[disk % len(colors)], edgecolor='black')
        plt.text(x_center, -1, rod_name, fontsize=14, ha='center')
    
    plt.xlim(-3, 3 * max_width)
    plt.ylim(-1, n + 2)
    plt.axis('off')

    filename = f"frame_{move_count}.png"
    plt.savefig(filename)
    plt.close()
    time.sleep(0.2)
    return filename


# Recursive Hanoi logic (also records frames)
def tower_of_hanoi(n, source, auxiliary, target, rods, move_count, frames):
    if n == 1:
        disk = rods[source].pop()
        rods[target].append(disk)
        move_count[0] += 1
        frame = draw_tower(rods, move_count[0], len(rods['A']) + len(rods['B']) + len(rods['C']))
        frames.append(frame)
        return
    
    tower_of_hanoi(n - 1, source, target, auxiliary, rods, move_count, frames)
    disk = rods[source].pop()
    rods[target].append(disk)
    move_count[0] += 1
    frame = draw_tower(rods, move_count[0], len(rods['A']) + len(rods['B']) + len(rods['C']))
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

            # Build animation
            images = [imageio.imread(frame) for frame in frames]
            imageio.mimsave(ANIM_PATH, images, duration=1.5)

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
