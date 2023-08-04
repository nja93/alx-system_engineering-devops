#!/usr/bin/env ruby
# This script matched "hbt with 2 to 5 ts" and ending with "n".

puts ARGV[0].scan(/hbt{2,5}n/).join
