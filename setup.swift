import Foundation
print("Installing and updating discord.py")
// install code, written by ma-ttp


@discardableResult
func shell(_ args: String...) -> Int32 {
    let task = Process()
    task.launchPath = "/bin/bash"
    task.arguments = args
    task.launch()
    shell("pip3 install discord.py")
    return task.terminationStatus
}

// Read the contents of the bot.py file
var fileURL = URL(fileURLWithPath: "bot.py")
var fileContents = try String(contentsOf: fileURL)

// Ask the user for the bot token
print("Please enter your bot token:")
let token = readLine(strippingNewline: true)

// Replace the placeholder token in the file contents with the user's token
fileContents = fileContents.replacingOccurrences(of: "token_is_here", with: token!)

// Write the modified contents back to the bot.py file
try fileContents.write(to: fileURL, atomically: true, encoding: .utf8)

print("Bot token added to bot.py!")
