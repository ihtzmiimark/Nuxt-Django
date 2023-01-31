<template>
    <main class="container my-5">
      <div class="row">
        <div class="col-12 text-center my-3">
          <h2 class="mb-3 display-4 text-uppercase">{{ library.title }}</h2>
        </div>
        <div class="col-md-6 mb-4">
        </div>
        <div class="col-md-6">
          <div class="library-details">
            <h2>Author</h2>
            <p>{{ library.author }}</p>
            <h3>Category</h3>
            <p>{{ library.category }}</p>
            <textarea class="form-control" rows="10" v-html="library.description" disabled />
          </div>
        </div>
      </div>
    </main>
  </template>
  
  <script>
  export default {
    head() {
      return {
        title: "View Library"
      };
    },
    async asyncData({ $axios, params }) {
      try {
        let library = await $axios.$get(`/library/${params.id}`);
        return { library };
      } catch (e) {
        return { library: [] };
      }
    },
    data() {
      return {
        library: {
          title: "",
          author: "",
          description: "",
          type: "",
        }
      };
    }
  };
  </script>
  
  <style scoped>
  </style>