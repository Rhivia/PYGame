from SlimeFarm import Tamagushi

class main():
    def game(self):
        self.loop = True

        def switch(action):
            action.upper()
            return {
                'FOME': slime.getHunger(),
                'IDADE': slime.getAge(),
                'HP': slime.getHP(),
            }.get(action, "Não foi uma ação válida")

        while (self.loop):
            print("Bem-vindo ao Slime Farm!!")
            print("Crie seu primeiro slime, qual o nome dele?")
            name = input()

            slime = Tamagushi.new(name)

            print("Muito bem! O ", slime.getName(), " parece feliz.")
            print(slime.getName(), " parece com fome.")
            print("Digite o comando FOME para saber a fome dele.")
            action = input()

            switch(action)

            self.loop = False



