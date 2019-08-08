<template>
  <div>
    <div @click="gotoWord('prev')">&lt;&mdash;</div>
    <div @click="gotoWord('next')">&mdash;&gt;</div>
    <div id="word-editors">
      <input type="text" v-model="currentWordOfModel" />
      <input type="text" :value="currentWordOfModel" />
    </div>
    <div id="wortart-buttons">
      <input type="button" value="Substantiv" 
        id="substantiv"
        @click="selectWordArt($event)" 
        v-bind:class="selectedWordArt('substantiv')" />
      <input type="button" value="Verb" 
        id="verb"
        @click="selectWordArt($event)" 
        v-bind:class="selectedWordArt('verb')"/>
      <input type="button" value="Adjektiv" 
        id="adjektiv"
        @click="selectWordArt($event)" 
        v-bind:class="selectedWordArt('adjektiv')"/>
      <input type="button" value="Pronomenon" 
        id="pronomenon"
        @click="selectWordArt($event)" 
        v-bind:class="selectedWordArt('pronomenon')"/>
      <input type="button" value="Präposition" 
        id="praeposition"
        @click="selectWordArt($event)"  
        v-bind:class="selectedWordArt('praeposition')"/>
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
    console.log(this.words[0])
    this.currentWordOfModel = this.currentWord == undefined 
      ? this.words[0]['originalWord'] 
      : this.currentWord;
    
    var wordData = "";

    this.words.forEach(element => {
      wordData += element['originalWord'] + "\n"
      this.$set(this.wordsModel, element['originalWord'], {'wordart': element['pos']})
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
    selectedWordArt: function(wordart) {      
      return {'selected': this.wordsModel[this.currentWordOfModel]['wordart'] == wordart};
    },
    selectWordArt: function(event) {
      this.wordsModel[this.currentWordOfModel]['wordart'] = event.currentTarget.id;
      this.$emit('pos-change', {'word': this.currentWordOfModel, 'pos': event.currentTarget.id});
    },
    gotoWord: function(direction) {
      var word = null;
      var wordCount = this.words.length;

      //find a way...how to extract to the small specific method
      
      // method start
      var currentIndex = -1;

      for (var i = 0; i < wordCount; i++) {
        if (this.words[i]['originalWord'] == this.currentWord) {
          currentIndex = i;
          break;
        }
      }
      // method end
      //console.log('current word index: ' + currentIndex + ' ' + this.cu);
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
      this.currentWordOfModel = word['originalWord'];
      this.$router.push({ name: 'word-edit', params: { word: word['originalWord'] }})
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
