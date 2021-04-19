<template>
  <header>
    <router-link :to="{path: '/index'}">
      <h1>ВелоФорум</h1>
    </router-link>
    <div id="is-auth" v-if="isAuthenticated">
      <p>Вы вошли как {{ activeUser }}</p>
      <base-button @click="logoutUser">Выйти</base-button>
    </div>
    <div id="no-auth" v-else>
      <base-button link :to="{path: '/login'}">Войти</base-button>
      <base-button link :to="{path: '/register'}">Зарегистрироваться</base-button>
    </div>
  </header>
</template>


<script>
import BaseButton from "../ui/BaseButton.vue";
export default {
  components: { BaseButton },
  methods: {
    logoutUser() {
      this.$store.commit("setToken", null);
      this.$store.commit("setUser", null);
      this.$router.replace("/index");
    },
  },
  computed: {
    isAuthenticated() {
      return this.$store.getters.isAuthenticated;
    },
    activeUser() {
      return this.$store.getters.activeUser;
    },
  },
};
</script>


<style scoped>
header {
  width: 100%;
  height: 5rem;
  background-color: #12A3EB;
  color: white;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
a,
button {
  text-decoration: none;
  color: white;
  border-color: white;
  background-color: #12A3EB;
}

div {
  display: flex;
  justify-content: space-between;
  align-items: center;
}
</style>