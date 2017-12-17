%define _unpackaged_files_terminate_build 1
%define dist Cairo
Name: perl-%dist
Version: 1.106
Release: alt1.1.1.1

Summary: Perl interface to the cairo vector graphics library
License: LGPL
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/X/XA/XAOC/Cairo-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: fonts-ttf-dejavu libcairo-devel perl-ExtUtils-Depends perl-ExtUtils-PkgConfig perl-devel

%package devel
Summary: Perl interface to the cairo vector graphics library
Group: Development/Perl
Requires: %name = %version-%release
Requires: libcairo-devel

%description
Cairo provides Perl bindings for the vector graphics library cairo.
It supports multiple output targets, including PNG, PDF and SVG.
Cairo produces identical output on all those targets.

%description devel
Cairo provides Perl bindings for the vector graphics library cairo.
It supports multiple output targets, including PNG, PDF and SVG.
Cairo produces identical output on all those targets.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc NEWS README
%perl_vendor_archlib/Cairo.pm
%perl_vendor_autolib/Cairo

%files devel
%dir %perl_vendor_archlib/Cairo
%perl_vendor_archlib/Cairo/Install

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.106-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.106-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.106-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.106-alt1
- automated CPAN update

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.105-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.104-alt1.1
- rebuild with new perl 5.20.1

* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 1.104-alt1
- automated CPAN update

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 1.103-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.103-alt1
- automated CPAN update

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 1.101-alt1
- 1.062 -> 1.101
- built for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.062-alt2
- rebuilt for perl-5.14

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 1.062-alt1
- 1.061 -> 1.062
- rebuilt as plain src.rpm

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.061-alt1.1
- rebuilt with perl 5.12
- disabled a failing test for a while

* Thu Apr 02 2009 Alexey Tourbin <at@altlinux.ru> 1.061-alt1
- 1.060 -> 1.061

* Mon Sep 29 2008 Alexey Tourbin <at@altlinux.ru> 1.060-alt1
- 1.023 -> 1.060

* Fri Dec 14 2007 Dmitry V. Levin <ldv@altlinux.org> 1.023-alt1.M40.1
- Replaced fonts-ttf-ms with fonts-ttf-dejavu in BuildRequires.

* Sun Feb 25 2007 Alexey Tourbin <at@altlinux.ru> 1.023-alt1
- 1.02 -> 1.023

* Tue Nov 14 2006 Alexey Tourbin <at@altlinux.ru> 1.02-alt1
- 1.00 -> 1.02

* Mon Sep 04 2006 Alexey Tourbin <at@altlinux.ru> 1.00-alt1
- 0.92 -> 1.00

* Sat Aug 26 2006 Alexey Tourbin <at@altlinux.ru> 0.92-alt1
- 0.91 -> 0.92

* Tue Aug 15 2006 Alexey Tourbin <at@altlinux.ru> 0.91-alt1
- initial revision
- fix for POPpx SEGV
