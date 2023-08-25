# Install flask 2.1.0 from pip3
#  pip 3 is the package provide
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}
