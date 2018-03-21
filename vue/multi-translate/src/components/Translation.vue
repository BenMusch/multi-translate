<template>
  <v-expansion-panel expand focusable light>
    <v-expansion-panel-content
      v-for="(translation, i) in translationChain"
      :value="i == 0"
      :key="i">
      <div slot="header">{{translation.language.name}}</div>
      <v-card>
        <v-card-text :class="i == 0 ? 'display-1' : 'headline'">{{translation.text}}</v-card-text>
      </v-card>
    </v-expansion-panel-content>
  </v-expansion-panel>
</template>

<script>
export default {
  computed: {
    translationChain() {
      return this.$store.getters.translation
    },
  }
}
</script>
