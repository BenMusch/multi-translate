<template>
  <v-container fluid>
    <h1>Create your translation</h1>
    <v-form>
      <v-text-field
        name="text"
        label="Text to translate"
        placeholder="Hello, world"
        multi-line
        rows="1"
      ></v-text-field>
      <v-text-field
        name="languageCount"
        label="Number of languages to translate through"
        type="number"
        placeholder="5"
        :full-width="false"
      ></v-text-field>
      <v-btn>Translate</v-btn>
    </v-form>
  </v-container>
</template>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
