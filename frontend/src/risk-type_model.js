import axios from 'axios'

const $risktypes = axios.create({
  baseURL: 'api/v1/',
  timeout: 5000,
  headers: { 'Content-Type': 'application/json' }
})

// Response Interceptor to handle and log errors
$risktypes.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // eslint-disable-next-line
  console.log(error)
  return Promise.reject(error)
})

$risktypes.$fetchRiskType = (id) => {
  return $risktypes.get(`risk-types/${id}`)
    .then(response => response.data)
}

$risktypes.$fetchRiskTypes = () => {
  return $risktypes.get(`risk-types/`)
    .then(response => response.data)
}

$risktypes.$createRiskType = (payload) => {
  return $risktypes.post(`risk-types/`, payload)
    .then(response => response.data)
}

$risktypes.$updateRiskType = (payload, id) => {
  return $risktypes.put(`risk-types/${id}`, payload)
    .then(response => response.data)
}

$risktypes.$deleteRiskType = (id) => {
  return $risktypes.delete(`risk-types/${id}`)
    .then(response => response.data)
}

export default $risktypes
