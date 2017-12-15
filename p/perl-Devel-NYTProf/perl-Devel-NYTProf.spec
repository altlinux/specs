%define _unpackaged_files_terminate_build 1
%define dist Devel-NYTProf
Name: perl-%dist
Version: 6.04
Release: alt1.1.1

Summary: Powerful fast feature-rich perl source code profiler
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/T/TI/TIMB/Devel-NYTProf-%{version}.tar.gz

# Automatically added by buildreq on Tue Oct 11 2011
BuildRequires: perl-JSON-Any perl-Moose perl-Test-Pod perl-Test-Pod-Coverage zlib-devel perl-Test-Differences perl(File/Which.pm)

%description
Devel::NYTProf is a powerful feature-rich perl source code profiler.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

rm -rv %buildroot%perl_vendor_archlib/Devel/auto

# disable dependency on Apache
%add_findreq_skiplist */Devel/NYTProf/Apache.pm

%files
%doc Changes README.md
%_bindir/nytprof*
%_bindir/flamegraph.pl
%_man1dir/nytpro*.1*
%perl_vendor_archlib/Devel
%perl_vendor_autolib/Devel

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 6.04-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 6.04-alt1.1
- rebuild with new perl 5.24.1

* Wed Nov 30 2016 Igor Vlasenko <viy@altlinux.ru> 6.04-alt1
- automated CPAN update

* Mon Mar 28 2016 Igor Vlasenko <viy@altlinux.ru> 6.03-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 6.02-alt1.1
- rebuild with new perl 5.22.0

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 6.02-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 5.06-alt1.1
- rebuild with new perl 5.20.1

* Mon Sep 30 2013 Igor Vlasenko <viy@altlinux.ru> 5.06-alt1
- automated CPAN update

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 5.05-alt1
- 4.09 -> 5.05

* Fri Sep 28 2012 Vladimir Lettiev <crux@altlinux.ru> 4.09-alt1
- 4.08 -> 4.09

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 4.08-alt1
- 4.06 -> 4.08
- built for perl-5.16

* Tue Oct 11 2011 Alexey Tourbin <at@altlinux.ru> 4.06-alt2
- rebuilt for perl-5.14
- disabled dependency on Apache

* Sat Dec 04 2010 Vladimir Lettiev <crux@altlinux.ru> 4.06-alt1
- New version 4.06

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 4.05-alt1.1
- rebuilt with perl 5.12

* Sun Sep 19 2010 Vladimir Lettiev <crux@altlinux.ru> 4.05-alt1
- New version 4.05

* Mon Aug 23 2010 Vladimir Lettiev <crux@altlinux.ru> 4.04-alt1
- initial build
