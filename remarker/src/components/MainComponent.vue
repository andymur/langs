<template>
  <div>
    <div @click="gotoWord('prev')">&lt;&mdash;</div>
    <div @click="gotoWord('next')">&mdash;&gt;</div>
    <div id="word-editors">
      <input type="text" v-model="currentWordOfModel" />
      <input type="text" :value="currentWordOfModel" />
    </div>
    <div id="wortart-buttons">
      <input type="button" value="Substantiv" v-bind:class="selectedWordArt(currentWord, 'substantiv')" />
      <input type="button" value="Verb" v-bind:class="selectedWordArt(currentWord, 'verb')"/>
      <input type="button" value="Adjektiv" v-bind:class="selectedWordArt(currentWord, 'adjektiv')"/>
      <input type="button" value="Pronomenon" v-bind:class="selectedWordArt(currentWord, 'pronomenon')"/>
      <input type="button" value="Präposition" v-bind:class="selectedWordArt(currentWord, 'präposition')"/>
    </div>
    <div @click="gotoWord('prev')">&lt;&mdash;</div>
    <div @click="gotoWord('next')">&mdash;&gt;</div>
    <textarea v-model="wordsList"></textarea>
  </div>
  
</template>

<script>
export default {
  name: 'MainComponent',
  props: {
    words: {
      type: Array
    },
    currentWord: {
      type: String
    }
  },
  created() {
    // eslint-disable-next-line
    console.log("We're in the component");
    this.currentWordOfModel = this.currentWord == undefined ? this.words[0] : this.currentWord;
    var wordData = "";

    this.words.forEach(element => {
      wordData += element + "\n"
      this.wordsModel[element] = element == 'schatz' ? {'wordart': 'substantiv'} : {'wordart': 'verb'}
    });
    this.wordsList = wordData;
  },
  data: function() {
    return {
      wordsList: "",
      currentWordOfModel: null,
      wordsModel: {}
    }
  },
  computed: {    
  },  
  methods: {
    selectedWordArt: function(selectedWord, wordart) {
      
      return {'selected': this.wordsModel[selectedWord]['wordart'] == wordart};
    },
    'gotoWord': function(direction) {
      var word = null;
      var wordCount = this.words.length;

      var currentIndex = this.words.indexOf(this.currentWord);
      
      if (currentIndex == -1) {
        return;
      }

      if (direction == 'next') {
        if (currentIndex >= wordCount - 1) {
          return;
        }
        word = this.words[currentIndex + 1];
      } else {
        if (currentIndex <= 0) {
          return;
        }
        word = this.words[currentIndex - 1];
      }
      this.currentWordOfModel = word;
      this.$router.push({ name: 'word-edit', params: { word: word }})
    }
  }  
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
input.selected {
  font-size: 18pt;
  color:red;
}
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
