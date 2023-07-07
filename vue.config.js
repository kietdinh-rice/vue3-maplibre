module.exports = {
  publicPath: process.env.NODE_ENV === 'production'
    ? './'
    : '/',
  pages: {
    index: {
      // entry for the page
      entry: 'src/main.js',
      title: 'Maptiler MapLibre',
    },
  },
  configureWebpack: {
    module: {
      rules: [
        {
          test: /\.geojson$/,
          loader: 'json-loader'
        }
      ]
    }
  }
}