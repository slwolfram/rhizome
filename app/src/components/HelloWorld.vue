<template>
    <div>
        <div class="hello" style=" display: none; ">
            <h1>{{ msg }}</h1>
            <p>
            For a guide and recipes on how to configure / customize this project,<br />
            check out the
            <a href="https://cli.vuejs.org" target="_blank" rel="noopener"
                >vue-cli documentation</a
            >.
            </p>
            <h3>Installed CLI Plugins</h3>
            <ul>
            <li>
                <a
                href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-babel"
                target="_blank"
                rel="noopener"
                >babel</a
                    >
                </li>
                <li>
                    <a
                    href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-router"
                    target="_blank"
                    rel="noopener"
                    >router</a
                    >
                </li>
                <li>
                    <a
                    href="https://github.com/vuejs/vue-cli/tree/dev/packages/%40vue/cli-plugin-eslint"
                    target="_blank"
                    rel="noopener"
                    >eslint</a
                    >
                </li>
                </ul>
                <h3>Essential Links</h3>
                <ul>
                <li>
                    <a href="https://vuejs.org" target="_blank" rel="noopener">Core Docs</a>
                </li>
                <li>
                    <a href="https://forum.vuejs.org" target="_blank" rel="noopener"
                    >Forum</a
                    >
                </li>
                <li>
                    <a href="https://chat.vuejs.org" target="_blank" rel="noopener"
                    >Community Chat</a
                    >
                </li>
                <li>
                    <a href="https://twitter.com/vuejs" target="_blank" rel="noopener"
                    >Twitter</a
                    >
                </li>
                <li>
                    <a href="https://news.vuejs.org" target="_blank" rel="noopener">News</a>
                </li>
                </ul>
                <h3>Ecosystem</h3>
                <ul>
                <li>
                    <a href="https://router.vuejs.org" target="_blank" rel="noopener"
                    >vue-router</a
                    >
                </li>
                <li>
                    <a href="https://vuex.vuejs.org" target="_blank" rel="noopener">vuex</a>
                </li>
                <li>
                    <a
                    href="https://github.com/vuejs/vue-devtools#vue-devtools"
                    target="_blank"
                    rel="noopener"
                    >vue-devtools</a
                    >
                </li>
                <li>
                    <a href="https://vue-loader.vuejs.org" target="_blank" rel="noopener"
                    >vue-loader</a
                    >
                </li>
                <li>
                    <a
                    href="https://github.com/vuejs/awesome-vue"
                    target="_blank"
                    rel="noopener"
                    >awesome-vue</a
                    >
                </li>
                </ul>
            </div>
    <table class="table">
        <thead>
            <tr>
                <th v-for="(column, index) in fields" :key="index"> {{column}}</th>
            </tr>
        </thead>
        <tbody>
            <tr v-for="(item, index) in roots" :key="index">
                <td v-for="(column, indexColumn) in fields" :key="indexColumn">{{item[column]}}</td>
            </tr>
        </tbody>
    </table>

    </div>
    <div>
        <form id="form-id">
            <label for="filename">File name:</label><br>
            <input type="text" id="filename" name="filename"><br>
            <label for="description">Description:</label><br>
            <input type="text" id="description" name="description"><br>
        </form>
    </div>
</template>

<script>
import RootService from '@/services/RootService';

export default {
    name: "HelloWorld",

    props: {
        msg: String
    },

    data () {
        return {
            loading: true,
            roots: [],
            fields: []
        }
    },

    created () {
        RootService.getRoots(0)
                   .then(roots => {
                       console.log('roots here');
                       this.roots = roots;
                       console.log(roots[0].root_id);
                       this.fields = Object.keys(roots[0]);
                   })
                   .catch(error => console.log(error))
                   .finally(() => {
                       this.loading = false
                   });
    }
};


</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="scss">
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
