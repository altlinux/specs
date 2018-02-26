%define dist File-Listing
Name: perl-%dist
Version: 6.04
Release: alt1

Summary: Parse directory listing
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

Conflicts: perl-libwww < 6

BuildArch: noarch

# Automatically added by buildreq on Mon Feb 20 2012
BuildRequires: perl-HTTP-Date perl-devel

%description
This module exports a single function called parse_dir(), which can be
used to parse directory listings.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/File

%changelog
* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 6.04-alt1
- 6.03 -> 6.04

* Mon Nov 14 2011 Alexey Tourbin <at@altlinux.ru> 6.03-alt2
- rebuilt as plain src.rpm

* Wed Sep 21 2011 Alexey Tourbin <at@altlinux.ru> 6.03-alt1
- 6.02 -> 6.03

* Mon Mar 21 2011 Alexey Tourbin <at@altlinux.ru> 6.02-alt1
- initial revision
