%define _unpackaged_files_terminate_build 1
%define dist Class-XSAccessor
Name: perl-%dist
Version: 1.19
Release: alt1.1.1.1.1

Summary: Generate fast XS accessors without runtime compilation
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/S/SM/SMUELLER/Class-XSAccessor-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel perl-threads

%description
Class::XSAccessor implements fast read, write and read/write accessors in XS.
Additionally, it can provide predicates such as "has_foo()" for testing
whether the attribute "foo" is defined in the object.
It only works with objects that are implemented as ordinary hashes.
Class::XSAccessor::Array implements the same interface for objects
that use arrays for their internal representation.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Class/XSAccessor*
%perl_vendor_autolib/Class/XSAccessor

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1.1
- rebuild with new perl 5.20.1

* Mon Nov 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.19-alt1
- automated CPAN update

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 1.18-alt2
- built for perl 5.18

* Fri Jul 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- automated CPAN update

* Thu Jun 13 2013 Vladimir Lettiev <crux@altlinux.ru> 1.16-alt1
- 1.14 -> 1.16

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 1.14-alt1
- 1.12 -> 1.14
- built for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.12-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1
- automated CPAN update

* Fri Feb 25 2011 Vladimir Lettiev <crux@altlinux.ru> 1.11-alt2
- fixed build

* Mon Dec 27 2010 Alexey Tourbin <at@altlinux.ru> 1.11-alt1
- 1.05 -> 1.11

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.05-alt1.1
- rebuilt with perl 5.12

* Sun Jan 31 2010 Vladimir Lettiev <crux@altlinux.ru> 1.05-alt1
- NMU: New version 1.05

* Thu Oct 22 2009 Michael Bochkaryov <misha@altlinux.ru> 1.03-alt1
- initial build for ALT Linux Sisyphus
