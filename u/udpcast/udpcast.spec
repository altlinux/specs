Name: udpcast
Version: 20110710
Release: alt2

Summary: UDP broadcast file distribution and installation
License: GPLv2+ and BSD
Group: Networking/Other

Url: http://udpcast.linux.lu/
Source: http://udpcast.linux.lu/download/%name-%version.tar.gz
Patch:  udpcast-fix-build.patch

# Automatically added by buildreq on Mon Apr 11 2011
BuildRequires: perl-Pod-Parser

%description
Allows easy installation of client machines via UDP broadcast.

%prep
%setup
%patch -p2

# Don't pass -s (strip) option to ld
sed -i 's/LDFLAGS +=-s//' Makefile.in

# -O6 is just as insane in 2019
sed -i 's/-O6/-O%_optlevel/' Makefile.in

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
* Fri Jun 21 2019 Michael Shigorin <mike@altlinux.org> 20110710-alt2
- Fix superfluous optimization level

* Wed Apr 10 2013 Andrey Cherepanov <cas@altlinux.org> 20110710-alt1.1
- Fix build

* Mon Aug 01 2011 Victor Forsiuk <force@altlinux.org> 20110710-alt1
- Version 20110710.

* Mon Apr 11 2011 Victor Forsiuk <force@altlinux.org> 20100130-alt1
- Version 20100130.

* Wed Nov 24 2010 Igor Vlasenko <viy@altlinux.ru> 20060929-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jan 12 2007 Mikhail Pokidko <pma@altlinux.ru> 20060929-alt1
- Initial build
