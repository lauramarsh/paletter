<template>
  <div class="Generator">
    <LeftBar
      :paletteNamesById="paletteNamesById"
      :currentView="currentView"
      @change-view="changeView"
    />
    <component :is="currentViewComponent"> </component>
  </div>
</template>

<script>
const axios = require("axios");
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";
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
    currentView: "",
    palettes: [],
    paletteNamesById: {},
  }),
  async mounted() {
    const fetchPalettes = () => {
      return axios.get("http://127.0.0.1:8000/palettes/");
    };

    const palettes = await fetchPalettes();
    const paletteNamesById = {};
    palettes.data.forEach(pal => {
      paletteNamesById[pal.id] = pal.name;
    });
    const initialView = palettes.data.length
      ? `${palettes.data[0].name} ${palettes.data[0].id}`
      : "addPal";

    this.palettes = palettes.data;
    this.paletteNamesById = paletteNamesById;
    this.currentView = initialView;
    console.log(this.currentView, this.palettes, this.paletteNamesById);
  },
  methods: {
    changeView(newView) {
      this.currentView = newView;
    },
  },
  computed: {
    currentViewComponent() {
      return this.currentView === "addPal" ? AddPalette : PaletteGenerator;
    },
  },
};
</script>

<style>
.Generator {
  height: inherit;
}
</style>
