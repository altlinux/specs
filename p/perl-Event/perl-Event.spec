%define _unpackaged_files_terminate_build 1
%define dist Event

Name: perl-%dist
Version: 1.26
Release: alt1.1.1

Summary: Event loop processing
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/E/ET/ETJ/Event-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
The Event module provide a central facility to watch for various types
of events and invoke a callback when these events occur. The idea is to
delay the handling of events so that they may be dispatched in priority
order when it is safe for callbacks to execute.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Event*
%perl_vendor_autolib/Event

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.26-alt1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.26-alt1.1
- rebuild with new perl 5.24.1

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.26-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1.1
- rebuild with new perl 5.22.0

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1.1
- rebuild with new perl 5.20.1

* Fri Jul 25 2014 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1
- automated CPAN update

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.21-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.21-alt1
- automated CPAN update

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 1.20-alt3
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.20-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1
- automated CPAN update

* Sun Jul 17 2011 Victor Forsiuk <force@altlinux.org> 1.18-alt1
- 1.18

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.13-alt1.1
- rebuilt with perl 5.12

* Mon Jun 21 2010 Victor Forsiuk <force@altlinux.org> 1.13-alt1
- 1.13

* Wed Jun 25 2008 Victor Forsyuk <force@altlinux.org> 1.11-alt1
- 1.11

* Wed Jun 06 2007 Victor Forsyuk <force@altlinux.org> 1.09-alt1
- 1.09

* Sat Jan 20 2007 Victor Forsyuk <force@altlinux.org> 1.08-alt1
- 1.08
- Package man pages.

* Mon Aug 07 2006 Alexey Tourbin <at@altlinux.ru> 1.06-alt1
- 1.02 -> 1.06

* Thu Dec 23 2004 Alexey Tourbin <at@altlinux.ru> 1.02-alt1
- NMU: 0.87 -> 1.02 (#5604)
- deparse.patch not needed due to rpm-build-perl enhancements
- manual pages not packaged (use perldoc)
- specfile cleanup

* Sun Oct 26 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.87-alt2
- deparse patch by at@.

* Thu Feb 27 2003 Yuri N. Sedunov <aris@altlinux.ru> 0.87-alt1
- First build for Sisyphus.
