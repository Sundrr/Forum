<template>
  <div class="container">
    <slot></slot>
  </div>
</template>


<style scoped>
.container {
  /*box-shadow: 0 2px 8px rgba(0, 0, 0, 0.26);*/
  outline: 1px solid #000;
  padding: 0.5rem;
  margin: 0.5rem auto;
  max-width: 120rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}
.container:hover {
    background-color: #c3f3f1;
}
</style>
