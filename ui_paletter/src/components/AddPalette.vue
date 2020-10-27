<template>
  <div class="add">
    <div class="add_form">
      <div class="fields">
        <div class="fields_upload">
          <div v-if="!image" class="fields_upload-no">
            <input
              type="file"
              name="file"
              id="file"
              accept="image/*"
              multiple="false"
              @change="onFileChange"
            />
            <vs-button
              danger
              border
              :active="isUploading"
              @click="handleUpload"
            >
              <label for="file" class="fields_upload-label">
                <i class="bx bx-cloud-upload"></i>
                Upload Image/Gif
              </label>
            </vs-button>
          </div>
          <div v-else class="fields_upload-yes">
            <img :src="image" />
            <vs-button danger border @click="removeImage">
              <div class="fields_upload-label">
                <i class="bx bx-x"></i> Remove image
              </div>
            </vs-button>
          </div>
        </div>
        <div class="fields_name">
          <vs-input
            success
            state="primary"
            v-model="name"
            placeholder="Palette Name"
          >
            <template #icon>
              <i class="bx bx-text"></i>
            </template>
          </vs-input>
        </div>
        <div class="fields_srcURL">
          <vs-input
            warn
            state="primary"
            v-model="url"
            placeholder="Source URL"
            type="url"
          >
            <template #icon>
              <i class="bx bx-link"></i>
            </template>
          </vs-input>
        </div>
        <div class="fields_srcSTR">
          <vs-input
            danger
            state="primary"
            v-model="urlStr"
            placeholder="Source Title?"
          >
            <template #icon>
              <i class="bx bx-info-circle"></i>
            </template>
          </vs-input>
        </div>
        <div class="fields_submit">
          <vs-button
            danger
            gradient
            :active="isSubmitting"
            @click="handleSubmit"
          >
            Submit
          </vs-button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
const axios = require("axios");
axios.defaults.xsrfCookieName = "csrftoken";
axios.defaults.xsrfHeaderName = "X-CSRFTOKEN";

function initialState() {
  return {
    isUploading: false,
    isSubmitting: false,
    name: "",
    url: "",
    urlStr: "",
    image: "",
  };
}

export default {
  name: "AddPalette",
  props: {},
  data() {
    return initialState();
  },
  methods: {
    handleUpload() {
      this.isUploading = true;
    },
    handleSubmit() {
      this.isSubmitting = true;
      const paletteData = new FormData();
      paletteData.append("name", this.name);
      paletteData.append("image", this.image);
      paletteData.append("source", this.url);
      paletteData.append("source_string", this.urlStr);
      this.createPalette(paletteData);
    },
    onFileChange(e) {
      var files = e.target.files || e.dataTransfer.files;
      if (!files.length) {
        this.isUploading = false;
        return;
      }
      this.createImage(files[0]);
    },
    createImage(file) {
      var reader = new FileReader();
      var vm = this;
      reader.onload = e => {
        vm.image = e.target.result;
        vm.isUploading = false;
      };
      reader.readAsDataURL(file);
    },
    removeImage: function() {
      this.image = "";
      this.isUploading = false;
    },
    async createPalette(paletteData) {
      const postResult = await axios.post(
        "http://127.0.0.1:8000/palettes/",
        paletteData
      );
      console.log("postRes, ", postResult);
      this.$emit("added-palette", {
        id: postResult.data.id,
        name: postResult.data.name,
      });
      Object.assign(this.$data, initialState());
    },
  },
};
</script>

<style>
.add {
  height: inherit;
  --dark: #503f48;
}

.add_form {
  text-align: center;
}

.fields > *,
.fields_upload-yes {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  margin-top: 1rem;
}

.fields_upload-yes > img {
  max-width: 60%;
}

.vs-input__label {
  color: var(--dark) !important;
}

.fields_upload-no div.vs-button__content {
  padding: 0px;
}

.fields_upload-no input {
  display: none;
}

.fields_upload-no label {
  padding: 10px;
  cursor: pointer;
}

.fields_upload-label {
  z-index: 1000;
  display: flex;
  align-items: center;
}

.fields_upload-label > i {
  font-size: large;
  padding-right: 0.5rem;
}
</style>
