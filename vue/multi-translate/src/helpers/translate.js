import axios from 'axios';

const TRANSLATE_URL = 'https://translate-api.benmuschol.com/translate'

const translatePhrase = (text, numTranslations) => {
  return axios({
    method: 'post',
    url: TRANSLATE_URL,
    data: { text: text, numTranslations: numTranslations },
    headers: { 'Content-Type': 'application/json' }
  })
}

export default { translatePhrase }
