<template>
  <div>
    <h2>{{ helloMsg }}</h2>
  </div>
</template>

<script>
export default {
  name: "Main",
  props: {
    helloMsg: String,
  },
};
</script>

