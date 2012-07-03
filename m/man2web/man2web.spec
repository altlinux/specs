Summary: Converts man pages to html
Name: man2web
Version: 0.88
Release: alt1
License: GPL
Group: Networking/WWW
Source: %name-%version.tar.gz
Source1: %name.conf
Packager: Fr. Br. George <george@altlinux.ru>
%define cgi /var/www/cgi-bin

%description
man2web is a program for converting man (manual) output to html on the fly (as
a CGI program) or on the command line.

Install man2web if you want to view man pages with your web browser.

%prep
%setup
#patch -p1 -b .buildroot

%build
autoreconf
# -O3 leads to some coredumps
CFLAGS=-O0 %configure --with-distro=debian-3 --with-manpath=/usr/local/man:%_mandir:/usr/X11R6/man:/usr/local/share/man --with-manpath-switch=-M 
%make

%install
%makeinstall
rm %buildroot%_sysconfdir/%name.conf.default
install %SOURCE1 %buildroot%_sysconfdir/

%files
%doc README TODO doc/README.RedHat doc/%name.conf.default
%_bindir/%name
%_man1dir/%name.1*
%_man5dir/%name.conf.5*
%config(noreplace) %_sysconfdir/%name.conf

%changelog
* Thu Dec 06 2007 Fr. Br. George <george@altlinux.ru> 0.88-alt1
- Initial build for ALT

* Thu Apr 26 2003 Jerry Talkington <jtalkington@users.sourceforge.net>
- added rpm
