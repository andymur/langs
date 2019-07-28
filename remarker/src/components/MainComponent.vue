<template>
  <div>
    <div @click="gotoWord('prev')">&lt;&mdash;</div>
    <div @click="gotoWord('next')">&mdash;&gt;</div>
    <input type="text" v-model="currentWord" />
    <input type="text" :value="currentWord" />
    <div @click="gotoWord('prev')">&lt;&mdash;</div>
    <div @click="gotoWord('next')">&mdash;&gt;</div>
    <textarea v-model="wordsModel"></textarea>
  </div>
  
</template>

<script>
export default {
  name: 'MainComponent',
  props: {
    words: {
      type: Array
    }
  },
  mounted() {
    // eslint-disable-next-line
    console.log(this.words);
    this.currentWord = this.words[1]
    var wordData = "";
    this.words.forEach(element => {
      wordData += element + "\n"
    });
    this.wordsModel = wordData;
  },
  methods: {
    'gotoWord': function(direction) {
      var word = null;
      var wordCount = this.words.length;

      var currentIndex = this.words.indexOf(this.currentWord);

      if (currentIndex == -1) {
        return;
      }

      if (direction == 'next') {
        if (currentIndex >= wordCount) {
          return;
        }
        word = this.words[currentIndex + 1];
      } else {
        if (currentIndex <= 0) {
          return;
        }
        word = this.words[currentIndex - 1];
      }

      this.$router.push({ name: 'word-edit', params: { word: word }})
    }
  },
  data: function() {
    return {
      wordsModel: "",
      currentWord: null
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
