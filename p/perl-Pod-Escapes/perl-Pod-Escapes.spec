%define dist Pod-Escapes
Name: perl-%dist
Version: 1.04
Release: alt4

Summary: Perl module for resolving Pod escape sequences
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Sun Nov 13 2011
BuildRequires: perl-devel

%description
This module provides things that are useful in decoding Pod E<...>
sequences.  It is used by Pod parsers and formatters.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/Pod

%changelog
* Sun Nov 13 2011 Alexey Tourbin <at@altlinux.ru> 1.04-alt4
- rebuilt

* Wed Jul 29 2009 Alexey Tourbin <at@altlinux.ru> 1.04-alt3
- rebuilt

* Tue Dec 28 2004 Alexey Tourbin <at@altlinux.ru> 1.04-alt2
- rebuild in new environment
- manual pages not packaged (use perldoc)

* Sat May 08 2004 Alexey Tourbin <at@altlinux.ru> 1.04-alt1
- 1.03 -> 1.04

* Tue Oct 07 2003 Alexey Tourbin <at@altlinux.ru> 1.03-alt1
- initial revision
