#!/usr/bin/env ruby
# RUBY script that matches 10 digit number

puts ARGV[0].scan(/^\d{10}$/).join
