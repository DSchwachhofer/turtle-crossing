from block import Block


class Blocks:
    def __init__(self):
        self.block_list = []  # list for all active blocks
        self.unused_blocks = []  # list to hold blocks which are not needed, after game has been restarted

    def init_blocks(self):
        self.block_list = []
        self.create_blocks()

    # block management: create new block or use one from unused list if available
    def create_one_block(self):
        if len(self.unused_blocks) > 0:
            reused_block = self.unused_blocks[0]
            reused_block.init_block()
            self.unused_blocks.pop(0)
            self.block_list.append(reused_block)
        else:
            self.block_list.append(Block())

    # create 20 random blocks
    def create_blocks(self):
        for _ in range(20):
            self.create_one_block()

    # hide blocks for game over screen
    def clear_blocks(self):
        if len(self.block_list) > 0:
            for block in self.block_list:
                block.hideturtle()
                self.unused_blocks.append(block)
            self.block_list = []

    # get blocks moving
    def move(self, level):
        for block in self.block_list:
            block.move(level)

    # get new block positions if level up, create one additional block each time
    def reset(self):
        for block in self.block_list:
            block.init_block()
        self.create_one_block()

    def check_collision(self, figure_ycor):
        is_collision = False
        for block in self.block_list:
            if -20 < block.ycor() - figure_ycor < 27:  # check if figure is on block height
                if -30 < block.xcor() < 30:  # check if figure is in block
                    is_collision = True
        return is_collision
