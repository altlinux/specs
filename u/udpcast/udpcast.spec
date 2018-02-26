Name: udpcast
Version: 20110710
Release: alt1

Summary: UDP broadcast file distribution and installation
License: GPLv2+ and BSD
Group: Networking/Other

URL: http://udpcast.linux.lu/
Source: http://udpcast.linux.lu/download/%name-%version.tar.gz

# Automatically added by buildreq on Mon Apr 11 2011
BuildRequires: perl-Pod-Parser

%description
Allows easy installation of client machines via UDP broadcast.

%prep
%setup

# Don't pass -s (strip) option to ld
subst 's/LDFLAGS +=-s//' Makefile.in

%build
%configure
%make_build

%install
%makeinstall_std

%files
%_sbindir/udp-receiver
%_sbindir/udp-sender
%_man1dir/udp-receiver.1*
%_man1dir/udp-sender.1*
%doc cmd.html COPYING

%changelog
* Mon Aug 01 2011 Victor Forsiuk <force@altlinux.org> 20110710-alt1
- Version 20110710.

* Mon Apr 11 2011 Victor Forsiuk <force@altlinux.org> 20100130-alt1
- Version 20100130.

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 20060929-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jan 12 2007 Mikhail Pokidko <pma@altlinux.ru> 20060929-alt1
- Initial build
