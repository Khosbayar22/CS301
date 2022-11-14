<template>
  <div>
    <h3>Холбоост хуваарилалт арга</h3>
    <div>
      <div style="display: flex; margin-bottom: 32px">
        <div class="cylinder" style="margin-right: 16px">
          <div class="input-container">
            <div class="input-item" v-for="i in memory" :key="i">
              <span>{{ i.address }}</span>
              <input type="checkbox" :checked="i.state">
            </div>
          </div>
        </div>
        <div>
          <table>
            <tr>
              <th>Файл нэр</th>
              <th>Эхлэх хаяг</th>
              <th>Дуусах хаяг</th>
            </tr>
            <tr v-for="i in data" :key="i">
              <td>{{ i.file_name }}</td>
              <td>{{ i.start_id }}</td>
              <td>{{ i.end_id }}</td>
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
          <input type="number" id="length" v-model="end_id"><br>
          <br>
          <button @click="addData()" type='button'>Нэмэх</button>
        </form>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'ComponentTwo',
  data() {
    return {
      file_name: null,
      start_id: null,
      end_id: null,
      data: [{
        "file_name": "count",
        "start_id": 9,
        "end_id": 25,
      }],
      memory: []
    }
  },
  mounted() {
    this.setMemory()
  },
  methods: {
    setMemory() {
      const length = 32;
      const memory = []
      for (let i = 0; i < length; i++) {
        const data = this.data.find(j => j.start_id === i);
        if (data) {
          for (let j = data.start_id; j < data.start_id + data.end_id; j++) {
            memory.push({address: i, state: true})
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
        length: this.end_id,
      })
      for (let i = this.start_id; i < (this.start_id + this.end_id); i++) {
        this.memory.find(j => j.address === i).state = true
        console.log(this.memory.find(j => j.address === i))
      }
    }
  }
}
</script>