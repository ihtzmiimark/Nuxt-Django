<template>
    <div class="card library-card">
      <img :src="library.picture" class="card-img-top" >
      <div class="card-body">
        <h5 class="card-title">{{ library.title }}</h5>
        <p class="card-text">
          <strong>Author:</strong> {{ library.author }}
        </p>
        <p class="card-text">
          <strong>Description:</strong> {{ library.description }}
        </p>
        <p class="card-text">
          <strong>Category:</strong> {{ library.category }}
        </p>
        <div class="action-buttons">
          <nuxt-link :to="`/library/${library.id}/`" class="btn btn-sm btn-success">View</nuxt-link>
          <nuxt-link :to="`/library/${library.id}/edit/`" class="btn btn-sm btn-primary">Edit</nuxt-link>
          <button @click="onDelete(library.id)" class="btn btn-sm btn-danger">Delete</button>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
      props: ["library", "onDelete"]
  };
  </script>
  
  <style>
  .library-card {
      box-shadow: 0 1rem 1.5rem rgba(0,0,0,.6);
  }
  </style>