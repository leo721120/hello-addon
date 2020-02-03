const lib = require('../out/hello') as {
    hello(): string
}

console.info(lib.hello());