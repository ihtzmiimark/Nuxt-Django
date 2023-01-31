<template>
    <main class="container my-5">
      <div class="row">
        <div class="col-12 text-center my-3">
          <h2 class="mb-3 display-4 text-uppercase">{{ library.author }}</h2>
        </div>
        <div class="col-md-4">
          <form @submit.prevent="submitLibrary">
            <div class="form-group">
              <label for>Book title</label>
              <input type="text" class="form-control" v-model="library.title">
            </div>
            <div class="form-group">
              <label for>Author</label>
              <input v-model="library.author" type="text" class="form-control">
            </div>
            <div class="form-group">
              <label for>Category</label>
              <input v-model="library.category" type="text" class="form-control">
            </div>
            <div class="form-group">
              <label for>Description</label>
              <input v-model="library.description" type="text" class="form-control">
            </div>
            <div class="row">
              <div class="col-md-6">
              </div>
            </div>
            <button type="submit" class="btn btn-primary">Submit</button>
          </form>
        </div>
      </div>
    </main>
  </template>
  
  <script>
  export default {
    head() {
      return {
        title: "Add Library"
      };
    },
    data() {
      return {
        library: {
          author: "",
          picture: "",
          ingredients: "",
          difficulty: "",
          prep_time: null,
          prep_guide: ""
        },
        preview: ""
      };
    },
    methods: {
      onFileChange(e) {
        let files = e.target.files || e.dataTransfer.files;
        if (!files.length) {
          return;
        }
        this.library.picture = files[0];
        this.createImage(files[0]);
      },
      createImage(file) {
        // let image = new Image();
        let reader = new FileReader();
        let vm = this;
        reader.onload = e => {
          vm.preview = e.target.result;
        };
        reader.readAsDataURL(file);
      },
      async submitLibrary() {
        const config = {
          headers: { "content-type": "multipart/form-data" }
        };
        let formData = new FormData();
        for (let data in this.library) {
          formData.append(data, this.library[data]);
        }
        try {
          let response = await this.$axios.$post("/library/", formData, config);
          this.$router.push("/library/");
        } catch (e) {
          console.log(e);
        }
      }
    }
  };
  </script>
  
  <style scoped>
  </style>