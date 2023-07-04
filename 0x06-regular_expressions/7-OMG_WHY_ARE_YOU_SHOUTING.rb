#!/usr/bin/env ruby
# rUBY script that only prints matching capital letters
puts ARGV[0].scan(/[A-Z]/).join
