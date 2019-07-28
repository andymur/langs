<template>
    <div>
        <pre>
            {{ $route.params.word }}
        </pre>
        <main-component :words="words" :currentWord="$route.params.word"/>
    </div>
</template>

<script>
    import Main from '@/components/MainComponent.vue'

    export default {
        name: "word-edit",
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
            console.log("Hey there...we're goint to edit something");
        },
    }
</script>
