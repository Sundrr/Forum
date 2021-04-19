<template>
  <button v-if="!link">
    <slot></slot>
  </button>
  <router-link v-else :to="to">
    <slot></slot>
  </router-link>
</template>


<script>
export default {
  props: {
    link: {
      type: Boolean,
      required: false,
      default: false,
    },
    to: {
      type: Object,
      required: false,
    },
  },
};
</script>


<style scoped>
button,
a {
  text-decoration: none;
  padding: 0.75rem 1.5rem;
  font: inherit;
  border: 1px solid #000;
  cursor: pointer;
  margin-right: 0.5rem;
  display: inline-block;
}
</style>