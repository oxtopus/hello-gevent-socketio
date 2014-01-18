// Connect to example namespace on localhost, port 5000
var example = io.connect("http://localhost:5000/example", 5000)

// Define handler for "response" event emitted by the server
example.on("response", function (data) { document.writeln(data.msg) })

// Emit "challenge" event, to be handled by server
example.emit("challenge", {msg: "Hello, world!"})
