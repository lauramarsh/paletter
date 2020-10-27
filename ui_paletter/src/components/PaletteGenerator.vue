<template>
  <div class="palgen">
    <div class="palgen-canvas" :style="`grid-template-${orientation}: 4fr 1fr;`">
      <div>
        <img v-if="palette" :src="palette.image" class="image" />
      </div>
      <div
        class="palgen-colors"
        :style="
          `grid-template-${
            orientation === 'rows' ? 'columns' : 'rows'
          }: repeat(${colorNum}, 1fr);`
        "
      >
        <div
          :key="idx"
          v-for="(col, idx) in colorNum"
          :style="`background: ${randomColors[idx]};`"
        />
      </div>
    </div>
    <div class="palgen-controls" v-if="palette">
      <vs-tooltip not-arrow primary border-thick>
        <vs-button icon warn transparent @click="decColorNum()">
          <i class="bx bx-minus-circle"></i>
        </vs-button>
        <template #tooltip>
          Remove Color
        </template>
      </vs-tooltip>
      <vs-tooltip not-arrow primary border-thick>
        <vs-button icon warn transparent @click="incColorNum()">
          <i class="bx bx-plus-circle"></i>
        </vs-button>
        <template #tooltip>
          Add Color
        </template>
      </vs-tooltip>
      <vs-tooltip not-arrow primary border-thick>
        <vs-button
          icon
          danger
          transparent
          @click="loadRandomColors(colorNum, palette.colors)"
        >
          <i class="bx bx-shuffle"></i>
        </vs-button>
        <template #tooltip>
          Randomize Palette Colors
        </template>
      </vs-tooltip>
      <vs-tooltip not-arrow primary border-thick>
        <vs-button
          icon
          dark
          transparent
          @click="orientation = orientation === 'rows' ? 'columns' : 'rows'"
        >
          <i :class="toggleIcon"></i>
        </vs-button>
        <template #tooltip>
          Toggle Palette Orientation
        </template>
      </vs-tooltip>
    </div>
  </div>
</template>

<script>
export default {
  name: "PaletteGenerator",
  props: {
    palette: Object,
  },
  computed: {
    toggleIcon: function() {
      return `bx bx-${
        this.orientation === "rows" ? "grid-vertical" : "grid-horizontal"
      }`;
    },
  },
  data() {
    return {
      colorNum: 7, // number of colors to load with the palette - default: 7
      randomColors: [], // random selected colors corresponding to the 'colors' array in the passed in palette obj
      orientation: "rows", // orientation for the palette & colors
    };
  },
  watch: {
    palette: function(newPalette) {
      // upon palette load/change, use rng to load up the default number of colors
      if (newPalette && newPalette.colors && newPalette.colors.length) {
        this.loadRandomColors(this.colorNum, newPalette.colors);
      }
    },
  },
  methods: {
    incColorNum() {
      if (this.colorNum < 12) {
        this.colorNum += 1;
        const randomColors = this.randomColors;
        randomColors.push(this.getRandomColor(this.$props.palette.colors));
        console.log("increment", randomColors);
        this.randomColors = randomColors;
      }
    },
    decColorNum() {
      if (this.colorNum > 1) {
        this.colorNum -= 1;
        const randomColors = this.randomColors;
        randomColors.pop();
        this.randomColors = randomColors;
      }
    },
    getRandomIdx(max) {
      return Math.floor(Math.random() * Math.floor(max));
    },
    getRandomColor(colorsArray) {
      // randomizes and returns a single color
      //    inneficient, but checks randomColors for duplicates
      const rgb = colorsArray[this.getRandomIdx(colorsArray.length)];
      return `rgb(${rgb[0]},${rgb[1]},${rgb[2]})`;
    },
    loadRandomColors(amount, colorsArray) {
      // selects {amount} of random idx positions to load randomIdxs with.
      //  Used to select random colors in display
      const randomIdxs = new Set();
      while (randomIdxs.size < amount) {
        randomIdxs.add(this.getRandomIdx(colorsArray.length));
      }
      this.randomColors = [...randomIdxs].map(idx => {
        const rgb = colorsArray[idx];
        return `rgb(${rgb[0]},${rgb[1]},${rgb[2]})`;
      });
    },
  },
};
</script>

<style scoped>
.palgen {
  height: inherit;
  display: flex;
  justify-content: center;
  align-items: center;
  position: relative;
}

.palgen-canvas {
  max-width: 65%;
  display: grid;
  grid-gap: 1rem;
}

.palgen-canvas > div {
  width: inherit;
}

.palgen-canvas > div > .image {
  width: 100%;
}

.palgen-controls {
  position: absolute;
  right: 0;
  bottom: 0;
  display: flex;
}

.palgen-colors {
  display: grid;
  grid-gap: 1rem;
}

.palgen-colors > * {
  height: 100%;
  width: 100%;
}
</style>
