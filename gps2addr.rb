#!/usr/bin/ruby
#gps2addr
#by Behdad Ahmadi
#Twitter: behdadahmadi
#https://logicalcoders.com

require 'net/http'
def usage()
  puts 'Usage: gps2addr.rb LAT LON'
end

def banner()
  dotname = '-' * 14
  puts ' '
  puts dotname.center(20,'-')
  puts ('.::' + 'gps2addr' + '::.').center(20,' ')
  puts 'by Behdad Ahmadi'.center(20)
  puts 'Twitter:behdadahmadi'.center(16)
  puts dotname.center(20,'-')
end

def main()
    banner()
    lat = ARGV[0]
    lon = ARGV[1]
    if lon == NIL or lat == NIL
      usage()
      abort('No given data')
    end

    uri = URI('http://cellphonetrackers.org/gsm/gps-coordinate.php')
    payload = {'a' => 'a','lat'=>lat,'lon'=>lon,'addr'=>''}
    res = Net::HTTP.post_form(uri,payload)
    m = /q=.*(&)/.match(res.body)
    m =  m[0].sub('q=','')
    puts m.split('&')[0]

end
main()

