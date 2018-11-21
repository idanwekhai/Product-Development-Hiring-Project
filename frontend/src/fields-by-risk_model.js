import axios from 'axios'

const $fieldbyrisks = axios.create({
  baseURL: 'api/v1/',
  timeout: 5000,
  headers: { 'Content-Type': 'application/json' }
})

// Response Interceptor to handle and log errors
$fieldbyrisks.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // eslint-disable-next-line
  console.log(error)
  return Promise.reject(error)
})

$fieldbyrisks.$fetchFieldType = (id) => {
  return $fieldtypes.get(`fields-by-risk/${id}`)
    .then(response => response.data)
}

$fieldbyrisks.$fetchFieldByRisk = (risk_id) => {
  return $fieldtypes.get(`fields-by-risk/list-fields-by-risk`, {risk_id: risk_id})
    .then(response => response.data)
}

$fieldbyrisks.$createFieldByRisk = (payload) => {
  return $fieldtypes.post(`fields-by-risk/`, payload)
    .then(response => response.data)
}


export default $fieldbyrisks
