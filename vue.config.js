const { defineConfig } = require('@vue/cli-service')

module.exports = defineConfig({
  transpileDependencies: true,
  devServer: {
    host: '210.70.85.133',
    port: 8080,
    allowedHosts: 'all'
  }
})