puts "Initializing..."
area = gets
puts "Writing to " + area + "."
File.open("log.txt", "w") { |f| f.write "header Hello World!" }
puts "Finished!"
