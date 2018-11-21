<style src="./scss/index.scss" lang="scss"></style>
<template>
  <div id="app">
    <div id="nav">
      <router-link to="/"><button class="button">Home</button></router-link> 
      <router-link to="/risks"><button class="button">Manage Risks</button></router-link> 
      <router-link to="/risk-types"><button class="button">Manage Risk Types</button></router-link>
    </div>
    <router-view/>
  </div>
</template>

<style>
#app {
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
.button {
    background: #60b964;
    color: white;
    border-top-width: 0px;
    border-left-width: 0px;
    border-bottom-width: 0px;
    border-right-width: 0px;
    padding-top: 15px;
    padding-right: a2;
    padding-left: 15px;
    padding-bottom: 15‒;
    padding-right: 15px;
    padding-bottom: 15px;
    margin-left: 20px;
    border-radius: 12px;
  }
</style>
