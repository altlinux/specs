%define _unpackaged_files_terminate_build 1
%define dist DateTime-Format-W3CDTF
Name: perl-%dist
Version: 0.07
Release: alt1

Summary: Parse and format W3CDTF datetime strings
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/G/GW/GWILLIAMS/%{dist}-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-DateTime perl-Test-Pod perl-Test-Pod-Coverage

%description
This module understands the W3CDTF date/time format, an ISO 8601 profile,
defined at http://www.w3.org/TR/NOTE-datetime. This format as the native
date format of RSS 1.0.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_privlib/DateTime

%changelog
* Tue May 09 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.06-alt2
- disabled build dependency on perl-Module-Install

* Sun Apr 24 2011 Alexey Tourbin <at@altlinux.ru> 0.06-alt1
- 0.05 -> 0.06

* Tue Feb 16 2010 Alexey Tourbin <at@altlinux.ru> 0.05-alt1
- 0.04 -> 0.05

* Sun Aug 21 2005 Alexey Tourbin <at@altlinux.ru> 0.04-alt1
- initial revision (for XML::Feed)
