<template>
  <div class="MainLanding">
    <Main helloMsg="For Paletter" />
  </div>
</template>

<script>
// @ is an alias to /src
import Main from "@/components/Main.vue";

export default {
  name: "MainLanding",
  components: {
    Main
  }
};
</script>