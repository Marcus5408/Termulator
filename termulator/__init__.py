import pygame
import subprocess

class Termulator:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Termulator")

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    pygame.quit()
                

            self.run_command("cd repos")

    def run_command(self, command: str):
        # run the command and return the output
        process = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
        output, error = process.communicate()
        return output
    
    def print_to_screen(self, text:str) -> None:
        pass

if __name__ == "__main__":
    termulator = Termulator()
    termulator.run()
    # test run_command()