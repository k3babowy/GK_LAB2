import pygame
import math

pygame.init()

window_width = 600
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Przekształcenie wielokąta")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

def draw_hexagon():
    center = (window_width // 2, window_height // 2)
    radius = 150
    num_sides = 6
    angle_increment = (2 * math.pi) / num_sides

    points = []
    for i in range(num_sides):
        x = center[0] + int(radius * math.cos(i * angle_increment))
        y = center[1] + int(radius * math.sin(i * angle_increment))
        points.append((x, y))

    return points

def transform_hexagon(points, option):
    if option == 2:
        points = rotate_polygon(points, 45)
    elif option == 3:
        points = rotate_polygon(points, 180)
    elif option == 4:
        points = skew_polygon(points, 1.5)
    elif option == 5:
        points = align_top(points)
    elif option == 6:
        points = skew_polygon(points, 1.5)
        points = rotate_polygon(points, 180)
    elif option == 7:
        points = rotate_polygon(points, 180)
        points = mirror_polygon(points, "vertical")
    elif option == 8:
        points = rotate_polygon(points, 45)
        points = align_bottom(points)
        points = widen_polygon(points, 1.5)
    elif option == 9:
        points = rotate_polygon(points, 180)
        points = skew_polygon(points, 1.5)
        points = align_right(points)

    return points

def rotate_polygon(points, angle):
    center = (window_width // 2, window_height // 2)
    angle_radians = math.radians(angle)
    rotated_points = []
    for point in points:
        x = center[0] + math.cos(angle_radians) * (point[0] - center[0]) - math.sin(angle_radians) * (point[1] - center[1])
        y = center[1] + math.sin(angle_radians) * (point[0] - center[0]) + math.cos(angle_radians) * (point[1] - center[1])
        rotated_points.append((x, y))
    return rotated_points

def skew_polygon(points, factor):
    center = (window_width // 2, window_height // 2)
    skewed_points = []
    for point in points:
        x = point[0] + factor * (point[1] - center[1])
        y = point[1]
        skewed_points.append((x, y))
    return skewed_points

def mirror_polygon(points, axis):
    if axis == "vertical":
        center_x = sum(point[0] for point in points) / len(points)
        mirrored_points = [(2 * center_x - point[0], point[1]) for point in points]
    elif axis == "horizontal":
        center_y = sum(point[1] for point in points) / len(points)
        mirrored_points = [(point[0], 2 * center_y - point[1]) for point in points]
    return mirrored_points

def align_top(points):
    min_y = min(point[1] for point in points)
    shifted_points = [(point[0], point[1] - min_y) for point in points]
    return shifted_points

def align_bottom(points):
    max_y = max(point[1] for point in points)
    shifted_points = [(point[0], point[1] - max_y + window_height) for point in points]
    return shifted_points

def align_right(points):
    max_x = max(point[0] for point in points)
    shifted_points = [(point[0] - max_x + window_width, point[1]) for point in points]
    return shifted_points

def widen_polygon(points, factor):
    center_y = sum(point[1] for point in points) / len(points)
    widened_points = []
    for point in points:
        x = point[0]
        y = center_y + factor * (point[1] - center_y)
        widened_points.append((x, y))
    return widened_points

running = True
option = 1
points = draw_hexagon()
font = pygame.font.Font(None, 14)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                option = 1
            elif event.key == pygame.K_2:
                option = 2
            elif event.key == pygame.K_3:
                option = 3
            elif event.key == pygame.K_4:
                option = 4
            elif event.key == pygame.K_5:
                option = 5
            elif event.key == pygame.K_6:
                option = 6
            elif event.key == pygame.K_7:
                option = 7
            elif event.key == pygame.K_8:
                option = 8
            elif event.key == pygame.K_9:
                option = 9

    window.fill(WHITE)
    transformed_points = transform_hexagon(points, option)
    pygame.draw.polygon(window, BLACK, transformed_points)

    if option == 1:
        mode_text = "Wielokąt na środku okna"
    elif option == 2:
        mode_text = "Wielokąt przekręcony o 45 stopni"
    elif option == 3:
        mode_text = "Wielokąt odwrócony o 180 stopni"
    elif option == 4:
        mode_text = "Wielokąt pochylony w lewo"
    elif option == 5:
        mode_text = "Wielokąt przy górnej krawędzi okna"
    elif option == 6:
        mode_text = "Wielokąt odwrócony o 180 stopni i przekrzywiony w lewo"
    elif option == 7:
        mode_text = "Wielokąt odwrócony o 180 stopni i odwrócenie lustrzane"
    elif option == 8:
        mode_text = "Wielokąt odwrócony o 45 stopni oraz przy dolnej krawędzi"
    elif option == 9:
        mode_text = "Wielokąt odwrócony o 180 stopni pochylony w lewo oraz przy prawej krawędzi"

    mode_text = font.render("Tryb: " + str(mode_text), True, BLACK)
    window.blit(mode_text, (10, 580))

    pygame.display.update()

pygame.quit()