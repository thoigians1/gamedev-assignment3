import pygame
from tiles import Tile
from settings import tileSize, screenWidth
from player import Player
class Level:
  def __init__(self,levelData,surface):
    # Level setup
    self.displaySurface = surface
    self.setupLevel(levelData)
    self.worldShift = 0

  def setupLevel(self,layout):
    self.tiles = pygame.sprite.Group()
    self.player = pygame.sprite.GroupSingle()
    for rowIndex,row in enumerate(layout):
      for colIndex,cell in enumerate(row):
        x = colIndex * tileSize
        y = rowIndex * tileSize
        if cell == 'X':
          tile = Tile((x,y),tileSize)
          self.tiles.add(tile)
        if cell == 'P':
          playerSprite = Player((x,y))
          self.player.add(playerSprite)

  def scrollX(self):
    player = self.player.sprite
    playerX = player.rect.centerx
    directionX = player.direction.x

    if playerX < screenWidth / 4 and directionX < 0:
      self.worldShift = 8
      player.speed = 0
    elif playerX > screenWidth - (screenWidth/4) and directionX > 0:
      self.worldShift = -8
      player.speed = 0
    else :
      self.worldShift = 0
      player.speed = 8
  
  def horizontalMovementCollision(self):
    player = self.player.sprite
    player.rect.x += player.direction.x * player.speed
    # Collision
    for sprite in self.tiles.sprites():
      if sprite.rect.colliderect(player.rect):
        if player.direction.x < 0:
          player.rect.left = sprite.rect.right
        elif player.direction.x > 0:
          player.rect.right = sprite.rect.left 
  
  def verticalMovementCollision(self):
    if sprite.rect.colliderect(player.rect):
        if player.direction.y < 0:
          player.rect.left = sprite.rect.right
        elif player.direction.x > 0:
          player.rect.right = sprite.rect.left 

  def run(self):
    # Level tiles
    self.tiles.update(self.worldShift)
    self.tiles.draw(self.displaySurface)
    self.scrollX()
    # Player
    self.player.update()
    self.horizontalMovementCollision()
    self.player.draw(self.displaySurface)
