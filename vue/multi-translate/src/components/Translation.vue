<template>
  <v-container>
    <v-layout>
      <h1 class="display-1">Your translation</h1>
      <v-btn class="ml-4" @click.prevent="reset">Go back</v-btn>
    </v-layout>
    <br>
    <v-expansion-panel expand focusable light>
      <v-expansion-panel-content
        v-for="(translation, i) in translationChain"
        :value="i == 0"
        :key="i">
        <div slot="header">{{translation.language.name}}</div>
        <v-card>
          <v-card-text :class="i == 0 ? 'headline' : 'subtitle'"
             v-text="translation.text"></v-card-text>
        </v-card>
      </v-expansion-panel-content>
    </v-expansion-panel>
  </v-container>
</template>

<script>
import { RESET_TRANSLATION } from '../store/mutationTypes'

export default {
  computed: {
    translationChain() {
      return this.$store.getters.translation.reverse()
    },
  },
  methods: {
    reset() {
      this.$store.commit(RESET_TRANSLATION)
    }
  }
}
</script>
