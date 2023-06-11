#!/usr/bin/perl
#
# program name : tacf (text-type access counter for first Web page)
#
# function     : count the number of guest, rewrite "index.html" 
#                and send a dummy gif file.
#
# note         : this counter is made for mesh home page (first page) 
#                where CGI is available, but SSI is not.
#
# programmer   : makoto takenaka : takesoft@mxs.meshnet.or.jp
#
# copyright    : (C) 1996 by Takesoft
#
# version(date): version  1. 0(June 20, 1996)
#                version  1. 1(June 22, 1996)
#                         Change "GUEST_NUMBER" to "INSERT_COUNTER".
#
#(1) set constants.
#
   $html_file0 = "./kanemoto_.html";     # prototype html file
   $html_file  = "./kanemoto.html";      # output html file with guest number
   $count_file = "./counteng.txt";       # guest number file
   $gif_file   = "./trans.gif";       # dummy gif file
#
#(2) Increment $count.
#
         open(COUNT_FILE, "+< $count_file")
            || &error_mail("tacf: Unable to open $count_file");
#         flock(COUNT_FILE, 2);
         $count = <COUNT_FILE>;
         $count++;
         seek(COUNT_FILE, 0, 0);
         print COUNT_FILE $count;
#         flock(COUNT_FILE, 8);
         close(COUNT_FILE);
#
#(3) Copy $html_file0 to $html_file, but insert guest number.
#
   open(HTML_FILE, ">$html_file")
      ||&error_mail("tacf: Unable to open $html_file. ");
#   flock(HTML_FILE, 2);
   open(HTML_FILE0, "$html_file0")
      ||&error_mail("tacf: Unable to open $html_file0.");

#
   while(<HTML_FILE0>)
      {
#
#  If this line contains "INSERT_COUNTER", send guest number.
#
      if ( $_ =~ /INSERT_COUNTER/ )
         {
         print HTML_FILE $count, "\n";
         }
      else
         {
         print HTML_FILE $_;
         }
      }
#
#   flock(HTML_FILE, 8);
   close(HTML_FILE);
   close(HTML_FILE0);
#
#(4) send dummy gif file to browser.
#
   print "Content-type: image/gif\n\n";
#
   open(GIF_FILE, $gif_file)
      ||&error_mail("tacf: Unable to open $gif_file");
#
   while(read(GIF_FILE, $buf, 16384))
      {
      print $buf;
      }
   close(GIF_FILE);
#
sub error_mail
   {
   local($message) = @_;
#
#(sub routine) Send error mail.
#
#   If you want to use error mail, change mail address to yours
#   and uncomment(remove #) next four lines.
#
   open(MAIL, "|mail kanemoto@e.u-tokyo.ac.jp");
   print MAIL "Error Message from tcf.cgi of home page: \n";
   print MAIL "$message\n";
   close(MAIL);
#
#  stop this perl program.
#
   die;
   }
