from block import Block


class Blocks:
    def __init__(self):
        self.block_list = []
        self.unused_blocks = []

    def init_blocks(self):
        self.block_list = []
        self.create_blocks()

    def create_one_block(self):
        if len(self.unused_blocks) > 0:
            reused_block = self.unused_blocks[0]
            reused_block.init_block()
            self.unused_blocks.pop(0)
            self.block_list.append(reused_block)
        else:
            self.block_list.append(Block())

    def create_blocks(self):
        for _ in range(20):
            self.create_one_block()

    def clear_blocks(self):
        if len(self.block_list) > 0:
            for block in self.block_list:
                block.hideturtle()
                self.unused_blocks.append(block)
            self.block_list = []

    def move(self, level):
        for block in self.block_list:
            block.move(level)

    def reset(self):
        for block in self.block_list:
            block.init_block()
        self.create_one_block()

    def check_collision(self, figure_ycor):
        is_collision = False
        for block in self.block_list:
            if -20 < block.ycor() - figure_ycor < 27:
                if -30 < block.xcor() < 30:
                    is_collision = True
        return is_collision
