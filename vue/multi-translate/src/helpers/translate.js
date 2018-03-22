import axios from 'axios';

const TRANSLATE_URL = 'http://localhost:8000/translate'

const translatePhrase = (text, numTranslations) => {
  return axios({
    method: 'post',
    url: TRANSLATE_URL,
    data: { text: text, numTranslations: numTranslations },
    headers: { 'Content-Type': 'application/json' }
  })
}

export default { translatePhrase }
