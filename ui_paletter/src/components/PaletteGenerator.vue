<template>
  <div class="palgen">
    <div class="palgen-canvas">
      <div>
        <img v-if="palette" :src="palette.image" class="image" />
      </div>
      <div class="palgen-colors" style="grid-template-columns: repeat(7, 1fr);">
        <div
          :key="idx"
          v-for="(col, idx) in 7"
          :style="`background: ${randomColors[idx]}`"
        />
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "PaletteGenerator",
  props: {
    palette: Object,
  },
  data() {
    return {
      colorNum: 7, // number of colors to load with the palette - default: 7
      randomColors: [], // random selected colors corresponding to the 'colors' array in the passed in palette obj
    };
  },
  // mounted: function() {},
  watch: {
    palette: function(newPalette) {
      // upon palette load/change, use rng to load up the default number of colors
      if (newPalette && newPalette.colors && newPalette.colors.length) {
        this.loadColors(this.colorNum, newPalette.colors);
      }
    },
  },
  methods: {
    loadColors(amount, colorsArray) {
      // selects {amount} of random idx positions to load randomIdxs with.
      //  Used to select random colors in display
      const getRandomIdx = max => {
        return Math.floor(Math.random() * Math.floor(max));
      };
      const randomIdxs = new Set();
      while (randomIdxs.size < amount) {
        randomIdxs.add(getRandomIdx(this.$props.palette.colors.length));
      }
      console.log(
        "RANDOS: ",
        [...randomIdxs].map(idx => {
          const rgb = colorsArray[idx];
          return `rgb(${rgb[0]},${rgb[1]},${rgb[2]})`;
        })
      );
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
}

.palgen-canvas {
  max-width: 65%;
  display: grid;
  grid-gap: 1rem;
  grid-template-rows: 4fr 1fr;
}

.palgen-canvas > div {
  width: inherit;
}

.palgen-canvas > .palgen-colors {
  display: grid;
  grid-gap: 1rem;
}

.palgen-canvas > .palgen-colors > * {
  height: 100%;
  width: 100%;
}

.palgen-canvas > div > .image {
  width: 100%;
}
</style>
