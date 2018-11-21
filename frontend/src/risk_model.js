import axios from 'axios'

const $risks = axios.create({
  baseURL: 'api/v1/',
  timeout: 5000,
  headers: { 'Content-Type': 'application/json' }
})

// Response Interceptor to handle and log errors
$risks.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // eslint-disable-next-line
  console.log(error)
  return Promise.reject(error)
})

$risks.$fetchRisk = (id) => {
  return $risks.get(`risks/${id}`)
    .then(response => response.data)
}

$risks.$fetchRisks = () => {
  return $risks.get(`risks/`)
    .then(response => response.data)
}

$risks.$fetchRisksByRiskType = (id) => {
  return $risks.get(`risks/list-by-risk-type/`, {risk_type_id: id})
    .then(response => response.data)
}


$risks.$createRisk = (payload) => {
  return $risks.post(`risks/`, payload)
    .then(response => response.data)
}

$risks.$updateRisk = (payload, id) => {
  return $risks.put(`risks/${id}`, payload)
    .then(response => response.data)
}

$risks.$deleteRisk = (id) => {
  return $risks.delete(`risks/${id}`)
    .then(response => response.data)
}

export default $risks
