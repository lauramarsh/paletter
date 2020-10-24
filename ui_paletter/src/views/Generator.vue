<template>
  <div class="Generator">
    <PaletteGenerator />
  </div>
</template>

<script>
// @ is an alias to /src
import PaletteGenerator from "@/components/PaletteGenerator.vue";

export default {
  name: "Generator",
  components: {
    PaletteGenerator
  }
};
</script>