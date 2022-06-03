puts "Initializing..."
puts "Creating New File..."
out_file = File.new("main.beans", "w")
puts "Writing to File..."
out_file.puts("header I love beans!\nprint Beans is not markdown!")
puts "Closing File..."
out_file.close
puts "Done!"
