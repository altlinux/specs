%define dist ExtUtils-Depends
Name: perl-%dist
Version: 0.304
Release: alt2

Summary: Perl module for building XS extensions easily
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 05 2011
BuildRequires: perl-devel

%description
This module tries to make it easy to build Perl extensions that use
functions and typemaps provided by other perl extensions. This means
that a perl extension is treated like a shared library that provides
also a C and an XS interface besides the perl one.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/ExtUtils

%changelog
* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 0.304-alt2
- rebuilt as plain src.rpm

* Fri Sep 23 2011 Igor Vlasenko <viy@altlinux.ru> 0.304-alt1
- automated CPAN update

* Tue Jul 06 2010 Alexey Tourbin <at@altlinux.ru> 0.302-alt1
- 0.301 -> 0.302

* Sat Sep 27 2008 Alexey Tourbin <at@altlinux.ru> 0.301-alt1
- 0.205 -> 0.301

* Wed Nov 14 2007 Alexey Tourbin <at@altlinux.ru> 0.205-alt2
- removed manual pages

* Wed Nov 14 2007 Alexey Tourbin <at@altlinux.ru> 0.205-alt1
- 0.204 -> 0.205

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.204-alt1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Wed Oct 06 2004 Alexey Tourbin <at@altlinux.ru> 0.204-alt1
- 0.202 -> 0.204

* Sat May 15 2004 Alexey Tourbin <at@altlinux.ru> 0.202-alt1
- 0.201 -> 0.202

* Wed Feb 18 2004 Alexey Tourbin <at@altlinux.ru> 0.201-alt1
- 0.201

* Sun Nov 30 2003 Alexey Tourbin <at@altlinux.ru> 0.104-alt1
- 0.104

* Thu Aug 28 2003 Alexey Tourbin <at@altlinux.ru> 0.103-alt1
- initial revision
