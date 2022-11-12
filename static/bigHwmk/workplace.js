var Main = {
    data() {
      return {
        activeName: '1'
      };
    }
  }
var Ctor = Vue.extend(Main)
new Ctor().$mount('#app')