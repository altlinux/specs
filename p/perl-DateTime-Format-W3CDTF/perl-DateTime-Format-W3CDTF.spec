%define dist DateTime-Format-W3CDTF
Name: perl-%dist
Version: 0.06
Release: alt2

Summary: Parse and format W3CDTF datetime strings
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-DateTime perl-Test-Pod perl-Test-Pod-Coverage

%description
This module understands the W3CDTF date/time format, an ISO 8601 profile,
defined at http://www.w3.org/TR/NOTE-datetime. This format as the native
date format of RSS 1.0.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/DateTime

%changelog
* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.06-alt2
- disabled build dependency on perl-Module-Install

* Sun Apr 24 2011 Alexey Tourbin <at@altlinux.ru> 0.06-alt1
- 0.05 -> 0.06

* Tue Feb 16 2010 Alexey Tourbin <at@altlinux.ru> 0.05-alt1
- 0.04 -> 0.05

* Sun Aug 21 2005 Alexey Tourbin <at@altlinux.ru> 0.04-alt1
- initial revision (for XML::Feed)
