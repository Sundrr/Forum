<template>
  <ul>
    <p v-for="page in pageCollection" :key="page.value" :class="page.class">
      <router-link :to="threadRoute(page.value)">{{ page.value }}</router-link>
    </p>
  </ul>
</template>


<script>
import Consts from "../../const.js";

export default {
  props: {
    id: { type: Number },
    tag: { type: String },
    answers: { type: Number },
    currentPage: { type: Number },
  },
  data() {
    return {};
  },
  methods: {
    threadRoute(pageNum) {
      return {
        name: "post-list",
        params: {
          threadId: this.id,
          sectionTag: this.tag,
          page: pageNum,
        },
        query: {
          page: pageNum,
        },
      };
    },
    createPageArray() {
      const pageNumber = Math.ceil(this.answers / Consts.PAGINATE_LIMIT);
      return Array.from({ length: pageNumber }, (_, i) => i + 1);
    },
    processArrayNoCurrentPage(pageArray) {
      const arrayLen = pageArray.length;
      if (arrayLen === 1) {
        return [];
      } else if (arrayLen > 5) {
        const elementsToDelete = arrayLen - 4;
        pageArray.splice(1, elementsToDelete, "...");
      }
      return pageArray;
    },
    processArrayHasCurrentPage(pageArray) {
      let elementsToDelete;
      let cut;
      const arrayLen = pageArray.length;
      const currentPagePosition =
        pageArray.indexOf(parseInt(this.currentPage)) + 1;
      console.log("currentPagePosition", currentPagePosition);
      if (arrayLen === 1) {
        pageArray = [];
      }
      if (currentPagePosition > 4) {
        elementsToDelete = currentPagePosition - 4;
        cut = pageArray.splice(1, elementsToDelete, "...");
        console.log("cutBefore", cut);
      }
      if (arrayLen - currentPagePosition > 4) {
        elementsToDelete = arrayLen - currentPagePosition - 3;
        console.log('params', currentPagePosition + 2, elementsToDelete);
        cut = pageArray.splice(
          currentPagePosition + 1,
          elementsToDelete,
          "..."
        );
        console.log("cutAfter", cut);
      }
      return pageArray;
    },
    createPaginateCollection(paginateArray) {
      let arrayData;
      let itemClass;
      const paginateCollection = [];
      for (const item of paginateArray) {
        arrayData = {};
        arrayData["value"] = item;
        if (typeof item === "string") {
          itemClass = "";
        } else if (item === this.currentPage) {
          itemClass = "page-link-active";
        } else {
          itemClass = "page-link";
        }
        arrayData["class"] = itemClass;
        paginateCollection.push(arrayData);
      }
      return paginateCollection;
    },
  },
  computed: {
    pageCollection() {
      const pageArray = this.createPageArray();
      let processedArray;
      if (this.currentPage) {
        processedArray = this.processArrayHasCurrentPage(pageArray);
      } else {
        processedArray = this.processArrayNoCurrentPage(pageArray);
      }
      const paginateCollection = this.createPaginateCollection(processedArray);
      return paginateCollection;
    },
  },
};
</script>


<style scoped>
ul {
  display: flex;
  justify-content: left;
  padding: 0;
}

.page-link {
  margin: 2px;
  padding: 1px;
  border: 1px solid black;
}

.page-link-active {
  margin: 2px;
  padding: 1px;
  border: 1px solid black;
  background-color: #faf606;
  color: white;
}
</style>