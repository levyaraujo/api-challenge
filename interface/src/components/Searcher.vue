<template>
  <div id="searcher">
    <h3 id="title">Obter dados da planilha de cadastro de operadoras</h3>
    <div class="input-group">
      <input
        type="search"
        class="form-control rounded search-box"
        placeholder="Pesquisar"
        aria-label="Search"
        aria-describedby="search-addon"
        v-model="query"
        id="search-box"
        v-on:keyup.enter="getData"
      />
      <button class="btn btn-primary" type="button" @click="getData">
        <img src="../assets/icons/search.svg" />
      </button>
    </div>
    <div v-if="infos.length > 0" class="cards">
      <div class="card" v-for="item of infos">
        <p v-for="(value, key) in item">
          <span class="key">{{ key }}: </span>
          <span class="value">{{ value }}</span>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      query: "",
      infos: [],
    };
  },
  methods: {
    getData: function () {
      axios
        .create({
          baseURL: "http://127.0.0.1:5000/",
          params: {
            key: this.query,
          },
        })
        .get("search")
        .then((response) => {
          if (response.data.length > 0) this.infos = response.data;
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
}

#searcher h3 {
  margin-bottom: 30px;
}

.input-group {
  display: flex;
  justify-content: center;
}

.search-box {
  max-width: 600px;
}

.btn {
  margin-right: 10px;
  border-radius: 5px;
  margin: 0;
}

.cards {
  display: grid;
  max-width: 90%;
  margin: 50px auto;
  grid-template-columns: repeat(3, 1fr);
  gap: 20px;
  text-align: left;
}

.card {
  box-shadow: 5 3 3px rgba(0, 0, 0, 0.1);
  line-height: 1.5;
  max-width: 100%;
  padding: 20px;
}

.key {
  color: purple;
  font-size: 20px;
}

.value {
  color: black;
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
</style>
