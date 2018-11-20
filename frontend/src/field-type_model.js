import axios from 'axios'

const $fieldtypes = axios.create({
  baseURL: 'api/v1/',
  timeout: 5000,
  headers: { 'Content-Type': 'application/json' }
})

// Response Interceptor to handle and log errors
$fieldtypes.interceptors.response.use(function (response) {
  return response
}, function (error) {
  // eslint-disable-next-line
  console.log(error)
  return Promise.reject(error)
})

$fieldtypes.$fetchFieldType = (id) => {
  return $fieldtypes.get(`field-types/${id}`)
    .then(response => response.data)
}

$fieldtypes.$fetchFieldTypes = () => {
  return $fieldtypes.get(`field-types/`)
    .then(response => response.data)
}

$fieldtypes.$createFieldType = (payload) => {
  return $fieldtypes.post(`field-types/`, payload)
    .then(response => response.data)
}

$fieldtypes.$updateFieldType = (payload, id) => {
  return $fieldtypes.put(`field-types/${id}`, payload)
    .then(response => response.data)
}

$fieldtypes.$deleteFieldType = (id) => {
  return $fieldtypes.delete(`field-types/${id}`)
    .then(response => response.data)
}

export default $fieldtypes
