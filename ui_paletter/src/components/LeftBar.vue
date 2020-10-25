<template>
  <div class="hidden">
    <vs-sidebar absolute hover-expand v-model="active" open id="sidebar-custom">
      <div @click="changeView">
        <vs-sidebar-item id="addPal">
          <template #icon>
            <i class="bx bx-plus"></i>
          </template>
          add new palette
        </vs-sidebar-item>
      </div>
      <div @click="changeView">
        <vs-sidebar-item id="genPal">
          <template #icon>
            <i></i>
          </template>
          Palettes
        </vs-sidebar-item>
      </div>
    </vs-sidebar>
  </div>
</template>
<script>
export default {
  name: "LeftBar",
  props: {
    currentView: String,
  },
  data() {
    return {
      active: this.currentView,
    };
  },
  methods: {
    changeView() {
      this.$emit("change-view", this.active);
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
