<template>
    <main class="container mt-5">
      <div class="row">
        <div class="col-12 text-right mb-4">
          <div class="d-flex justify-content-between">
            <h3>La library</h3>
            <nuxt-link to="/library/add" class="btn btn-info">Add library</nuxt-link>
          </div>
        </div>
        <template v-for="library in library">
          <div :key="library.id" class="col-lg-3 col-md-4 col-sm-6 mb-4">
            <library-card :onDelete="deletelibrary" :library="library"></library-card>
          </div>
        </template>
      </div>
    </main>
  </template>
  
  <script>
import libraryCard from "~/components/libraryCard.vue";

export default {
  head() {
    return {
      title: "library list"
    };
  },
  components: {
    libraryCard
  },
  async asyncData({ $axios, params }) {
    try {
      let library = await $axios.$get(`/library/`);
      return { library };
    } catch (e) {
      return { library: [] };
    }
  },
  data() {
    return {
      library: []
    };
  },
  methods: {
    async deletelibrary(library_id) {
      try {
        await this.$axios.$delete(`/library/${library_id}/`); // delete recipe
        let newLibrary = await this.$axios.$get("/library/"); // get new list of library
        this.library = newLibrary; // update list of library
      } catch (e) {
        console.log(e);
      }
    }
  },
  mounted(){
  }
};
</script>
  
  <style scoped>
  </style>