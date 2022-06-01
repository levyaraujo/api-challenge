<template>
  <main id="searcher">
    <h3 id="title">Pesquisar dados na tabela</h3>
    <div class="input-group">
      <input
        type="search"
        class="form-control rounded search-box"
        placeholder="Pesquisar"
        aria-label="Search"
        aria-describedby="search-addon"
        v-model="query"
        id="search-box"
        v-on:keyup.enter="query.length >= 4 ? getData() : pass"
      />
      <button
        class="btn btn-primary"
        type="button"
        @click="query.length >= 4 ? getData() : pass"
        :disabled="query.length < 4"
      >
        <img src="../assets/icons/search.svg" />
      </button>
    </div>
    <span v-if="query.length < 4">Digite pelo menos 4 letras</span>
    <h1 class="message">{{ request_info }}</h1>
    <div v-show="display" class="cards">
      <div class="card" v-for="item of infos">
        <p v-for="(value, key) in item">
          <span class="key">{{ key }}: </span>
          <span class="value">{{ value }}</span>
        </p>
      </div>
    </div>
  </main>
</template>

<script>
import "vue-router";
import axios from "axios";
export default {
  data() {
    return {
      query: "",
      infos: [],
      request_info: null,
      display: true,
    };
  },
  methods: {
    getData: function () {
      axios
        .create({
          baseURL: "http://127.0.0.1:5000/",
          params: {
            key: this.query.trim(),
          },
        })
        .get("search")
        .then((response) => {
          if (response.data.length > 0) {
            this.infos = response.data;
            this.request_info = `A pesquisa encontrou ${this.infos.length} resultados`;
            this.display = true;
          } else {
            this.request_info = "Nenhum resultado foi encontrado. 😥";
            this.display = false;
          }
        });
    },
  },
};
</script>

<style>
#searcher {
  top: 150px;
  position: absolute;
  text-align: center;
  color: #282828;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  justify-content: center;
}

.input-group {
  display: flex;
  justify-content: center;
}

.search-box {
  width: 300px;
  background: None;
}

.search-box:hover {
  border-color: #eeefef;
}

.btn {
  margin-right: 10px;
  border-radius: 5px;
  margin: 0;
}

.message {
  margin-top: 70px;
}

.cards {
  display: grid;
  max-width: 90%;
  margin: 50px auto;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  text-align: left;
  animation-name: slide;
  animation-duration: 1s;
  animation-fill-mode: forwards;
  transform: translateY(-100px);
}

.card {
  opacity: 0;
  background-color: #eeefef;
  line-height: 1.5;
  max-width: 100%;
  padding: 20px;
  border: 1px solid #f8f9fa;
  animation-name: slide;
  animation-duration: 1s;
  animation-fill-mode: forwards;
  transform: translateX(-100px);
}

.key {
  font-size: 20px;
  font-weight: bold;
  color: rgba(0, 0, 0, 0.5);
}

.value {
  font-size: 17px;
}

footer {
  text-align: left;
  padding-left: 25px;
}

@media (max-width: 950px) {
  .cards {
    display: flex;
    flex-direction: column;
  }
}

@media (max-width: 570px) {
  .cards {
    display: flex;
    flex-direction: column;
  }
}

@media (max-width: 1100px) {
  .cards {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
  }
}

@keyframes slide {
  from {
    opacity: 0;
  }
  to {
    transform: translateX(0);
    opacity: 1;
  }
}
</style>
