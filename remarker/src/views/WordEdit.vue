<template>
    <div>
        <pre>
            {{ $route.params.word }}
        </pre>
        <main-component :words="words" :currentWord="$route.params.word" v-on:pos-change="posChange"/>
         <pre>
            {{words}}
        </pre>
    </div>
</template>

<script>
    import Main from '@/components/MainComponent.vue'

    export default {
        name: "word-edit",
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
            console.log("Hey there...we're goint to edit something");
        },
    }
</script>
