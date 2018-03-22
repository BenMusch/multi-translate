import axios from 'axios';

const TRANSLATE_URL = 'https://266ic11wl4.execute-api.us-east-1.amazonaws.com/api/translate'

const translatePhrase = (text, numTranslations) => {
  return axios({
    method: 'post',
    url: TRANSLATE_URL,
    data: { text: text, numTranslations: numTranslations },
    headers: { 'Content-Type': 'application/json' }
  })
}

export default { translatePhrase }
