def on_a_pressed():
    if mySprite.is_hitting_tile(CollisionDirection.BOTTOM):
        mySprite.vy = -200
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    game.over(False)
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, on_on_overlap)

projectile: Sprite = None
mySprite: Sprite = None
tiles.set_tilemap(tilemap("""
    level1
    """))
mySprite = sprites.create(img("""
        . . . . . . 5 . 5 . . . . . . .
        . . . . . f 5 5 5 f f . . . . .
        . . . . f 1 5 2 5 1 6 f . . . .
        . . . f 1 6 6 6 6 6 1 6 f . . .
        . . . f 6 6 f f f f 6 1 f . . .
        . . . f 6 f f d d f f 6 f . . .
        . . f 6 f d f d d f d f 6 f . .
        . . f 6 f d 3 d d 3 d f 6 f . .
        . . f 6 6 f d d d d f 6 6 f . .
        . f 6 6 f 3 f f f f 3 f 6 6 f .
        . . f f d 3 5 3 3 5 3 d f f . .
        . . f d d f 3 5 5 3 f d d f . .
        . . . f f 3 3 3 3 3 3 f f . . .
        . . . f 3 3 5 3 3 5 3 3 f . . .
        . . . f f f f f f f f f f . . .
        . . . . . f f . . f f . . . . .
        """),
    SpriteKind.player)
tiles.place_on_tile(mySprite, tiles.get_tile_location(1, 5))
mySprite.ay = 500

def on_update_interval():
    global projectile
    projectile = sprites.create_projectile_from_side(img("""
            1 1 e e e e e e e e e e e e 1 1
            1 1 e e e e e e e e e e e e 1 1
            e e e e e e e e e e e e e e e e
            e e e e e e e e e e e e e e e e
            e e e e e e e e e e e e e e e e
            e e e e e e e e e e e e e e e e
            e e e e e e e e e e e e e e e e
            e e e e e e e e e e e e e e e e
            e e e e e e e e e e e e e e e e
            e e e e e e e e e e e e e e e e
            e e e e e e e e e e e e e e e e
            e e e e e e e e e e e e e e e e
            e e e e e e e e e e e e e e e e
            e e e e e e e e e e e e e e e e
            1 1 e e e e e e e e e e e e 1 1
            1 1 e e e e e e e e e e e e 1 1
            """),
        randint(-100, -80),
        0)
    tiles.place_on_tile(projectile, tiles.get_tile_location(9, 5))
    info.change_score_by(1)
game.on_update_interval(2000, on_update_interval)
