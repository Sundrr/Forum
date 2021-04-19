<template>
  <base-container>
    <div class="name-column">
      <h4>
        <router-link :to="threadRoute">{{ name }}</router-link>
      </h4>
    </div>
    <thread-paginator
      :post-count="postCount"
      :id="id"
      :tag="tag"
      :current-page="null"
    ></thread-paginator>
    <div>
      {{ postCount }}
    </div>
    <div>
      {{ viewCount }}
    </div>
    <div>
      <p>{{ creator }}</p>
      <p>{{ created }}</p>
    </div>
  </base-container>
</template>


<script>
import ThreadPaginator from "../elements/ThreadPaginator.vue";

export default {
  components: { ThreadPaginator },
  props: {
    id: { type: Number },
    name: { type: String },
    created: { type: String },
    creator: { type: String },
    postCount: { type: Number },
    viewCount: { type: Number },
    tag: { type: String },
  },
  computed: {
    threadRoute() {
      return {
        name: "post-list",
        params: {
          threadId: this.id,
          sectionTag: this.tag,
          page: 1,
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