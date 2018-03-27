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
      collisions: [],
      posX: 0,
      posY: 0,
      oX: 0,
      oY: 0,
      moves: [
        // ['down', 1],
        // ['right', 1],
        // ['down', 1],
        // ['right', 2]
        // ['down', 2],
        // ['up', 2],
        // ['right', 8],
        // ['up', 3]

      ],
      // move: ['down', 'right', 'down'],
    },

    added: function () {
      var p = this.entity.p;

      p.posX = this.entity.p.x;
      p.posY = this.entity.p.y;

      p.oX = this.entity.p.x;
      p.oY = this.entity.p.y;

      p.direction = null;

      Q._defaults(p, this.defaults);

      this.entity.on("step", this, "step");
    },

    step: function (dt) {
      var p = this.entity.p;
      console.log(p.moves)
      console.log(p.move);

      // if (p.ignoreControls === undefined || !p.ignoreControls) {
      //   var collision = null;

        // Follow along the current slope, if possible.
        // if (p.collisions !== undefined && p.collisions.length > 0 && (Q.inputs['left'] || Q.inputs['right'] || Q.inputs['down'] || Q.inputs['up']) && (p.move[0] == 'down' || p.move[0] == 'up' || p.move[0] == 'left' || p.move[0] == 'right')) {
        //   if (p.collisions.length === 1) {
        //     collision = p.collisions[0];
        //   } else {
        //     collision = null;
        //     for (var i = 0; i < p.collisions.length; i++) {
        //       if (p.collisions[i].normalY < 0) {
        //         collision = p.collisions[i];
        //       }
        //     }
        //   }
        // }

        if (p.moves.length > 0) {
          if (p.moves[0][0] == 'left') {
            p.posX = p.oX - (32 * p.moves[0][1]);
          }
          if (p.moves[0][0] == 'right') {
            p.posX = p.oX + (32 * p.moves[0][1]);
          }
          if (p.moves[0][0] == 'down') {
            p.posY = p.oY + (32 * p.moves[0][1]);
          }
          if (p.moves[0][0] == 'up') {
            p.posY = p.oY - (32 * p.moves[0][1]);
          }
        }

        switch (p.move[0]) {
          case "left":
            p.vx = -p.speed;
            p.vy = 0;
            break;
          case "right":
            p.vx = p.speed;
            p.vy = 0;
            break;
          case "up":
            p.vy = -p.speed;
            p.vx = 0;
            break;
          case "down":
            p.vy = p.speed;
            p.vx = 0;
            break;
          default:
            p.vx = 0;
            p.vy = 0;
        }
        // right
        if (p.posX < p.x) {
          if (p.move[0] == 'right') {
            p.oX = p.posX;
            p.move.shift();
            p.moves.shift();
          }
        }
        // left
        if (p.posX > p.x) {
          if (p.move[0] == 'left') {
            p.oX = p.posX
            p.move.shift();
            p.moves.shift();
          }
        }
        // down
        if (p.posY < p.y) {
          if (p.move[0] == 'down') {
            p.oY = p.posY;
            p.move.shift();
            p.moves.shift();
          }
        }
        // up
        if (p.posY > p.y) {
          if (p.move[0] == 'up') {
            p.oY = p.posY;
            p.move.shift();
            p.moves.shift();
          }
        }
        // En caso de colisiones
        // if (p.collisions.length > 0) {
        //   console.log('entro');
        //   // p.move.shift();
        //   // p.moves.shift();
        // }
      // }
    }
  });


  Q.Sprite.extend("Player", {
    init: function (p) {
      this._super(p, {
        sheet: "player",
        sprite: "player",
        "w": 32,
        "h": 32,
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
    return {
      x: col * 32 + 16,
      y: row * 32 + 16
    };
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
    Q.sheet("tiles", "tiles.png", {
      tileW: 32,
      tileH: 32
    });

    Q.compileSheets("sprites.png", "sprites.json");

    Q.animations("player", {
      walk_right: {
        frames: [0, 1, 2],
        rate: 1 / 6,
        flip: false,
        loop: true
      },
      walk_left: {
        frames: [0, 1, 2],
        rate: 1 / 6,
        flip: "x",
        loop: true
      },
    });

    Q.animations("enemy", {
      walk: {
        frames: [0, 1],
        rate: 1 / 3,
        loop: true
      },
    });

    Q.animations("flower", {
      fire: {
        frames: [0, 1, 2],
        rate: 1 / 3,
        loop: true
      },
    });

    Q.stageScene("level1");
  });
}
