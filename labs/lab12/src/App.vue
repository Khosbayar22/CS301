<template>
  <div style="display: flex; gap: 32px">
    <Component1 />
    <Component2 />
  </div>
</template>

<script>
import Component1 from "./Component1"
import Component2 from "./Component2"
export default {
  name: 'App',
  components: {
    Component1,
    Component2,
  }
}
</script>

<style>
* {
  font-family: Arial;
}

.input-container {
  display: grid;
  grid-template-columns: 1fr 1fr 1fr 1fr;
  gap: 16px
}

.cylinder {
  width: auto;
  height: auto;
  margin: 10% auto;
  display: inline-block;
  position: relative;
  background-color: #87CEEB;
  border: 1px solid #000;
  margin: 0;
  border-radius: 50% / 5%;

}

.input-container {
  margin: 32px 16px;
}

.input-item {
  position: relative;
  z-index: 100;
}

.cylinder:before {
  content: '';
  display: inline-block;
  width: 100%;
  height: 25px;
  background: #87CEEB;
  border-radius: 100% / 100%;
  position: absolute;
  border: 1px solid #000;
  top: -1px;
  z-index: 2;
}

.cylinder:after {
  content: '';
  display: inline-block;
  width: 179px;
  height: 25px;
  border-radius: 100% / 100%;
  position: absolute;
  z-index: 1;
}
</style>