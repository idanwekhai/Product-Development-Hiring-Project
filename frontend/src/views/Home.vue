<style src="../scss/Home.scss" lang="scss" scoped></style>
<template>
  <section class="risk">
    <h1>Select the risk</h1>
    <div class="risk--type-content row">
      <combofield v-model="form.risk_type" :content="riskTypes" label="risk type" class="col-6"/>
      <combofield v-model="form.risk" :content="risks" label="risk" class="col-6"/>
    </div>

    <div class="risk--content row">
      <h3 v-if="fieldsByRisk.length">Risk fields / information</h3>

      <component class="fields-by-risk-elements"
        v-for="(fieldByRisk, index) in fieldsByRisk" :key='index'
        :is="mapFieldsId[fieldByRisk.id]"
        :label="fieldByRisk.label"
        v-model="fieldsByRisk.value"
        :content="fieldsByRisk.value"
      >
      </component>
    </div>

    <div class="actions col-12">
      <button class="button--save col-4" disabled @click="registerNewFieldsByRisk(fields)">Save</button>
    </div>

  </section>
</template>

<script>
import Textfield from '@/components/plugins/textfield/Textfield'
import Numberfield from '@/components/plugins/numberfield/Numberfield'
import Datefield from '@/components/plugins/datefield/Datefield'
import Combofield from '@/components/plugins/combofield/Combofield'
import { IconEdit, IconGarbage } from '@/components/plugins/icon'

export default {
  name: 'home',
  components: {
    Textfield,
    Numberfield,
    Combofield,
    Datefield,
    IconEdit,
    IconGarbage
  },
  data () {
    return {
      errors: [],
      riskTypes: [],
      risks: [],
      fieldTypes: [],
      mapFieldsId: [
        '',
        'Textfield',
        'Numberfield',
        'Datefield',
        'Combofield'
      ],
      fieldsByRisk: [],
      form: {
        risk_type: '',
        field_type: '',
        field_label: '',
        risk: ''
      }
    }
  },
  mounted () {
    this.setContentType()
  },
  filters: {
    fieldTypeFilter (term, fieldtypes) {
      return fieldtypes.filter(item => item.id === term)[0].name
    }
  },
  watch: {
    'form.risk_type' (risktype) {
      if (risktype) {
        this.setRisks(risktype)
      }
    },
    'form.risk' (risk) {
      if (risk) {
        this.setFieldsByRisk(risk)
      }
    }
  },
  methods: {
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
        .catch(err => console.error(err))
    },
    setAllFieldTypes () {
      this.$fieldtypes.$fetchFieldTypes()
        .then(res => {this.fieldTypes = res})
        .catch(err => console.error(err))
    },
    setRisks (id) {
      this.$risks.$fetchRisksByRiskType(id)
        .then(res => {this.risks = res})
        .catch(err => console.error(err))
    },
    setFieldsByRisk (id) {
      this.$fieldbyrisks.$fetchFieldByRisk(id)
        .then(res => {this.fieldsByRisk = res})
        .catch(err => console.error(err))
    }
  }
}
</script>
