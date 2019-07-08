const webpack = require('webpack');
const path = require('path');
const src = path.resolve(__dirname, 'src');
const build = path.resolve(__dirname, 'build');
const port = 8000;

module.exports = {
    mode: 'production',
    entry:[
        'webpack/hot/only-dev-server',
        `webpack-dev-server/client?http://127.0.0.1:${port}`,
        path.resolve(src, 'index.js')
    ],
    output: {
    path: build,
    filename: 'bundle.js'
        },
    module: {
        rules: [
            {
                test: /\.(png|jpg|gif|svg|woff|woff2|ttf|eot|ico)$/,
                use: {
                    loader: 'file-loader',
                }
            },
            {
                test: /\.js|.jsx$/,
                exclude: /node_modules/,
                use: {
                    loader: 'babel-loader',
                }
            },
            {
                test: /\.css$/,
                use:[
                    {loader: "style-loader"},
                    {loader: "css-loader"}
                ]
            }
        ]
    },
    plugins: [
        new webpack.HotModuleReplacementPlugin(),
    ],
    devServer: {
        hot: true,
        contentBase: build,
        compress: true,
        port
    }
};