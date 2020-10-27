<template>
  <div class="palgen">
    <div class="palgen-canvas">
      <img v-if="palette" :src="palette.image">
    </div>
  </div>
</template>

<script>
export default {
  name: "PaletteGenerator",
  props: {
    palette: Object,
  }
};
</script>

<style scoped>
.palgen {
  height: inherit;
}

.palgen-canvas > img {
  max-width: 65%;
}

</style>
