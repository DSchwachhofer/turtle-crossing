from block import Block


class Blocks:
    def __init__(self):
        self.block_list = []
        self.create_blocks()

    def create_blocks(self):
        for _ in range(20):
            self.block_list.append(Block())

    def move(self, level):
        for block in self.block_list:
            block.move(level)

    def reset(self):
        for block in self.block_list:
            block.init_block()
        self.block_list.append(Block())

    def check_collision(self, figure_ycor):
        is_collision = False
        for block in self.block_list:
            if -20 < block.ycor() - figure_ycor < 27:
                if -30 < block.xcor() < 30:
                    is_collision = True
        return is_collision
