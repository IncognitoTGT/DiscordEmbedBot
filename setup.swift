import Foundation
print("Installing and updating discord.py")
// install code, written by ma-ttp
func shell(_ launchPath: String, _ arguments: [String]) -> String?
{
    let task = Process()
    task.launchPath = launchPath
    task.arguments = arguments

    let pipe = Pipe()
    task.standardOutput = pipe
    task.launch()

    let data = pipe.fileHandleForReading.readDataToEndOfFile()
    let output = String(data: data, encoding: String.Encoding.utf8)

    return output
    shell("pip3 install discord.py")
}
// Read the contents of the bot.py file
var fileURL = URL(fileURLWithPath: "bot.py")
var fileContents = try String(contentsOf: fileURL)

// Ask the user for the bot token
print("Please enter your bot token:")
let token = readLine(strippingNewline: true)

// Replace the placeholder token in the file contents with the user's token
fileContents = fileContents.replacingOccurrences(of: "token is here", with: token!)

// Write the modified contents back to the bot.py file
try fileContents.write(to: fileURL, atomically: true, encoding: .utf8)

print("Bot token added to bot.py!")
