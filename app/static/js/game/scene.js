function gameDefault(url, map = 'level.json') {


  let Q = window.Q = Quintus({
    development: true,
    imagePath: `${url}/images/`,
    dataPath: `${url}/data/`
  })
    .include("Sprites, Scenes, Input, 2D, Anim")
    .setup('marioSmart')
    .controls(true);

  // Add in the default keyboard controls
  // along with joypad controls for touch
  Q.input.keyboardControls();
  Q.input.joypadControls();

  Q.gravityX = 0;
  Q.gravityY = 0;

  let SPRITE_PLAYER = 1;
  let SPRITE_TILES = 2;
  let SPRITE_ENEMY = 4;
  let SPRITE_DOT = 8;

  Q.component("marioControls", {
    defaults: {
      speed: 100,
      collisions: []
    },

    added: function () {
      var p = this.entity.p;

      Q._defaults(p, this.defaults);

      this.entity.on("step", this, "step");
      p.direction = 'right';
    },

    step: function (dt) {
      var p = this.entity.p;

      if (p.ignoreControls === undefined || !p.ignoreControls) {
        var collision = null;

        // Follow along the current slope, if possible.
        if (p.collisions !== undefined && p.collisions.length > 0 && (Q.inputs['left'] || Q.inputs['right'] || Q.inputs['down'] || Q.inputs['up'])) {
          if (p.collisions.length === 1) {
            collision = p.collisions[0];
          } else {
            // If there's more than one possible slope, follow slope with negative Y normal
            collision = null;

            for (var i = 0; i < p.collisions.length; i++) {
              if (p.collisions[i].normalY < 0) {
                collision = p.collisions[i];
              }
            }
          }

          // // Don't climb up walls.
          // if (collision !== null && collision.normalY > -0.3 && collision.normalY < 0.3) {
          //   collision = null;
          // }
        }

        if (Q.inputs['left']) {
          p.direction = 'left';
          if (collision && p.landed > 0) {
            p.vx = p.speed * collision.normalY;
            p.vy = -p.speed * collision.normalX;
          } else {
            p.vx = -p.speed;
          }
        } else if (Q.inputs['right']) {
          p.direction = 'right';
          if (collision && p.landed > 0) {
            p.vx = -p.speed * collision.normalY;
            p.vy = p.speed * collision.normalX;
          } else {
            p.vx = p.speed;
          }
        }
        else {
          p.vx = 0;
          if (collision && p.landed > 0) {
            p.vy = 0;
          }
        }

        if (Q.inputs['down']) {
          p.direction = 'down';
          if (collision && p.landed > 0) {
            p.vx = -p.speed * collision.normalY;
            p.vy = p.speed * collision.normalX;
          } else {
            p.vy = p.speed;
          }
        } else if (Q.inputs['up']) {
          p.direction = 'up';
          if (collision && p.landed > 0) {
            p.vx = p.speed * collision.normalY;
            p.vy = -p.speed * collision.normalX;
          } else {
            p.vy = -p.speed;
          }
        }
        else {
          p.vy = 0;
          if (collision && p.landed > 0) {
            p.vx = 0;
          }
        }
      }
    }
  });


  Q.Sprite.extend("Player", {
    init: function (p) {
      this._super(p, {
        sheet: "player",
        sprite: "player",
        type: SPRITE_PLAYER,
        collisionMask: SPRITE_TILES | SPRITE_ENEMY,
        strength: 100,
        direction: "right",
      });
      this.add("2d, marioControls, animation");
    },
    step: function (dt) {
      if (this.p.vx > 0) {
        this.play("walk_right");
      } else if (this.p.vx < 0) {
        this.play("walk_left");
      }
    }
  });

  Q.Sprite.extend("Flower", {
    init: function (p) {
      this._super(Q._defaults(p, {
        sheet: 'flower',
        sprite: "flower",
        type: SPRITE_DOT,
        sensor: true
      }));
      this.on("sensor");
      this.add("2d, animation");
      this.play('fire');
    },
    sensor: function () {
      this.destroy();
    },
  });

  Q.Sprite.extend("Princess", {
    init: function (p) {
      this._super(Q._defaults(p, {
        sheet: 'princess',
        type: SPRITE_DOT,
        // sensor: true
      }));
      // this.on("sensor");
      this.add("2d");
    },
    // sensor: function () {
    //   this.destroy();
    // },
  });

  Q.Sprite.extend("Enemy", {
    init: function (p) {
      this._super(p, {
        sheet: "enemy",
        sprite: "enemy",
        type: SPRITE_ENEMY,
        collisionMask: SPRITE_PLAYER | SPRITE_TILES
      });
      this.add("2d, animation");
      this.play('walk');
    },
  });

  // Return a x and y location from a row and column
  // in our tile map
  Q.tilePos = (col, row) => {
    return { x: col * 32 + 16, y: row * 32 + 16 };
  }

  Q.TileLayer.extend("marioMap", {
    init: function () {
      this._super({
        type: SPRITE_TILES,
        dataAsset: map,
        sheet: 'tiles',
      });
    },
    setup: function () {
      // Clone the top level arriw
      var tiles = this.p.tiles = this.p.tiles.concat();
      var size = this.p.tileW;
      for (var y = 0; y < tiles.length; y++) {
        var row = tiles[y] = tiles[y].concat();
        for (var x = 0; x < row.length; x++) {
          var tile = row[x];

          if (tile == 2) {
            this.stage.insert(new Q['Player'](Q.tilePos(x, y)));
            row[x] = 0;
          }
          if (tile == 3) {
            this.stage.insert(new Q['Flower'](Q.tilePos(x, y)));
            row[x] = 0;
          }
          if (tile == 4) {
            this.stage.insert(new Q['Enemy'](Q.tilePos(x, y)));
            row[x] = 0;
          }
          if (tile == 5) {
            this.stage.insert(new Q['Princess'](Q.tilePos(x, y)));
            row[x] = 0;
          }
        }
      }
    }

  });

  Q.scene("level1", function (stage) {
    var level = stage.collisionLayer(new Q.marioMap());
    level.setup();
  });

  Q.load(`sprites.png, sprites.json, ${map}, tiles.png`, function () {
    Q.sheet("tiles", "tiles.png", { tileW: 32, tileH: 32 });

    Q.compileSheets("sprites.png", "sprites.json");

    Q.animations("player", {
      walk_right: { frames: [0, 1, 2], rate: 1 / 6, flip: false, loop: true },
      walk_left: { frames: [0, 1, 2], rate: 1 / 6, flip: "x", loop: true },
    });

    Q.animations("enemy", {
      walk: { frames: [0, 1], rate: 1 / 3, loop: true },
    });

    Q.animations("flower", {
      fire: { frames: [0, 1, 2], rate: 1 / 3, loop: true },
    });

    Q.stageScene("level1");
  });
}
