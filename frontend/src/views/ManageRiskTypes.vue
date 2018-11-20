<template>
  <div class="risktypes">
   <input type="text" placeholder="name" v-model="form.name">
   <input type="text" placeholder="description" v-model="form.description">
   <input type="submit" v-if="!updateRisk" value="Add" @click="createRiskType" :disabled="!form.name">
   <input type="submit" v-if="updateRisk" value="Update" @click="editRiskType" :disabled="!form.name">

   <h2>Risk Types</h2>
   <p v-if="risktypes.length === 0">No RiskTypes </p>
   <div class="risktype" v-for="(risktype, index) in risktypes" :key="index">
    <p class="risktype-id">[{{index}}]</p>
    <p class="risktype-name" v-html="risktype.name"></p>
    <p class="risktype-description" v-html="risktype.description"></p>
    <input type="submit" @click="editRiskType(risktype)" value="Edit" />
    <input type="submit" @click="deleteRiskType(risktype.id)" value="Delete" />
  </div>
 </div>
</template>


<script>
export default {
  name: "RiskTypes",
  data() {
    return {
      errors: [],
      risktypes: [],
      form: {
        name: "",
        description: "",  
      },
      updateRisk: false
     
    }
  },
  mounted() {
    this.fetchRiskTypes();
  },
  methods: {

    handleAction (payload) {
      if (!this.updateRisk) {
        this.createRiskType(payload)
      } else {
        this.updateRiskType(payload)
      }
    },

    fetchRiskTypes() {
        
      this.$risktypes.$fetchRiskTypes().then(responseData => {
        this.risktypes = responseData;
      })
      .catch((err) => {
          console.error(err)
       })
    },

    createRiskType() {

      const payload = { name: this.form.name, description: this.form.description};
        this.$risktypes.$createRiskType(payload)
           .then(() => {
             this.cleanFields()
             this.fetchRiskTypes()
           })
           .catch((err) => {
            console.error(err)
           })
    },

    deleteRiskType(id) {
     this.$risktypes.$deleteRiskType(id).then(() => {
        this.risktypes = this.risktypes.filter(m => m.id !== id)
        this.fetchRiskTypes();
    })
     .catch((err) => {
        console.error(err)
      })
    },
    updateRiskType(payload) {
        this.$risktype.$updateRiskType(payload.id, payload)
          .then(() => {
            this.cleanFields()
          })
          .catch((err) => {
          console.error(err)
          })
    },

    editRiskType(payload) {
        this.updateRisk = true
        this.form = payload
    },

    cleanFields() {
        this.form = {
            name: '',
            description: ''
        }
    },
  }
}
</script>
