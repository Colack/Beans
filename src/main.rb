#!/usr/bin/env ruby

require 'optparse'
require 'ostruct'
require 'pp'

# Beans keywords:
# - header : Print bold
# - print : Print
# - error : Print red
# - warning : Print yellow
# - info : Print green
# - debug : Print blue
# - wait : Sleep for X * 1000 milliseconds
# - exit : Exit with code
# - run : Run command ( Specify the command in the value )
# - run! : Run command and exit if failed ( Specify the command in the value )

class Beans
  def initialize
    @options = OpenStruct.new
    @options.verbose = false
  end

  def parse(args)
    opts = OptionParser.new do |opts|
      opts.banner = "Usage: main.rb [options]"

      opts.separator ""
      opts.separator "Specific options:"

      opts.on("-v", "--[no-]verbose", "Run verbosely") do |v|
        @options.verbose = v
      end

      opts.on("-h", "--help", "Show this message") do
        puts opts
        exit
      end
    end

    opts.parse!(args)
  end

  def run
    while line = gets
        line = line.chomp
        if line.start_with?("#")
            next
        end
    
        if line.start_with?("header")
            puts "\033[1m#{line[7..-1]}\033[0m"
        elsif line.start_with?("print")
            puts line[6..-1]
        elsif line.start_with?("error")
            puts "\033[31m#{line[6..-1]}\033[0m"
        elsif line.start_with?("warning")
            puts "\033[33m#{line[8..-1]}\033[0m"
        elsif line.start_with?("info")
            puts "\033[32m#{line[5..-1]}\033[0m"
        elsif line.start_with?("debug")
            puts "\033[34m#{line[6..-1]}\033[0m"
        elsif line.start_with?("wait")
            sleep(line[5..-1].to_i / 1000.0)
        elsif line.start_with?("exit")
            exit(line[5..-1].to_i)
        elsif line.start_with?("run")
            system(line[4..-1])
        elsif line.start_with?("run!")
            system(line[5..-1])
            exit($?.exitstatus) unless $?.exitstatus == 0
        end
        end
  end
end

beans = Beans.new
beans.parse(ARGV)
beans.run