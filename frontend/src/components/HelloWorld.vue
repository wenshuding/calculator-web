<template>
  <div class="calculator">
    <input v-model="expression" class="input-field" placeholder="Enter expression">
    <button @click="calculate">Calculate</button>
    <p v-if="result">{{ result }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      expression: '',
      result: ''
    };
  },
  methods: {
    calculate() {
      if (this.expression) {
        fetch('http://localhost:5000/calculate', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify({ expression: this.expression })
        })
          .then(response => response.json())
          .then(data => {
            if (data.error) {
              this.result = data.error;
            } else {
              this.result = data.result;
            }
          })
          .catch(error => {
            this.result = `An error occurred:` + error ;
          });
      }
    }
  }
};
</script>

<style scoped>
.calculator {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 50px;
}

.input-field {
  margin-bottom: 10px;
  padding: 5px;
  font-size: 18px;
}

button {
  padding: 10px;
  font-size: 18px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>
