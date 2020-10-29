<template>
  <div class="MainLanding">
    <transition name="slide-up">
      <TitleCard v-if="isActive" @scroll-down="scrollDown" />
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
  mounted() {
    setTimeout(() => {
      this.isActive = true;
    }, 200);
  },
  destroyed() {
    this.isActive = false;
    window.removeEventListener("wheel", this.scrollDown);
  },
  name: "MainLanding",
  components: {
    TitleCard
  },
  data() {
    return {
      isActive: false,
    };
  },
  methods: {
    scrollDown(e, bypass=false) {
      if (bypass || e.deltaY > 0) {
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

.slide-up-enter {
  transform: translateY(100vh);
  /* opacity: 0; */
}

.slide-up-enter-active {
  transition: all 1s cubic-bezier(.22,.68,0,1);
}

.slide-up-leave-active {
  transition: all 0.8s cubic-bezier(1, 0.1, 0.25, 1);
}

.slide-up-leave-to {
  transform: translateY(-100vh);
}
</style>