<template>
  <base-container @click="$router.push(threadRoute)" style="cursor: pointer">
    <template #name-block>
      <div class="name-column">
        <h4>
          {{ name }}
        </h4>
      </div>
      <thread-paginator
        :post-count="postCount"
        :id="id"
        :tag="tag"
        :current-page="null"
      ></thread-paginator>
    </template>
    <template #stat-block>
      <div>
        {{ postCount }}
      </div>
    </template>
    <template #count-block>
      <div>
        {{ viewCount }}
      </div>
    </template>
    <template #user-block>
      <div>
        <p>{{ creator }}</p>
        <p>{{ created }}</p>
      </div>
    </template>
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
p {
  color: #105289;
  margin: 4px 0;
}

h4 {
  margin: 4px 0;
}

a {
  color: #105289;
  margin: 0;
}
</style>