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
      languageCount: 5
    }
  },

  methods: {
    submit() {
      const getErrorMessage = (e) => {
        if (e.response && e.response.data && e.response.data.Message) {
          return e.response.data.Message
        } else {
          return "An unknown error occurred"
        }
      }
      translateHelpers.translatePhrase(this.text, this.languageCount)
        .then(response => this.$store.commit(SET_TRANSLATION, { translation: response.data }))
        .catch(e => this.$store.commit(SET_ERROR_MESSAGE, { message: getErrorMessage(e) }))
      this.$store.commit(SET_LOADING)
    }
  }
}
</script>
