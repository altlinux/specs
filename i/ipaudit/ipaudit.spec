Name: ipaudit
Version: 1.0
Release: alt1rc9
Copyright: GPL
Group: Monitoring
Source: %{name}-%{version}rc9.tar.gz
Patch: ipaudit-errno.patch
Summary: IPAudit monitors network activity on a network by host, protocol and port.
Packager: Ilya Mashkin <oddity@altlinux.ru>
Url: http://ipaudit.sourceforge.net/
BuildRoot: /var/tmp/%{name}-%{version}-root
BuildRequires: libpcap-devel


%description
IPAUDIT listens to a network device in promiscuis mode, and records
of every 'connection', each conversation between two ip addresses.  A unique
connection is determined by the ip addresses of the two machines, the
protocol used between them and the port numbers (if they are communicating
via udp or tcp).

It uses a hash table to keep track of the number of bytes and packets
in both directions.  When IPAUDIT receives a signal SIGTERM (kill)
or SIGINT (kill -2, usually the same as a Control-C), it stops collecting
data and write the tabulated results.
  
%prep
%setup -q -n %{name}-%{version}rc9
#patch -p 1

%build
./configure --prefix=/usr
%make_build
# all

%install
make install DESTDIR=%buildroot

#mkdir %buildroot/usr/share/man
#mkdir %buildroot%_man1dir
#mkdir %buildroot%_man8dir

%__install -pD -m444 %buildroot/usr/man/man1/total.1 %buildroot%_man1dir/total.1
#rmdir %buildroot/usr/man/man1/
%__install -pD -m444 %buildroot/usr/man/man8/%name.8 %buildroot%_man8dir/%name.8
%__install -pD -m444 %buildroot/usr/man/man8/ipstrings.8 %buildroot%_man8dir/ipstrings.8
#rmdir %buildroot/usr/man/man8/

%files
%doc README
%_bindir/*
%_sbindir/*
%_man1dir/*
%_man8dir/*


%changelog
* Thu Sep 30 2010 Ilya Mashkin <oddity@altlinux.ru> 1.0-alt1rc9
- 1.0rc9
- spec cleanup
- add summary, add url

* Wed May 05 2004 Andrey Orlov <cray@altlinux.ru> 0.95-alt5
- Clause "Include <errno.h>" added into suorce;

* Thu Mar 11 2004 Andrey Orlov <cray@altlinux.ru> 0.95-alt4
- Rebuild with new libpcap

* Thu Oct 09 2003 Andrey Orlov <cray@altlinux.ru> 0.95-alt3
- Fix FHS-2.2 violence

* Tue Oct 07 2003 Andrey Orlov <cray@altlinux.ru> 0.95-alt2
- Fix build requires (libpcap-devel);

* Fri Nov  1 2002 Andrey Orlov <cray@altlinux.ru> 0.95-alt1

Jan 19, 2001
-  ipaudit:  corrected for packet double count / double write
               when packets travels between two monitored interfaces.
             added -M option to turn off correction for multiple
             devices.

Jan 2, 2001
-  ipaudit:  added config file option

Dec 21, 2000
-  ipaudit:  added multiple interface read - "ipaudit eth0:eth1"
             Use of select() to implement multiple reads
             fixes exit problem in a different way from yesterday.

Dec 20, 2000
-  ipaudit: fixed ihandler() to exit cleanly (no more core dumps?) by
   using fcntl() to set interface file descriptor to O_NONBLOCK
-  ipstrings: fixed handling of DLT_NULL packet type (needed to
   at 'PacketOffset' to 'caplen'

Dec 10, 2000
-  ipaudit: expand '-l' (local) option to allow more flexible ip ranges.
-  ipstrings:  add '-z' (size) to print ip packet size.

Oct 17, 2000
-  ipaudit: add 'C' option to preserve icmp packet type/code bytes
   in printed source port field.
-  ipaudit: add 'I' option to dump all traffic from a single IP address.
-  ipaudit: separate ipaudit distribution into ipaudit-bin (just C code)
   and a future ipaudit-web (cron and cgi scripts).  Currently
   cron and cgi scripts available in ipaudit-0.93b3.tgz

Sep 29, 2000
-  fixed long standing problem when writing ICMP packets (-w);
   first 4 bytes of ICMP header were mistakenly zeroed.

Sep 19, 2000
-  total.c - added -d, -v, -N options

Aug 23, 2000
-  changed from gif to png (thanx andyz)

Aug 21, 2000
- ipaudit.c: cleaned up Usage message
- ipaudit.c: added -S option to print ip addresses in short format
- Removed dependence upon GNU date in all scripts.  Perl scripts use
    &Date() subroutine, shell scripts call new pdate.c.

Aug 14, 2000
- removed from cronclean bash specific construct:  ${HTML_DAY:-${DEF_HTML_DAY}}

ipaudit 0.93b3
July 25, 2000
- re-organized distribution
- added scripts for generating web site displaying ipaudit statistics

ipauidt 0.92
Jun 20, 2000
- print ethernet packets with -e option
- prevent memory overflow due to packet storms with -L option
- sort output by ip address or intial connection time if -t option.
- include total.c, ipstrings.c utilies in distribution, and
     assorted perl scripts - dnslist, ipf, icf (total utility replaces collate)
- fix reading of some devices such as ppp (add correct offset to ip packet structure)
- use separate structures for ip and eth packet cracking.
- hopefully removed code which made BSD OS not compile.
- Packet length no longer includes ethernet header
- correctly take into account ip header length (option field)
- debug option also prints version info, for easier debug reports


ipaudit 0.91.2
Feb 1, 2000
   - added -m option by request (to switch off promisc mode)
   - try 'call pcap_close()' from ihandler(), see if it helps signal
     trouble
Jan 24, 2000
   - added collate utility
ipaudit 0.91.1
Jan 19, 2000
   - Fixed -p option, was not reading udp port options correctly
     (thanks James Stephens)

ipaudit 0.91
Jan 7, 2000
   - Fix -c option in getopt() (thanks Bob Maccione)
   - Add -t option to list opening and closing connection time
         (suggested by Aivo Kalu)
   - Add -b option to write output in binary format (experimental)
   - Add -d option to switch on debugging output

ipaudit 0.9
Nov 18, 1999
   Initial Release
