<script>
import Header from "./components/Header.vue";
import Searcher from "./components/Searcher.vue";
export default {
  components: {
    Header,
    Searcher,
  },
};
</script>

<template>
  <div id="app">
    <Header />
    <Searcher />
  </div>
</template>

<style>
* {
  font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", Roboto,
    "Helvetica Neue", Arial, sans-serif;
}

body {
  background-color: #fffefc;
}

#app {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: auto;
}
</style>
