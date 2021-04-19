<template>
  <the-header></the-header>
  <the-navigation></the-navigation>
  <main>
    <router-view :key="$route.path"></router-view>
  </main>
  <the-footer></the-footer>
</template>


<script>
import TheHeader from "./components/layout/TheHeader.vue";
import TheNavigation from "./components/layout/TheNavigation.vue";
import TheFooter from "./components/layout/TheFooter.vue";

export default {
  components: { TheHeader, TheNavigation, TheFooter },
};
</script>


<style>
body {
  font-family: Verdana, Arial, Helvetica, sans-serif;
}

a {
  text-decoration: none;
  color: #000;
}
</style>