<template>
  <base-container>
    <template #name-block>
      <router-link :to="sectionRoute">
        <div class="name-column">
          <h4>
            {{ name }}
          </h4>
          <p>{{ description }}</p>
        </div>
      </router-link>
    </template>
    <template #stat-block>
      <router-link :to="sectionRoute">
        <div>
          {{ threadCount }}
        </div>
      </router-link>
    </template>
    <template #count-block>
      <div>
        {{ postCount }}
      </div>
    </template>
    <template #user-block>
      <div>
        <p>{{ lastUsername }}</p>
        <p>{{ lastDate }}</p>
      </div>
    </template>
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
p {
  color: #105289;
  margin: 4px 0;
}

.name-column p {
  color: #4c5d77;
}

h4 {
  margin: 4px 0;
}

a {
  color: #105289;
  margin: 0;
}
</style>
