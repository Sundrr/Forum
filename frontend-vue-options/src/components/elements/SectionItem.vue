<template>
  <base-container>
    <div class="name-column">
      <h4>
        <router-link :to="sectionRoute">{{ name }}</router-link>
      </h4>
      <p>{{ description }}</p>
    </div>
    <div>
      {{ threadCount }}
    </div>
    <div>
      {{ postCount }}
    </div>
    <div>
      <p>{{ lastUsername }}</p>
      <p>{{ lastDate }}</p>
    </div>
  </base-container>
</template>


<script>
export default {
  props: {
    id: { type: Number },
    name: { type: String },
    description: { type: String },
    tag: { type: String },
    threadCount: { type: Number },
    postCount: { type: Number },
    lastUsername: { type: String },
    lastDate: { type: String },
  },
  computed: {
    sectionRoute() {
      return {
        name: "thread-list",
        params: {
          sectionId: this.id,
          sectionTag: this.tag,
        },
      };
    },
  },
};
</script>


<style scoped>
.name-column {
  width: 40rem;
}
</style>
