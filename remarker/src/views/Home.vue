<template>
  <div class="home">
    <main-component :words="words" :currentWord="currentWord"/>
  </div>
</template>

<script>
    import Main from '@/components/MainComponent.vue'
    
    export default {
        name: "home",
        components: {
            'main-component': Main
        },                
        data: function () {
            return {
                words: ["auswahlen", "verstehen", "ausgeben", "schatz"],
                currentWord: null
            }
        },
        created: function() {
            // eslint-disable-next-line
            console.log("Hey there...");
            this.currentWord = this.words[0]
        },
    }
</script>