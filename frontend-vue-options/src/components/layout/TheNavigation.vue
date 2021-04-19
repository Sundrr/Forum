<template>
  <div class="nav">
    <section class="nav-structure">
      <router-link :to="{ path: '/index' }">Список форумов</router-link>
      <p v-if="currentSectionId">></p>
      <router-link v-if="currentSectionId" :to="sectionRoute">{{
        currentSectionName
      }}</router-link>
      <p v-if="currentThreadId">></p>
      <router-link v-if="currentThreadId" :to="threadRoute">{{
        currentThreadName
      }}</router-link>
    </section>
    <section>
      Личный раздел
      Новых Сообщений
      Ваши сообщения
    </section>
    <section>
      Текущее время
      Предыдущее посещение
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
  background-color: #eef5f9;
  display: flex;
  align-items: center;
}

a {
  color: #536482;
}
</style>
