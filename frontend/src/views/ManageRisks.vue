<style src="../scss/ManageRisk.scss" lang="scss" scoped></style>
<template>
  <section class="manage-risk">
    <h1>Manage the Risks</h1>
    <div class="manage-risk--type-content row">
      <combofield v-model="form.riskType" :content="riskTypes" label="risk type" class="col-6"/>
      <textfield v-model="form.name" label="risk name" class="col-6" :is-required="true"/>
    </div>

    <div class="manage-risk--content row">
      <h3>Add the risk fields</h3>
      <form @submit.stop.prevent="handleNewField(form)" class="manage-risk--content-fields row">
        <combofield v-model="form.fieldType" :content="fieldTypes" label="field type" class="col-4"/>
        <textfield v-model="form.fieldLabel" label="field label" class="col-6" :is-required="true"/>
        <button class="manage-risk--action-new col-2">+</button>
      </form>

      <div class="manage-risk--content-header">
        <li>
          <ul class="row">
            <li class="col-4">Field Type</li>
            <li class="col-6">Field Label</li>
            <li class="col-2"></li>
          </ul>
        </li>
      </div>
      <div class="manage-risk--list">
        <li v-for="(field, index) in fieldTypes" :key='index'>
          <ul class="row">
            <li class="col-4">{{ field.name }}</li>
            <li class="col-6">{{ field.description }}</li>
            <li class="col-2"><span @click="removeField(index)"><icon-garbage class="icon-garbage"/></span></li>
          </ul>
        </li>
      </div>
    </div>

    <div class="actions col-12">
      <button class="button--save col-4" disabled @click="createNewFieldsByRisk(fields)">Save</button>
    </div>
  </section>
</template>

<script>
import Textfield from '@/components/plugins/textfield/Textfield'
import Combofield from '@/components/plugins/combofield/Combofield'
import { IconEdit, IconGarbage } from '@/components/plugins/icon'

export default {
  name: 'risks',
  components: {
    Textfield,
    Combofield,
    IconEdit,
    IconGarbage
  },
  data () {
    return {
      errors: [],
      riskTypes: [],
      risks: [],
      fields: [],
      fieldTypes: [],
      form: {
        name: '',
        riskType: '',
        fieldType: '',
        fieldLabel: ''
      }
    }
  },
  mounted () {
    this.setContentType()
  },
  methods: {
    cleanFields () {
        this.form.fieldType = ''
        this.form.fieldLabel = ''
    },
    createNewFieldsByRisk (risk) {
    },
    handleNewField (form) {
      if (form) {
        let field = {
          fieldLabel: form.fieldLabel,
          fieldType: form.fieldType
        }

        this.fields.push(field)
        this.cleanFields()
      }
    },
    setContentType () {
        this.setAllRiskTypes()
        this.setAllFieldTypes()
    },
    setAllRiskTypes () {
        this.$risktypes.$fetchRiskTypes()
          .then(res => {this.riskTypes = res})
          .catch(err => console.log(err))
    },
    setAllFieldTypes () {
        this.$fieldtypes.$fetchFieldTypes()
          .then(res => {this.fieldTypes = res})
          .catch(err => console.log(err))
    },

  }
}
</script>