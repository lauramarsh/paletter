<template>
  <div class="add">
    <div class="add_form">
      <div class="title">
        <p>add a new palette</p>
      </div>
      <div class="fields">
        <div class="fields_upload">
          <input type="file" name="file" id="file" @change="onFileChange" />
          <vs-button
            danger
            gradient
            :active="isUploading"
            @click="handleUpload"
          >
            <label for="file" style="z-index: 1000;">
              Upload Image/Gif
            </label>
          </vs-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "AddPalette",
  props: {},
  data() {
    return {
      isUploading: false,
    };
  },
  methods: {
    handleUpload() {
      this.isUploading = true;
    },
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) return;
      this.createImage(files[0]);
    },
    // createImage(file) {
    //   var image = new Image();
    //   var reader = new FileReader();
    //   var vm = this;

    //   reader.onload = (e) => {
    //     vm.image = e.target.result;
    //   };
    //   reader.readAsDataURL(file);
    // },
  },
};
</script>

<style>
.add {
  height: inherit;
}

.add_form {
  text-align: center;
}

.fields_upload {
  display: flex;
  justify-content: center;
  align-items: center;
}

.fields_upload div.vs-button__content {
  padding: 0px;
}

.fields_upload input {
  display: none;
}

.fields_upload label {
  padding: 10px;
  cursor: pointer;
}
</style>
