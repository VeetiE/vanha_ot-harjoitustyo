class Snake:
    def __init__(self):
        self.lenght=1
        self.pos=[((SCREEN_W/2), (SCREEN_H/2))]
        self.beginning_pos=[((SCREEN_W/2), (SCREEN_H/2))]
        self.dir=random.choice([UP,DOWN,LEFT,RIGHT])
        self.color=(17,24,47)
        self.score=0
    def find_head(self):
        return self.pos[0]
    
    def move(self):
        current=self.pos[0]
        x,y=self.dir
        new = (((current[0]+(x*snake_block_size))%SCREEN_W), (current[1]+(y*snake_block_size))%SCREEN_H)
        self.pos.insert(0,new)
        if len(self.pos)>self.lenght:
            self.pos.pop()

    def new_game(self):
        self.score=0
        self.lenght=1
        self.pos=self.beginning_pos

    def turn(self, point):
        if self.lenght>1 and (point[0]*-1,point[1]*-1)==self.dir:
            return
        else:
            self.dir=point

    def draw(self, surface):
        for i in self.pos:
            r=pygame.Rect((i[0],i[1]), (snake_block_size,snake_block_size))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93,216,228), r,1)
