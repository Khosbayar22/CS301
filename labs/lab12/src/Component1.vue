<template>
  <div>
    <h3>Үргэлжилсэн хувиарлалтын арга</h3>
    <div>
      <div style="display: flex; margin-bottom: 32px">
        <div class="cylinder" style="margin-right: 16px">
          <div class="input-container">
            <div class="input-item" v-for="i in memory" :key="i" style="display: flex; justify-content: center; align-items: center">
              <span style="margin-right: 4px">{{ i.address }}</span>
              <div v-if="i.state" style="width: 10px; height: 10px" :style="`background-color: #${i.color}`"></div>
              <div v-else style="width: 10px; height: 10px; background-color: #ddd"></div>
            </div>
          </div>
        </div>
        <div>
          <table>
            <tr>
              <th>Файл нэр</th>
              <th>Эхлэх хаяг</th>
              <th>Файлын урт</th>
            </tr>
            <tr v-for="i in data" :key="i">
              <td>{{ i.file_name }}</td>
              <td>{{ i.start_id }}</td>
              <td>{{ i.length }}</td>
            </tr>
          </table>
        </div>
      </div>
      <div>
        <form>
          <label for="file_name">Файл нэр</label><br>
          <input type="text" id="file_name" v-model="file_name"><br>
          <label for="start_id">Эхлэх хаяг</label><br>
          <input type="number" id="start_id" v-model="start_id"><br>
          <label for="length">Файлын урт</label><br>
          <input type="number" id="length" v-model="length"><br>
          <br>
          <button @click="addData()" type='button'>Нэмэх</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ComponentOne',
  data() {
    return {
      file_name: null,
      start_id: null,
      length: null,
      data: [{
        "file_name": "count",
        "start_id": 0,
        "length": 2,
      }],
      memory: []
    }
  },
  mounted() {
    this.setMemory()
  },
  methods: {
    // randomColor() {
    //   console.log(Math.floor(Math.random()*16777215).toString(16))
    //   return Math.floor(Math.random()*16777215).toString(16);
    // },
    setMemory() {
      const length = 32;
      const memory = []
      for (let i = 0; i < length; i++) {
        const data = this.data.find(j => j.start_id === i);
        if (data) {
          const color = Math.floor(Math.random()*16777215).toString(16)
          for (let j = data.start_id; j < data.start_id + data.length; j++) {
            memory.push({address: i, state: true, color: color})
            i++;
          }
        }
        memory.push({address: i, state: false})
      }
      this.memory = memory;
    },
    addData() {
      this.data.push({
        file_name: this.file_name,
        start_id: this.start_id,
        length: this.length,
      })
      const color = Math.floor(Math.random()*16777215).toString(16)
      for (let i = this.start_id; i < (this.start_id + this.length); i++) {
        const temp = this.memory.find(j => j.address === i)
        temp.state = true
        temp.color = color
      }
    }
  }
}
</script>