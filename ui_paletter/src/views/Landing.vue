<template>
  <div class="MainLanding">
    <transition name="slide-up">
      <TitleCard v-if="isActive" />
    </transition>
  </div>
</template>

<script>
// @ is an alias to /src
import TitleCard from "@/components/TitleCard.vue";
import router from "./../router";

export default {
  created() {
    window.addEventListener("wheel", this.scrollDown);
  },
  destroyed() {
    window.removeEventListener("wheel", this.scrollDown);
  },
  name: "MainLanding",
  components: {
    TitleCard
  },
  data() {
    return {
      isActive: true,
    };
  },
  methods: {
    scrollDown(e) {
      if (e.deltaY > 0) {
        this.isActive = false;
        window.removeEventListener("wheel", this.scrollDown);
        setTimeout(() => {
          router.push("generator");
        }, 850);
      }
    },
  },
};
</script>

<style scoped>
.MainLanding {
  height: inherit;
}

.slide-up-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.1, 0.25, 1);
}

.slide-up-leave-to
/* .slide-fade-leave-active below version 2.1.8 */ {
  transform: translateY(-100vh);
  /* opacity: 0; */
}
</style>