<template>
    <main class="container my-5">
      <div class="row">
        <div class="col-12 text-center my-3">
          <h2 class="mb-3 display-4 text-uppercase">{{ library.title }}</h2>
        </div>
        <div class="col-md-6 mb-4">
          <img v-if="!preview" class="img-fluid" style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"  :src="library.picture">
          <img v-else class="img-fluid" style="width: 400px; border-radius: 10px; box-shadow: 0 1rem 1rem rgba(0,0,0,.7);"  :src="preview">
        </div>
        <div class="col-md-4">
          <form @submit.prevent="submitLibrary">
            <div class="form-group">
              <label for>Book <Title></Title></label>
              <input type="text" class="form-control" v-model="library.title" >
            </div>
            <div class="form-group">
              <label for>Author</label>
              <input type="text" v-model="library.author" class="form-control" name="Author" >
            </div>
            <div class="form-group">
              <label for>category</label>
              <input type="text" v-model="library.category" class="form-control" name="Category" >
            </div>
            <div class="form-group">
              <label for>Description</label>
              <input type="text" v-model="library.description" class="form-control" name="Description" >
            </div>
            <button type="submit" class="btn btn-success">Save</button>
          </form>
        </div>
      </div>
    </main>
  </template>
  
  <script>
  export default {
    head(){
        return {
          title: "Edit library"
        }
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
          category: "",
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
        this.library.picture = files[0]
        this.createImage(files[0]);
      },
      createImage(file) {
        let reader = new FileReader();
        let vm = this;
        reader.onload = e => {
          vm.preview = e.target.result;
        };
        reader.readAsDataURL(file);
      },
      async submitLibrary() {
        let editedlibrary = this.library
        const config = {
          headers: { "content-type": "multipart/form-data" }
        };
        let formData = new FormData();
        for (let data in editedlibrary) {
          formData.append(data, editedlibrary[data]);
        }
        try {
          let response = await this.$axios.$patch(`/library/${editedlibrary.id}/`, formData, config);
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