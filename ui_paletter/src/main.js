import Vue from "vue";
import Vuesax from "vuesax";
import "vuesax/dist/vuesax.css";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import 'boxicons';

Vue.use(Vuesax, {
  colors: {
    // primary: "#8FC2E0",
    primary: "#CAAEA2",
    success: "#AFCB90",
    warning: "#FDC49B",
    danger: "#B26C96",
    dark: "#503F48",
  },
});

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App),
}).$mount("#app");
