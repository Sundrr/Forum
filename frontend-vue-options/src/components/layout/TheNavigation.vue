<template>
  <div class="nav">
    <section class="nav-structure">
      <router-link :to="{ path: '/index' }"
        ><h2>Список форумов</h2></router-link
      >
      <h2 v-if="currentSectionId">></h2>
      <router-link v-if="currentSectionId" :to="sectionRoute"
        ><h2>{{ currentSectionName }}</h2></router-link
      >
      <h2 v-if="currentThreadId">></h2>
      <router-link v-if="currentThreadId" :to="threadRoute"
        ><h2>{{ currentThreadName }}</h2></router-link
      >
    </section>
  </div>
</template>


<script>
export default {
  computed: {
    currentSectionId() {
      return this.$store.getters.getCurrentSectionId;
    },
    currentSectionName() {
      return this.$store.getters.getCurrentSectionName;
    },
    currentThreadId() {
      return this.$store.getters.getCurrentThreadId;
    },
    currentThreadName() {
      return this.$store.getters.getCurrentThreadName;
    },
    sectionRoute() {
      const currentSectionTag = this.$store.getters.getCurrentSectionTag;
      return {
        name: "thread-list",
        params: {
          sectionId: this.currentSectionId,
          sectionTag: currentSectionTag,
        },
      };
    },
    threadRoute() {
      const currentSectionTag = this.$store.getters.getCurrentSectionTag;
      return {
        name: "post-list",
        params: {
          threadId: this.currentThreadId,
          sectionTag: currentSectionTag,
        },
      };
    },
  },
};
</script>


<style scoped>
.nav-structure {
  height: 3rem;
  width: 100%;
  margin: 0.5rem 0;
  padding: 0 1rem;
  background-color: #b4dcf3;
  border-radius: 8px;
  display: flex;
  align-items: center;
}

.nav-structure * {
  padding-right: 2px;
}

a {
  color: white;
}

h2 {
  color: #105289;
  font-size: 14px;
}
</style>
