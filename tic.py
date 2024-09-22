import pygame
import sys
import json
from datetime import datetime

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 300, 350  # Increased height for scoreboard
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
SQUARE_SIZE = WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Colors
BG_COLOR = (28, 170, 156)
LINE_COLOR = (23, 145, 135)
CIRCLE_COLOR = (239, 231, 200)
CROSS_COLOR = (66, 66, 66)
SCOREBOARD_COLOR = (20, 130, 120)
TEXT_COLOR = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Tic Tac Toe')
screen.fill(BG_COLOR)

# Font for scoreboard
font = pygame.font.Font(None, 36)

# Load scores from file
try:
    with open('scores.json', 'r') as f:
        scores = json.load(f)
except FileNotFoundError:
    scores = {'X': 0, 'O': 0, 'Ties': 0}

# Load match history from file
try:
    with open('match_history.json', 'r') as f:
        match_history = json.load(f)
except FileNotFoundError:
    match_history = []

# New constants for the pop-up
POPUP_WIDTH, POPUP_HEIGHT = 200, 100
POPUP_COLOR = (200, 200, 200)
BUTTON_COLOR = (100, 100, 100)
BUTTON_HOVER_COLOR = (150, 150, 150)

# Draw the game board
def draw_lines():
    # Horizontal lines
    pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE), (WIDTH, SQUARE_SIZE), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (0, 2 * SQUARE_SIZE), (WIDTH, 2 * SQUARE_SIZE), LINE_WIDTH)
    # Vertical lines
    pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE, 0), (SQUARE_SIZE, HEIGHT), LINE_WIDTH)
    pygame.draw.line(screen, LINE_COLOR, (2 * SQUARE_SIZE, 0), (2 * SQUARE_SIZE, HEIGHT), LINE_WIDTH)

# Draw X or O
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'O':
                pygame.draw.circle(screen, CIRCLE_COLOR, (int(col * SQUARE_SIZE + SQUARE_SIZE // 2), int(row * SQUARE_SIZE + SQUARE_SIZE // 2)), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == 'X':
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, CROSS_COLOR, (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE), (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)

def draw_scoreboard():
    pygame.draw.rect(screen, SCOREBOARD_COLOR, (0, 300, WIDTH, 50))
    x_score = font.render(f"X: {scores['X']}", True, TEXT_COLOR)
    o_score = font.render(f"O: {scores['O']}", True, TEXT_COLOR)
    ties = font.render(f"Ties: {scores['Ties']}", True, TEXT_COLOR)
    screen.blit(x_score, (20, 310))
    screen.blit(o_score, (120, 310))
    screen.blit(ties, (220, 310))

def save_scores():
    with open('scores.json', 'w') as f:
        json.dump(scores, f)

def save_match_history(event):
    global match_history
    match = {
        'date': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        'event': event,
        'board': [item for sublist in board for item in sublist],
        'scores': scores.copy()
    }
    match_history.append(match)
    with open('match_history.json', 'w') as f:
        json.dump(match_history, f)

def check_winner(board, player):
    # Check rows, columns, and diagonals
    for i in range(3):
        if all(board[i][j] == player for j in range(3)) or \
           all(board[j][i] == player for j in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or \
       all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def draw_popup(message):
    popup_rect = pygame.Rect((WIDTH - POPUP_WIDTH) // 2, (HEIGHT - POPUP_HEIGHT) // 2, POPUP_WIDTH, POPUP_HEIGHT)
    pygame.draw.rect(screen, POPUP_COLOR, popup_rect)
    
    font = pygame.font.Font(None, 30)
    text = font.render(message, True, (0, 0, 0))
    text_rect = text.get_rect(center=(WIDTH // 2, (HEIGHT - POPUP_HEIGHT) // 2 + 20))
    screen.blit(text, text_rect)
    
    play_again_button = pygame.Rect((WIDTH - 150) // 2, (HEIGHT + POPUP_HEIGHT) // 2 - 60, 150, 30)
    exit_button = pygame.Rect((WIDTH - 150) // 2, (HEIGHT + POPUP_HEIGHT) // 2 - 20, 150, 30)
    
    pygame.draw.rect(screen, BUTTON_COLOR, play_again_button)
    pygame.draw.rect(screen, BUTTON_COLOR, exit_button)
    
    play_text = font.render("Play Again", True, (255, 255, 255))
    exit_text = font.render("Exit", True, (255, 255, 255))
    
    screen.blit(play_text, play_text.get_rect(center=play_again_button.center))
    screen.blit(exit_text, exit_text.get_rect(center=exit_button.center))
    
    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_match_history('Game End')
                reset_game()
                return False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_button.collidepoint(event.pos):
                    save_match_history('Game End')
                    reset_game()
                    return True
                elif exit_button.collidepoint(event.pos):
                    save_match_history('Game End')
                    reset_game()
                    return False
        
        # Hover effect
        mouse_pos = pygame.mouse.get_pos()
        if play_again_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, play_again_button)
            screen.blit(play_text, play_text.get_rect(center=play_again_button.center))
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, play_again_button)
            screen.blit(play_text, play_text.get_rect(center=play_again_button.center))
        
        if exit_button.collidepoint(mouse_pos):
            pygame.draw.rect(screen, BUTTON_HOVER_COLOR, exit_button)
            screen.blit(exit_text, exit_text.get_rect(center=exit_button.center))
        else:
            pygame.draw.rect(screen, BUTTON_COLOR, exit_button)
            screen.blit(exit_text, exit_text.get_rect(center=exit_button.center))
        
        pygame.display.update()

def reset_game():
    global board, current_player, scores
    board = [[" " for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    current_player = 'X'
    scores = {'X': 0, 'O': 0, 'Ties': 0}
    screen.fill(BG_COLOR)
    draw_lines()
    draw_scoreboard()
    pygame.display.update()
    save_match_history('Game Start')

# Main game loop
reset_game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            save_match_history('Game Incomplete')
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouseX = event.pos[0]
            mouseY = event.pos[1]
            
            if mouseY < 300:  # Ensure click is within the game board
                clicked_row = int(mouseY // SQUARE_SIZE)
                clicked_col = int(mouseX // SQUARE_SIZE)
                
                if board[clicked_row][clicked_col] == " ":
                    board[clicked_row][clicked_col] = current_player
                    if check_winner(board, current_player):
                        print(f"Player {current_player} wins!")
                        scores[current_player] += 1
                        if not draw_popup(f"Player {current_player} wins!"):
                            pygame.quit()
                            sys.exit()
                    elif all(board[i][j] != " " for i in range(BOARD_ROWS) for j in range(BOARD_COLS)):
                        print("It's a tie!")
                        scores['Ties'] += 1
                        if not draw_popup("It's a tie!"):
                            pygame.quit()
                            sys.exit()
                    else:
                        current_player = 'O' if current_player == 'X' else 'X'
    
    draw_figures()
    draw_scoreboard()
    pygame.display.update()
