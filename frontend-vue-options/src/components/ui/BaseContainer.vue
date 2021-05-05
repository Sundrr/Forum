<template>
  <div class="base-container">
    <table>
      <tr>
        <td class="name-block">
          <slot name="name-block"></slot>
        </td>
        <td class="stat-block">
          <slot name="stat-block"></slot>
        </td>
        <td class="count-block">
          <slot name="count-block"></slot>
        </td>
        <td class="user-block">
          <slot name="user-block"></slot>
        </td>
      </tr>
    </table>
  </div>
</template>


<style scoped>
.base-container {
  background-color: #b4dcf3;
  border-bottom: 1px solid #12A3EB;
}

.header-container {
  background-color: #12A3EB;
  border-bottom: 1px solid #12A3EB;
}

table {
  width: 100%;
  table-layout: fixed;
  border-collapse: collapse;
}

td {
  background-color: #b4dcf3;
  color: #105289;
}

.header-containter td {
  background-color: #12a3eb;
  color: white;
}

.name-block {
  width: 45%;
  padding: 0 16px;
  border-right: 1px solid #12A3EB;
}

.stat-block {
  width: 10%;
  text-align: center;
  border-right: 1px solid #12A3EB;
}

.count-block {
  width: 10%;
  text-align: center;
  border-right: 1px solid #12A3EB;
}

.user-block {
  width: 25%;
  padding: 0 16px;
}

tr:hover td {
  background-color: #f9fad3;
}

.header-containter tr:hover td {
  background-color: #12A3EB;
}
</style>
