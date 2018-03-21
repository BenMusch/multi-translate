<template>
  <v-container fluid>
    <h1>Create your translation</h1>
    <v-form @submit.prevent="submit">
      <v-text-field
        name="text"
        label="Text to translate"
        placeholder="Hello, world"
        v-model="text"
        multi-line
        rows="1"
      ></v-text-field>
      <v-text-field
        name="languageCount"
        label="Number of languages to translate through"
        type="number"
        placeholder="5"
        v-model="languageCount"
        :full-width="false"
      ></v-text-field>
      <v-btn @click.prevent="submit">Translate</v-btn>
    </v-form>
  </v-container>
</template>

<script>
import axios from 'axios'

export default {
  name: 'TranslateForm',
  data() {
    return {
      text: "",
      languageCount: ""
    }
  },

  methods: {
    submit() {
      console.log(this.text, this.languageCount)
    }
  }
}
</script>
