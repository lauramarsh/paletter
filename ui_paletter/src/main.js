import Vue from "vue";
import Vuesax from "vuesax";
import 'vuesax/dist/vuesax.css';
import App from "./App.vue";
import router from "./router";
import store from "./store";

Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");

Vue.use(Vuesax, {
  colors: {
    primary:'#8FC2E0',
    success:'#BAD29F',
    warning:'#FCAC73',
    danger:'#B26C96',
    dark:'#503F48'
  }
});
