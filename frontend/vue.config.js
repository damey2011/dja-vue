const ASSET_DIR = "static";
const FaviconsWebpackPlugin = require("favicons-webpack-plugin");

module.exports = {
  assetsDir: ASSET_DIR,
  configureWebpack: {
    plugins: [
      new FaviconsWebpackPlugin({
        logo: "./src/assets/favicon.png",
        prefix: ASSET_DIR + "/favicons"
      })
    ]
  }
};
