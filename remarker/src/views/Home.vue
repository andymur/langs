<template>
  <div class="home">
    <main-component :words="words"/>
  </div>
</template>

<script>
    import Main from '@/components/MainComponent.vue'
    
    export default {
        name: "home",
        components: {
            'main-component': Main
        },        
        created: function() {
            // eslint-disable-next-line
            console.log("Hey there...");
        },
        data: function () {
            return {
                words: ["auswhalen", "verstehen", "ausgeben", "schatz"]
            }
        }
    }
</script>