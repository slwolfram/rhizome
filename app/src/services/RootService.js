import axios from "axios";

export default {
  name: "RootService",

  getRoots(depth) {
    return axios.get('/roots')
      .then(response  => {
        console.log(response);
        console.log(depth);
        console.log('depth: ${depth}');
        return response.data;
      });
  }
};
