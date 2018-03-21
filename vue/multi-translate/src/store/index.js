import Vue from "vue"
import Vuex from "vuex";

import * as types from "./mutationTypes"

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    "translation": [
      {"text":"Hello, this is a test","language":{"code":"en","name":"English"}},{"text":"Bună, acesta este un test","language":{"code":"ro","name":"Romanian"}},{"text":"హాయ్, ఈ ఒక పరీక్ష","language":{"code":"te","name":"Telugu"}},{"text":"Hi, dit is in test","language":{"code":"fy","name":"Frisian"}},{"text":"ਅਧਿਕਤਮ, ਇਸ ਨੂੰ ਇੱਕ ਟੈਸਟ ਹੁੰਦਾ ਹੈ","language":{"code":"pa","name":"Punjabi"}},{"text":"Cześć, to jest test","language":{"code":"pl","name":"Polish"}},{"text":"Hi, this is a test","language":{"code":"en","name":"English"}}
    ],
    editing: false,
    loading:false,
    displaying: true,
    errorMessage: ""
  },
  getters: {
    translation: state => state.translation,
    errorMessage: state => state.errorMessage,
    isDisplaying: state => state.displaying,
    isLoading: state => state.loading,
    isEditing: state => state.editing
  },
  mutations: {
    [types.SET_LOADING](state) {
      state.editing = false
      state.loading = true
      state.displaying = false
    },

    [types.SET_TRANSLATION](state, { translation }) {
      state.editing = false
      state.loading = false
      state.displaying = true
      state.translation = translation
    }
  }
})
