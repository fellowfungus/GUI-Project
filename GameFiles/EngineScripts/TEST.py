# This game is being rewritten in Pygame. For install in PyCharm (I, TechNGamer, recommend) is to go to File -> Settings
#  -> Project: GUI Project -> Project Interpreter. Double click anywhere in the list box to open the package manager.
#  Search for pygame, and install the latest version. For my project team mates, follow this tutorial:
# https://www.youtube.com/watch?v=K5F-aGDIYaM&index=1&list=PL6gx4Cwl9DGAjkwJocj7vlc_mFU-4wXJq

from GameFiles.EngineScripts.ContinueMover import *
from GameFiles.EngineScripts.Frogger import *
from GameFiles.EngineScripts.River import *


class Test:
    WHITE = (255, 255, 255)

    def __init__(self):

        status = pygame.init()

        if status[1] > 0:
            print("Unsuccessful launch.")
            exit(-1)
        else:
            print("Successful.")

        self.game_display = pygame.display.set_mode((800, 600))

        pygame.display.set_caption("Frogger")

        pygame.display.update()

        self.exit_game = False

        self.objects = [ContinueMover(self.game_display, 1, 50), River(self.game_display)]
        self.objects.append(Frogger(self.game_display, self))
        #self.river =


        self.event_list = []


    def run(self):
        while not self.exit_game:

            self.game_display.fill(self.WHITE)

            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    self.exit_game = True
                else:
                    self.event_list.append(event)

            for game_object in self.objects:
                game_object.update()
            #self.river.render()
            pygame.display.update()

            Time.update()

        pygame.quit()


if __name__ == '__main__':
    main_class = Test()

    main_class.run()

    quit(0)
