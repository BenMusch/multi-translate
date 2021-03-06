import Vue from "vue"
import Vuex from "vuex";

import * as types from "./mutationTypes"

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    translation: [],
    editing: true,
    loading:false,
    displaying: false,
    errorMessage: ""
  },
  getters: {
    translation: state => state.translation,
    errorMessage: state => state.errorMessage,
    isDisplaying: state => state.displaying,
    isLoading: state => state.loading,
    isEditing: state => state.editing,
    hasError: state => state.errorMessage !== "",
    error: state => state.errorMessage
  },

  mutations: {
    [types.SET_LOADING](state) {
      state.editing = false
      state.loading = true
      state.displaying = false
      state.errorMessage = ""
    },

    [types.SET_TRANSLATION](state, { translation }) {
      state.editing = false
      state.loading = false
      state.displaying = true
      state.translation = translation
    },

    [types.RESET_TRANSLATION](state) {
      state.editing = true
      state.loading = false
      state.displaying = false
      state.translation = []
    },

    [types.SET_ERROR_MESSAGE](state, { message }) {
      state.editing = true
      state.loading = false
      state.dispalying = false
      state.errorMessage = message
    }
  }
})
