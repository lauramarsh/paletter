<template>
  <div class="Generator">
    <LeftBar
      :paletteNamesById="paletteNamesById"
      :currentView="currentView"
      @change-view="changeView"
      @change-palette="changePalette"
    />
    <keep-alive>
      <component
        :is="currentViewComponent"
        v-bind="currentViewProps"
        @added-palette="addedPalette"
      >
      </component>
    </keep-alive>
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
    currentPalId: 0,
    palettes: {},
    paletteNamesById: {},
  }),
  async mounted() {
    const fetchPalettes = () => {
      return axios.get("http://127.0.0.1:8000/palettes/");
    };
    const fetchedPalettes = await fetchPalettes();

    const palettes = {};
    const paletteNamesById = {};
    fetchedPalettes.data.forEach(pal => {
      palettes[pal.id] = pal;
      paletteNamesById[pal.id] = pal.name;
    });

    const initialView = fetchedPalettes.data.length
      ? `${fetchedPalettes.data[0].name} ${fetchedPalettes.data[0].id}`
      : "addPal";

    this.palettes = palettes;
    this.paletteNamesById = paletteNamesById;
    this.currentView = initialView;
    this.currentPalId = fetchedPalettes.data.length
      ? fetchedPalettes.data[0].id
      : 0;
  },
  watch: {
    paletteNamesById: async function(newMap, oldMap) {
      if (Object.keys(newMap).length !== Object.keys(oldMap).length) {
        const fetchPalettes = () => {
          return axios.get("http://127.0.0.1:8000/palettes/");
        };

        const fetchedPalettes = await fetchPalettes();
        const palettes = {};
        const paletteNamesById = {};
        fetchedPalettes.data.forEach(pal => {
          palettes[pal.id] = pal;
          paletteNamesById[pal.id] = pal.name;
        });
        this.palettes = palettes;
        this.paletteNamesById = paletteNamesById;
      }
    },
  },
  methods: {
    changeView(newView) {
      this.currentView = newView;
    },
    changePalette(newId) {
      this.currentPalId = newId;
    },
    addedPalette({ id, name }) {
      this.$set(this.paletteNamesById, id, name);
    },
  },
  computed: {
    currentViewComponent() {
      return this.currentView === "addPal" ? AddPalette : PaletteGenerator;
    },
    currentViewProps() {
      if (this.currentViewComponent === PaletteGenerator) {
        return { palette: this.palettes[this.currentPalId] };
      } else {
        return {};
      }
    },
  },
};
</script>

<style>
.Generator {
  height: inherit;
}
</style>
