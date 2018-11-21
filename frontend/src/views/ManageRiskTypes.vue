<style src="../scss/ManageRiskTypes.scss" lang="scss" scoped></style>
<template>
<section class="manage-risk-type">
    <h1>Manage the Risk Types</h1>
     <div class="manage-risk-type--content row">
<form @submit.stop.prevent="handleAction(form)" class="manage-risk-type--content-fields row">
   <textfield v-model="form.name" label="name"  class="col-4" :is-required="true"/>
   <textfield v-model="form.description" label="description" class="col-6"/>
   <button class="manage-risk-type--action-new col-2" v-if="!updateRisk" :disabled="!form.name">Add</button>
   <button class="manage-risk-type--action-new col-2" v-if="updateRisk" :disabled="!form.name">Update</button>
</form>
<div class="manage-risk-type--content-header">
        <li>
          <ul class="row">
            <li class="col-4">Name</li>
            <li class="col-6">Description</li>
            <li class="col-1"></li>
            <li class="col-1"></li>
          </ul>
        </li>
      </div>
      <div class="manage-risk-type--list">
        <li v-for="(risktype, index) in risktypes" :key='index'>
          <ul class="row">
            <li class="col-4">{{ risktype.name }}</li>
            <li class="col-6">{{ risktype.description }}</li>
            <li class="col-1"><span @click="deleteRiskType(risktype.id)"><icon-garbage class="icon-garbage"/></span></li>
            <li class="col-1"><span @click="editRiskType(risktype)"><icon-edit class="icon-edit"/></span></li>
          </ul>
        </li>
      </div>
    </div>
  </section>
</template>


<script>
import Textfield from '@/components/plugins/textfield/Textfield'
import { toast } from '@/components/plugins/alert'
import { IconEdit, IconGarbage } from '@/components/plugins/icon'

export default {
  name: "risktypes",
  components: {
    Textfield,
    IconEdit,
    IconGarbage
  },
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
        this.createRiskType()
      } else {
        this.updateRiskType(payload)
      }
    },

    fetchRiskTypes() {
        
      this.$risktypes.$fetchRiskTypes()
       .then(res=> {this.risktypes = res;})
       .catch((err) => {console.error(err)})
    },

    createRiskType() {

      const payload = { name: this.form.name, description: this.form.description};
        this.$risktypes.$createRiskType(payload)
           .then(() => {
             this.cleanFields()
             this.fetchRiskTypes()
             toast.success('Risk type created', 'Success!')
           })
           .catch((err) => {
             console.error(err)
             toast.error('Server internal error', 'Error!')})
    },

    deleteRiskType(id) {
     this.$risktypes.$deleteRiskType(id).then(() => {
        this.risktypes = this.risktypes.filter(m => m.id !== id)
        this.fetchRiskTypes();
        toast.success('Risk type removed', 'Success!')
    })
       .catch((err) => {
         console.error(err)
         toast.error('Server internal error', 'Error!')})
    },
    updateRiskType(payload) {
        this.$risktypes.$updateRiskType(payload.id, payload)
          .then(() => {
            this.cleanFields()
            toast.success('Risk type updated', 'Success!')})
          .catch((err) => {
            console.error(err)
            toast.error('Server internal error', 'Error!')})
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
