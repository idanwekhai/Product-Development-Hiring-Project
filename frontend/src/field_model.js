import axios from 'axios'

const $fields = axios.create({
  baseURL: 'api/v1/',
  timeout: 5000,
  headers: { 'Content-Type': 'application/json' }
})

// Response Interceptor to handle and log errors
$fields.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // eslint-disable-next-line
  console.log(error)
  return Promise.reject(error)
})

$fields.$fetchField = (id) => {
  return $fields.get(`fields/${id}`)
    .then(response => response.data)
}

$fields.$fetchFields = () => {
  return $fields.get(`fields/`)
    .then(response => response.data)
}

$fields.$createField = (payload) => {
  return $fields.post(`fields/`, payload)
    .then(response => response.data)
}

$fields.$updateField = (payload, id) => {
  return $fields.put(`fields/${id}`, payload)
    .then(response => response.data)
}

$fields.$deleteField = (id) => {
  return $fields.delete(`fields/${id}`)
    .then(response => response.data)
}

export default $fields
