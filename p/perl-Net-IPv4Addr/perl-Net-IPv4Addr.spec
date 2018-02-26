%define module Net-IPv4Addr

Name: perl-%module
Version: 0.10
Release: alt2
Epoch: 1

Summary: Perl modules to manipulates Ipv4 addresses
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Net/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Mon Dec 13 2010
BuildRequires: perl-devel perl-podlators

%description
Net::IPv4Addr provides methods for parsing IPv4 addresses both in traditional
address/netmask format and in the new CIDR format.  There are also methods
for calculating the network and broadcast address and also to see check if a
given address is in a specific network.

%prep
%setup -n %module-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%_bindir/*
%_man1dir/*
%perl_vendor_privlib/Net/
%perl_vendor_privlib/auto/*

%changelog
* Mon Dec 13 2010 Victor Forsiuk <force@altlinux.org> 1:0.10-alt2
- Rebuild without man3 pages (fixes build with our perl 5.12).

* Tue Jul 31 2007 Victor Forsyuk <force@altlinux.org> 1:0.10-alt1
- Spec cleanups.

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.10-ipl5mdk.1
- Rebuilt with rpm-build-perl-0.5.1.

* Wed Nov 06 2002 Stanislav Ievlev <inger@altlinux.ru> 0.10-ipl5mdk
- rebuild with new perl

* Mon Jul 23 2001 Stanislav Ievlev <inger@altlinux.ru> 0.10-ipl4mdk
- Rebuilt with new perl again

* Mon Jun 25 2001 Konstantin Volckov <goldhead@altlinux.ru> 0.10-ipl3mdk
- Rebuilt with perl-5.6.1
- Some spec cleanup

* Wed Jan 17 2001 AEN <aen@logic.ru>
- RE adaptation

* Wed Oct 18 2000  Florin Grad <florin@mandrakesoft.com> 0.10-1mdk
- mandrake adaptations

* Tue Aug 01 2000  Francis J. Lacoste <francis.lacoste@iNsu.COM>
  [0.10-1i]
- Updated to version 0.10.
- Updated spec file to use new macros.

* Wed May 03 2000  Francis J. Lacoste <francis.lacoste@iNsu.COM>
  [0.09-1i]
- Updated to version 0.09.
- Updated automatic file list generation.
- Changed group.

* Wed Dec 15 1999  Francis J. Lacoste <francis.lacoste@iNsu.COM>
  [0.08-1i]
- Updated to version 0.08.
- Added perl(Net::IPv4Addr) to list of Provides.
- Fixed Source URL.

* Tue Oct 19 1999  Francis J. Lacoste <francis.lacoste@iNsu.COM>
  [0.07-1i]
- Updated to version 0.07

* Tue Oct 19 1999  Francis J. Lacoste <francis.lacoste@iNsu.COM>
  [0.06-1i]
- Updated to version 0.06.
- Renamed package to Net-IPv4Addr.

* Wed Sep 15 1999  Francis J. Lacoste <francis.lacoste@iNsu.COM>
  [0.05-1i]
- Updated to version 0.05.

* Sun Aug 15 1999  Francis J. Lacoste <francis.lacoste@iNsu.COM>
  [0.04-1i]
- Updated to version 0.04.

* Mon Jul 05 1999  Francis J. Lacoste <francis.lacoste@iNsu.COM>
  [0.03-1i]
- Updated to version 0.03.

* Sat May 15 1999  Francis J. Lacoste <francis@iNsu.COM>
  [0.02-2i]
- Updated to version 0.02.

* Sat May 15 1999  Francis J. Lacoste <francis@iNsu.COM>
  [0.01-1i]
- First RPM release.

