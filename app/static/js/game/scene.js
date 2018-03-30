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

  Q.component("manualControls", {
    defaults: {
      speed: 100,
    },
    added: function () {
      var p = this.entity.p;
      Q._defaults(p, this.defaults);
      this.entity.on("step", this, "step");
    },
    step: function (dt) {
      var p = this.entity.p;

      if (p.ignoreControls === undefined || !p.ignoreControls) {

        if (Q.inputs['left']) {
          p.direction = 'left';
          p.vx = -p.speed;
        } else if (Q.inputs['right']) {
          p.direction = 'right';
          p.vx = p.speed;
        }
        else {
          p.vx = 0;
        }
        if (Q.inputs['down']) {
          p.direction = 'down';
          p.vy = p.speed;
        } else if (Q.inputs['up']) {
          p.direction = 'up';
          p.vy = -p.speed;
        }
        else {
          p.vy = 0;
        }
      }
    }
  });

  Q.component("autoControls", {
    defaults: {
      speed: 100,
      start: true,
      posX: 0,
      posY: 0,
      oX: 0,
      oY: 0,
      move: ['down', 'down', 'right', 'down', 'right', 'right', 'down', 'right', 'right', 'up', 'up', 'up', 'left', 'left', 'up', 'up', 'right', 'up', 'right', 'right', 'right', 'down', 'right', 'right']
    },
    // Arreglar las condiciones no ejecuta el ultmo down
    added: function () {
      var p = this.entity.p;
      p.posX = this.entity.p.x;
      p.posY = this.entity.p.y;
      p.oX = this.entity.p.x;
      p.oY = this.entity.p.y;
      p.direction = 'right';
      Q._defaults(p, this.defaults);
      this.entity.on("step", this, "step");
    },

    step: function (dt) {
      var p = this.entity.p;
      if (p.ignoreControls === undefined || !p.ignoreControls) {
        if (p.move.length > 0) {
          if (p.move[0] == 'left') {
            p.posX = p.oX - 32;
            p.direction = 'left';
          }
          if (p.move[0] == 'right') {
            p.posX = p.oX + 32;
            p.direction = 'right';
          }
          if (p.move[0] == 'down') {
            p.posY = p.oY + 32;
            p.direction = 'down';
          }
          if (p.move[0] == 'up') {
            p.posY = p.oY - 32;
            p.direction = 'up';
          }
        }

        switch (p.move[0]) {
          case "up":
            p.vy = -p.speed;
            break;
          case "down":
            p.vy = p.speed;
            break;
          case "left":
            p.vx = -p.speed;
            break;
          case "right":
            p.vx = p.speed;
            break;
        }

        if (p.posY >= p.y) {
          if (p.direction == 'up') {
            console.log(1)
            p.oY = p.posY;
            p.y = p.posY;
            p.vy = 0;
            p.move.shift();
            p.direction = null
          }
        }
        if (p.posY <= p.y) {
          if (p.direction == 'down') {
            console.log(2)
            p.oY = p.posY;
            p.y = p.posY;
            p.vy = 0;
            p.move.shift();
            p.direction = null
          }
        }
        if (p.posX <= p.x) {
          if (p.direction  == 'right') {
            console.log(3)
            p.oX = p.posX;
            p.x = p.posX;
            p.vx = 0;
            p.move.shift();
            p.direction = null
          }
        }
        if (p.posX >= p.x){
          if (p.direction == 'left') {
            console.log(4)
            p.oX = p.posX;
            p.x = p.posX;
            p.vx = 0;
            p.move.shift();
            p.direction = null
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
      });
      this.add("2d, autoControls, animation");
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
      }));
      this.add("2d");
    },
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
      this.on("hit.sprite", this, "hit");
      this.play('walk');
    },
    hit: function (col) {
      if (col.obj.isA("Player")) {
        this.destroy();
      }
    }
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
