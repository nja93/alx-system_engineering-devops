#!/usr/bin/env ruby
# This is a RUBY script accepts one argument and pass it to a regular expression

puts ARGV[0].scan(/School/).join
