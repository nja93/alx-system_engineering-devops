#!/usr/bin/env ruby
# This is a ruby script that matches  hbt with "t" icrementing to t*5 ending with n
puts ARGV[0].scan(/hbt{2-4}n/).join
