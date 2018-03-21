<template>
  <pre>{{ translation }}</pre>
</template>

<script>
export default {
  computed: {
    translation() {
      return this.$store.getters.translation
    }
  }
}
</script>
