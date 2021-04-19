<template>
  <base-container>
    <div>
      <div>
        <p>{{ username }}</p>
        <p>{{ created }}</p>
      </div>
      <p>{{ text }}</p>
    </div>
  </base-container>
</template>


<script>
export default {
  props: {
    id: { type: Number },
    username: { type: String },
    created: { type: String },
    text: { type: String },
  },
};
</script>


<style scoped>
</style>