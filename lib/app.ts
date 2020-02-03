const lib = require('./hello.node') as {
    hello(): string
}

console.info(lib.hello());