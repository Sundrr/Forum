<template>
  <post-container>
    <div>
      <div>
        <p>{{ username }}</p>
        <p>{{ created }}</p>
      </div>
      <p>{{ text }}</p>
    </div>
  </post-container>
</template>


<script>
import PostContainer from "../ui/PostContainer.vue";

export default {
  components: { PostContainer },
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