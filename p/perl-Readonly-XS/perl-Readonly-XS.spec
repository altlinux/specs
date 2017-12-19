%def_without bootstrap
%add_findreq_skiplist %perl_vendor_archlib/Readonly/XS.pm
%define dist Readonly-XS

Name: perl-%dist
Version: 1.05
Release: alt6

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Companion module for perl-Readonly
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/modules/by-module/Readonly/%dist-%version.tar.gz

BuildRequires: perl-devel
%if_without bootstrap
BuildRequires: perl-Readonly
Requires: perl-Readonly
%endif

%description
Readonly::XS is a companion module for Readonly, to speed up read-only
scalar variables.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Readonly
%perl_vendor_autolib/Readonly

%changelog
* Tue Dec 19 2017 Igor Vlasenko <viy@altlinux.ru> 1.05-alt6
- unbootstrap

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.05-alt5.3.1.1.1
- rebuild with new perl 5.26.1

* Sun Feb 12 2017 Igor Vlasenko <viy@altlinux.ru> 1.05-alt5.3.1.1
- unbootstrap after rebuild with new perl 5.24.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.05-alt5.3.1
- rebuild with new perl 5.24.1

* Sat Nov 28 2015 Igor Vlasenko <viy@altlinux.ru> 1.05-alt5.3
- unbootstrap

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.05-alt5.2.1
- rebuild with new perl 5.22.0

* Sat Dec 13 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt5.2
- unbootstrap

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt5.1
- rebuild with new perl 5.20.1

* Wed Dec 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt5
- added %if_with bootstrap

* Wed Apr 02 2014 Igor Vlasenko <viy@altlinux.ru> 1.05-alt4
- fixed build

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.05-alt3
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 1.05-alt2
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.05-alt1.2
- rebuilt for perl-5.14
- disabled dependency on perl-Readonly

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.05-alt1.1
- rebuilt with perl 5.12

* Mon Jul 13 2009 Victor Forsyuk <force@altlinux.org> 1.05-alt1
- 1.05

* Wed Jul 11 2007 Victor Forsyuk <force@altlinux.org> 1.04-alt1
- Initial build.
