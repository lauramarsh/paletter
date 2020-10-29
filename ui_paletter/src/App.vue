<template>
  <div id="app">
    <div id="border">
      <router-view />
    </div>
  </div>
</template>

<style>
#app {
  font-family: "Inter", sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  height: inherit;
  width: inherit;
}

#border {
  padding: 3rem 6rem;
  height: -webkit-fill-available;
}

@media only screen and (max-width: 768px) {
  /* For mobile phones: */
  #border {
    padding: 0px;
    height: 100%;
  }
}
</style>
