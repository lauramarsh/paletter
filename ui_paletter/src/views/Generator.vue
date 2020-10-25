<template>
  <div class="Generator">
    <LeftBar :currentView="currentView" @change-view="changeView" />
    <component :is="currentViewComponent"> </component>
  </div>
</template>

<script>
// @ is an alias to /src
import AddPalette from "@/components/AddPalette.vue";
import PaletteGenerator from "@/components/PaletteGenerator.vue";
import LeftBar from "@/components/LeftBar.vue";

export default {
  name: "Generator",
  components: {
    PaletteGenerator,
    LeftBar,
    AddPalette,
  },
  data: () => ({
    currentView: "genPal",
  }),
  methods: {
    changeView(newView) {
      this.currentView = newView;
    },
  },
  computed: {
    currentViewComponent() {
      const viewToComponent = {
        addPal: "AddPalette",
        genPal: "PaletteGenerator",
      };
      return viewToComponent[this.currentView];
    },
  },
};
</script>

<style>
.Generator {
  height: inherit;
}
</style>
