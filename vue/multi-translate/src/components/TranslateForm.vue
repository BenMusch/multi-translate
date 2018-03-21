<template>
  <v-container fluid class="pt-4 pb-4 pl-4 pr-4">
    <h1>Create your translation</h1>
    <v-form @submit.prevent="submit" class="mt-2">
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
      <v-btn @click.prevent="submit" color="info">Translate</v-btn>
    </v-form>
  </v-container>
</template>

<script>
import translateHelpers from '../helpers/translate'
import { SET_ERROR_MESSAGE, SET_TRANSLATION, SET_LOADING } from '../store/mutationTypes'

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
      translateHelpers.translatePhrase(this.text, this.languageCount)
        .then(response => this.$store.commit(SET_TRANSLATION, { translation: response.data }))
        .catch(error => this.$store.commit(SET_ERROR_MESSAGE, { message: error.response.data.Message }))
      this.$store.commit(SET_LOADING)
    }
  }
}
</script>
