<template>
  <div>
    <h3>Холбоост хуваарилалт арга</h3>
    <div>
      <div style="display: flex; margin-bottom: 32px">
        <div class="cylinder" style="margin-right: 16px">
          <div class="input-container">
            <div class="input-item" v-for="i in main_memory" :key="i">
              <span style="margin-right: 4px">{{ i }}</span>
              <div v-if="!isFreeMemory(i)" class="memory-block"></div>
              <div v-else class="memory-block" :style="`background-color: #${isFreeMemory(i).color}`">
                {{ isFreeMemory(i).next }}
              </div>
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
            <tr v-for="i in table_data" :key="i">
              <td>{{ i.file_name }}</td>
              <td>{{ i.start_index }}</td>
              <td>{{ i.file_length }}</td>
            </tr>
          </table>
        </div>
      </div>
      <div>
        <form>
          <label for="file_name">Файл нэр</label><br>
          <input type="text" id="file_name" v-model="file_name"><br>
          <label for="start_index">Эхлэх хаяг</label><br>
          <input type="number" id="start_index" v-model="start_index"><br>
          <label for="length">Файлын урт</label><br>
          <input type="number" id="length" v-model="file_length"><br>
          <br>
          <button @click="allocateMemory()" type='button'>Нэмэх</button>
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
      start_index: null,
      file_length: null,
      main_memory: [],
      free_memory: [],
      allocated_memory: [],
      table_data: [],
    }
  },
  mounted() {
    this.setMemory()
  },
  methods: {
    getRandom() {
      if (this.free_memory.length <= 0) {
        return
      }
      const random_index = Math.floor((Math.random() * this.free_memory.length))
      this.free_memory = this.free_memory.filter((i) => i !== random_index)
      return random_index
    },
    setMemory() { 
      const length = 32;
      this.main_memory = Array(length).fill(null).map((_, i) => i);
      this.free_memory = Array(length).fill(null).map((_, i) => i);
    },
    allocateMemory() {
      const color = Math.floor(Math.random() * 16777215).toString(16)

      const allocated_memory = []
      let current = this.start_index
      this.free_memory = this.free_memory.filter((i) => i !== current)

      for (let i = 0; i < this.file_length; i += 1) {
        if (i === this.file_length - 1) {
          allocated_memory.push({
            'address': current,
            'next': '-1',
            'color': color
          })
        }
        else {
          const removedItem = this.getRandom()
          allocated_memory.push({
            'address': current,
            'next': removedItem,
            'color': color
          })
          current = removedItem;
        }
      }

      this.allocated_memory = this.allocated_memory.concat(allocated_memory);

      this.table_data.push({
        'file_name': this.file_name,
        'start_index': this.start_index,
        'file_length': this.file_length,
      })
    },
    isFreeMemory(index) {
      const tmp = this.allocated_memory.find((i) => i.address === index)
      if (tmp) {
        return tmp
      }
      return false;
    },
  }
}
</script>

<style>
.input-item {
  display: flex;
  justify-content: center;
  align-items: center;
}

.memory-block {
  width: 10px;
  height: 10px;
  background-color: #ddd;
}
</style>