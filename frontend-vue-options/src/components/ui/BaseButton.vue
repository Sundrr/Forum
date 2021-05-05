<template>
  <button :class="mode" v-if="!link">
    <slot></slot>
  </button>
  <router-link :class="mode" v-else :to="to">
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
    mode: {
      type: String,
      required: false,
      default: null,
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
  margin-bottom: 0.5rem;
  display: inline-block;
  border-radius: 8px;
}

.main {
  background-color: #12A3EB;
  color: white;
  font-weight: bold;
  border: none;
  border-radius: 8px;
}
</style>