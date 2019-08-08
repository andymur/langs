<template>
  <div class="home">
    <main-component :words="words" :currentWord="currentWord" v-on:pos-change="posChange"/>
    <pre>
        {{words}}
    </pre>
  </div>
</template>

<script>

    /*
        [
            {
                originalWord: 'verstehe',
                normalizedWord: 'verstehen',
                pos: 'verb',
            },
            {
                originalWord: 'strand'
                normalizedWord: 'strand',
                pos: 'verb',
                gender: 'male'
            },...
        ]
    */

    import Main from '@/components/MainComponent.vue'
    
    export default {
        name: "home",
        components: {
            'main-component': Main
        },        
        methods: {
            posChange: function(obj) {
                // eslint-disable-next-line
                console.log(obj);
                this.words.forEach(
                    word => {
                        if (word['originalWord'] == obj['word']) {
                            word['pos'] = obj['pos']
                        }
                    }
                )
            }
        },
        data: function () {
            return {
                words: [
                        {
                            originalWord: "auswahlen",
                            normalizedWord: "auswahlen",
                            pos: null
                        },
                        {
                            originalWord: "verstehen",
                            normalizedWord: "verstehen",
                            pos: null
                        },
                        {
                            originalWord: "ausgeben",
                            normalizedWord: "ausgeben",
                            pos: null
                        },
                        {
                            originalWord: "schatz",
                            normalizedWord: "schatz",
                            pos: null
                        }
                ],
                currentWord: null
            }
        },
        created: function() {
            // eslint-disable-next-line
            console.log("Hey there...");
            this.currentWord = this.words[0]['originalWord']
        },
    }
</script>