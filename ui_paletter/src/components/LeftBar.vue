<template>
  <div class="hidden">
    <vs-sidebar
      absolute
      hover-expand
      v-model="currentView"
      open
      id="sidebar-custom"
    >
      <div @click="navigateToAdd">
        <vs-sidebar-item id="addPal">
          <template #icon>
            <i class="bx bx-image-add"></i>
          </template>
          Add new palette
        </vs-sidebar-item>
      </div>
      <vs-sidebar-group>
        <template #header>
          <vs-sidebar-item arrow>
            <template #icon>
              <i class="bx bx-palette"></i>
            </template>
            Palettes
          </vs-sidebar-item>
        </template>
        <div
          v-for="(palette, paletteId) in paletteNamesById"
          :key="palette + paletteId"
          @click="changePalette(palette, paletteId)"
        >
          <vs-sidebar-item :id="`${palette} ${paletteId}`">
            <template #icon>
              <i class="bx bx-radio-circle"></i>
            </template>
            {{ palette }}
          </vs-sidebar-item>
        </div>
      </vs-sidebar-group>
    </vs-sidebar>
  </div>
</template>
<script>
export default {
  name: "LeftBar",
  props: {
    currentView: String,
    paletteNamesById: Object,
  },
  data() {
    return {
      active: this.currentView,
    };
  },
  methods: {
    navigateToAdd() {
      this.$emit("change-view", "addPal");
    },
    changePalette(name, id) {
      this.$emit("change-view", `${name} ${id}`);
      this.$emit("change-palette", id);
    },
  },
};
</script>

<style>
#sidebar-custom {
  margin: 3rem 0px 3rem 6rem;
  max-height: -webkit-fill-available;
}

#sidebar-custom div {
  font-weight: 100;
  letter-spacing: 1px;
}
</style>
