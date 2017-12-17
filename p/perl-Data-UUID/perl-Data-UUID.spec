%define _unpackaged_files_terminate_build 1
%define dist Data-UUID
Name: perl-%dist
Version: 1.221
Release: alt1.1.1.1

Summary: Perl extension for generating Globally/Universally Unique Identifiers (GUIDs/UUIDs)
License: BSD
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RJ/RJBS/Data-UUID-%{version}.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Pod-Parser perl-devel perl-threads

%description
This module provides a framework for generating UUIDs (Universally Unique
Identifiers, also known as GUIDs (Globally Unique Identifiers). A UUID is
128 bits long, and is guaranteed to be different from all other UUIDs/GUIDs
generated until 3400 A.D. UUIDs were originally used in the Network Computing
System (NCS) and later in the Open Software Foundation's (OSF) Distributed
Computing Environment. Currently many different technologies rely on UUIDs to
provide unique identity for various software components, Microsoft COM/DCOM
for instance, uses GUIDs very extensively to uniquely identify classes,
applications and components across network-connected systems.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_archlib/Data
%perl_vendor_autolib/Data

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.221-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.221-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.221-alt1.1
- rebuild with new perl 5.22.0

* Fri Oct 16 2015 Igor Vlasenko <viy@altlinux.ru> 1.221-alt1
- automated CPAN update

* Fri Dec 19 2014 Igor Vlasenko <viy@altlinux.ru> 1.220-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.219-alt2.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.219-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.219-alt1
- automated CPAN update

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 1.218-alt1
- 1.217 -> 1.218
- built for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.217-alt1.2
- rebuilt with perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.217-alt1.1
- rebuilt with perl 5.12

* Sun Oct 10 2010 Nikolay A. Fetisov <naf@altlinux.ru> 1.217-alt1
- New version 1.217

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 1.149-alt1
- New version 1.149

* Mon Mar 26 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.148-alt1
- New version 1.148:
  - fix incorrect initialization of tick-tracking (rt #2481, rt #21486)
  - packaging improvements
  - Win32 compatibility/compilation improvements

* Sun Apr 23 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.14-alt1
- Initial build for ALT Linux

* Sun Apr 23 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.14-alt0
- New version 0.14

* Tue May 24 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.11-alt0.1
- Build for new perl-5.8.7

* Fri Mar 04 2005 Nikolay A. Fetisov <naf@altlinux.ru> 0.11-alt0
- Preparing for ALT Linux
- Removing man pages

* Tue Jan 18 2005 Nikolay A. Fetisov <naf@naf.net.ru> 0.11-naf1
- Initial build
