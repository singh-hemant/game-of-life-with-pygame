import pygame
import random
import sys
import math


########## game of life #################
class Person:
    def __init__(self):
        self.is_alive = False

    def check(self):
        return self.is_alive

    def live(self):
        self.is_alive = True

    def dead(self):
        self.is_alive = False


class Population:
    def __init__(self):
        self.population_size = 22500
        self.square_root = int(math.sqrt(self.population_size))
        self.population = []

        for i in range(self.square_root):
            rows = []
            for j in range(self.square_root):
                rows.append(Person())
            self.population.append(rows)

    def infect(self, no_of_infected_people=100):
        for _ in range(no_of_infected_people):
            i = random.randint(0, self.square_root-1)
            j = random.randint(0, self.square_root-1)
            self.population[i][j].live()

    def printing(self):
        for i in range(self.square_root):
            for j in range(self.square_root):
                if self.population[i][j].check():
                    print("O", end=" ")
                else:
                    print("X", end=' ')
            print()

    def update_gen(self):
        for i in range(self.square_root):
            for j in range(self.square_root):
                count = 0
                if i == 0:
                    if j == 0:
                        if self.population[i+1][j].check():
                            count += 1
                        if self.population[i][j+1].check():
                            count += 1
                        if self.population[i+1][j+1].check():
                            count += 1
                    elif j == self.square_root - 1:
                        if self.population[i][j-1].check():
                            count += 1
                        if self.population[i+1][j-1].check():
                            count += 1
                        if self.population[i+1][j].check():
                            count += 1
                    else:
                        if self.population[i-1][j].check():
                            count += 1
                        if self.population[i-1][j+1].check():
                            count += 1
                        if self.population[i][j+1].check():
                            count += 1
                        if self.population[i+1][j+1].check():
                            count += 1
                        if self.population[i+1][j].check():
                            count += 1
                if i == self.square_root-1:
                    if j == 0:
                        if self.population[i-1][j].check():
                            count += 1
                        if self.population[i-1][j+1].check():
                            count += 1
                        if self.population[i][j+1].check():
                            count += 1
                    elif j == self.square_root - 1:
                        if self.population[i][j-1].check():
                            count += 1
                        if self.population[i-1][j].check():
                            count += 1
                        if self.population[i-1][j-1].check():
                            count += 1
                    else:
                        if self.population[i-1][j].check():
                            count += 1
                        if self.population[i-1][j+1].check():
                            count += 1
                        if self.population[i][j+1].check():
                            count += 1
                        if self.population[i-1][j-1].check():
                            count += 1
                        if self.population[i][j-1].check():
                            count += 1
                else:
                    if j == 0:
                        if self.population[i-1][j].check():
                            count += 1
                        if self.population[i-1][j+1].check():
                            count += 1
                        if self.population[i+1][j].check():
                            count += 1
                        if self.population[i+1][j+1].check():
                            count += 1
                        if self.population[i+1][j].check():
                            count += 1
                    elif j == self.square_root - 1:
                        if self.population[i-1][j].check():
                            count += 1
                        if self.population[i-1][j-1].check():
                            count += 1
                        if self.population[i][j-1].check():
                            count += 1
                        if self.population[i+1][j-1].check():
                            count += 1
                        if self.population[i+1][j].check():
                            count += 1
                    else:
                        if self.population[i-1][j-1].check():
                            count += 1
                        if self.population[i-1][j].check():
                            count += 1
                        if self.population[i-1][j+1].check():
                            count += 1
                        if self.population[i][j+1].check():
                            count += 1
                        if self.population[i+1][j+1].check():
                            count += 1
                        if self.population[i+1][j].check():
                            count += 1
                        if self.population[i+1][j-1].check():
                            count += 1
                        if self.population[i][j-1].check():
                            count += 1

                if count < 2 or count > 3:
                    self.population[i][j].dead()
                elif count == 3:
                    self.population[i][j].live()



########### End of game life code ##################


class Game:
    def __init__(self):
        Width = 600
        Height = 600
        pygame.init()
        self.window = pygame.display.set_mode((Width, Height))
        pygame.display.set_caption("GameOfLife")
        self.population = Population()
        self.UI()

    def UI(self):
        square_range = self.population.square_root
        size = 600/square_range

        self.population.infect(2000)

        run = True
        generation = 1

        while run:
            Dead = 0
            Alive = 0
            print(str(generation))
            self.population.update_gen()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
            for i in range(square_range):
                for j in range(square_range):
                    if self.population.population[i][j].check():
                        Alive += 1
                        pygame.draw.rect(self.window, (0, 200, 0), (i * size + 1, j * size + 1, size - 1, size - 1))
                    else:
                        Dead += 1
                        pygame.draw.rect(self.window, (200, 0, 0), (i*size+1, j*size+1, size-1, size-1))
            pygame.display.flip()

            ###############
            print(f"---------Generation: {str(generation)}-------")
            print("Alive : ", str(Alive))
            print("Dead : ", str(Dead))
            print("----------------------------")
            generation += 1


if __name__ == "__main__":
    Game()
    pygame.quit()
    sys.exit()
