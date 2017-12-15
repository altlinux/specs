%define dist Bit-Vector
Name: perl-%dist
Version: 7.4
Release: alt1.1.1.1.1

Summary: Efficient bit vector, set of integers and "big int" math library
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/S/ST/STBEY/Bit-Vector-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Carp-Clan perl-devel

%description
Bit::Vector is an efficient C library which allows you to handle
bit vectors, sets (of integers), "big integer arithmetic" and
boolean matrices, all of arbitrary sizes.

The library is efficient (in terms of algorithmical complexity)
and therefore fast (in terms of execution speed) for instance
through the widespread use of divide-and-conquer algorithms.

The package also includes an object-oriented Perl module for
accessing the C library from Perl, and optionally features
overloaded operators for maximum ease of use.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	CHANGES.txt CREDITS.txt README.txt examples/
%dir	%perl_vendor_archlib/Bit
	%perl_vendor_archlib/Bit/Vector.pm
%doc	%perl_vendor_archlib/Bit/Vector.pod
%dir	%perl_vendor_archlib/Bit/Vector
	%perl_vendor_archlib/Bit/Vector/*.pm
%doc	%perl_vendor_archlib/Bit/Vector/*.pod
%dir	%perl_vendor_autolib/Bit
	%perl_vendor_autolib/Bit/Vector

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 7.4-alt1.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 7.4-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 7.4-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 7.4-alt1.1
- rebuild with new perl 5.20.1

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 7.4-alt1
- automated CPAN update

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 7.3-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 7.3-alt1
- automated CPAN update

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 7.2-alt1
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 7.1-alt3
- rebuilt for perl-5.14

* Tue Oct 04 2011 Alexey Tourbin <at@altlinux.ru> 7.1-alt2
- rebuilt as plain src.rpm

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 7.1-alt1.1
- rebuilt for perl-5.12

* Tue Oct 20 2009 Alexey Tourbin <at@altlinux.ru> 7.1-alt1
- 7.0 -> 7.1

* Fri Aug 28 2009 Alexey Tourbin <at@altlinux.ru> 7.0-alt1
- 6.6 -> 7.0

* Mon Aug 03 2009 Alexey Tourbin <at@altlinux.ru> 6.6-alt1
- 6.4 -> 6.6

* Mon Apr 13 2009 Alexey Tourbin <at@altlinux.ru> 6.4-alt2
- rebuild

* Mon Oct 16 2006 Alexey Tourbin <at@altlinux.ru> 6.4-alt1
- 6.3 -> 6.4
- imported sources into git and built with gear
- use -fvisibility=hidden to hide underlying C library symbols
- use PERL_NO_GET_CONTEXT for some marginal performance gain
- for the same reason, use XSLoader instead of DynaLoader

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 6.3-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Nov 04 2002 Stanislav Ievlev <inger@altlinux.ru> 6.3-alt2
- rebuild with new perl

* Mon Sep 30 2002 Igor Homyakov <homyakov at altlinux dot ru> 6.3-alt1
- 6.3 

* Tue Sep 17 2002 Igor Homyakov <homyakov at altlinux dot ru> 6.2-alt1
- 6.2-alt1 
- cleanup spec file

* Wed Nov 14 2001 Igor Homyakov <homyakov@altlinux.ru> alt1 
- Build package for ALTLinux 
