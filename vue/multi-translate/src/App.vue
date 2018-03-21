<template>
  <v-app>
    <v-content>
      <v-container>
        <v-layout justify-center>
          <v-flex xs16 sm12 md8>
            <v-card>
              <p v-if="isLoading">Loading...</p>
              <translate-form v-if="isEditing"/>
              <translation v-if="isDisplaying"></translation>
            </v-card>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<script>
import TranslateForm from './components/TranslateForm'
import Translation from './components/Translation'

const states = {
  EDITING: 'editing',
  LOADING: 'loading',
  DISPLAYING: 'displaying'
}

export default {
  data() {
    return {
      title: 'Multi-Translate',
      state: states.EDITING
    };
  },
  name: 'App',
  components: {
    'translate-form': TranslateForm,
    'translation': Translation
  },
  computed: {
    isEditing() {
      return this.$store.getters.isEditing
    },

    isLoading() {
      return this.$store.getters.isLoading
    },

    isDisplaying() {
      return this.$store.getters.isDisplaying
    }
  }
};
</script>
