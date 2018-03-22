<template>
  <v-app>
    <v-content>
      <v-container>
        <v-layout justify-center class="mt-3">
          <v-flex xs16 sm12 md8>
            <div class="mb-4">
              <center>
                <h1 class="display-1 grey--text text--darken-3">Multi Translator</h1>
                <p class="subheading grey--text text--darken-1">Run your phrase through multiple languages in Google Translate</p>
              </center>
            </div>
            <v-card>
              <v-alert
                :value="$store.getters.hasError"
                color="error"
              >
                {{ $store.getters.error }}
              </v-alert>
              <div v-if="isLoading" class="pt-5 pb-5 mx-auto">
                <v-layout justify-center>
                  <v-progress-circular indeterminate :size="50" color="blue"></v-progress-circular>
                </v-layout>
                <br>
                <v-layout justify-center>
                  <span class="subheading">Translating...</span>
                </v-layout>
              </div>
              <translate-form v-if="isEditing"/>
              <translation v-if="isDisplaying"></translation>
            </v-card>
          </v-flex>
        </v-layout>

        <v-layout justify-center class="mt-4 mb-3">
          <v-flex xs16 sm12 md8>
            <center class="pt-3 pb-3">
              <link href="https://fonts.googleapis.com/css?family=Cookie" rel="stylesheet">
              <a class="bmc-button" target="_blank" href="https://www.buymeacoffee.com/BSPKn39"><img src="https://www.buymeacoffee.com/assets/img/BMC-btn-logo.svg" alt="Buy me a coffee"><span style="margin-left:5px">Buy me a coffee</span></a>
              <br>
              <span class="caption grey--text text--darken-1">
                I personally cover all of the costs to host this application.
                Any help is appreciated!
              </span>
              <br>
              <br>
              <a href="https://github.com/benmusch/multi-translate" target="_blank">
                <v-icon>fab fa-github</v-icon>
              </a>
            </center>
          </v-flex>
        </v-layout>
      </v-container>
    </v-content>
  </v-app>
</template>

<style>
.bmc-button img{width: 27px !important;margin-bottom: 1px !important;box-shadow: none !important;border: none !important;vertical-align: middle !important;}.bmc-button{line-height: 36px !important;height:37px !important;text-decoration: none !important;display:inline-flex !important;color:#000000 !important;background-color:#FFFFFF !important;border-radius: 3px !important;border: 1px solid transparent !important;padding: 1px 9px !important;font-size: 23px !important;letter-spacing: 0.6px !important;box-shadow: 0px 1px 2px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;margin: 0 auto !important;font-family:'Cookie', cursive !important;-webkit-box-sizing: border-box !important;box-sizing: border-box !important;-o-transition: 0.3s all linear !important;-webkit-transition: 0.3s all linear !important;-moz-transition: 0.3s all linear !important;-ms-transition: 0.3s all linear !important;transition: 0.3s all linear !important;}.bmc-button:hover, .bmc-button:active, .bmc-button:focus {-webkit-box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;text-decoration: none !important;box-shadow: 0px 1px 2px 2px rgba(190, 190, 190, 0.5) !important;opacity: 0.85 !important;color:#000000 !important;}
</style>

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
