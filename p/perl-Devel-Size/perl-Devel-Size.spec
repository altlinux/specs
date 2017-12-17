%define _unpackaged_files_terminate_build 1
%define dist Devel-Size
Name: perl-%dist
Version: 0.81
Release: alt1.1

Summary: Perl extension for finding the memory usage of Perl variables
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/N/NW/NWCLARK/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
This module figures out the real size of Perl variables in bytes, as
accurately as possible.

Call functions with a reference to the variable you want the size of.
If the variable is a plain scalar it returns the size of this scalar.
If the variable is a hash or an array, use a reference when calling.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc CHANGES README
%perl_vendor_archlib/Devel
%perl_vendor_autolib/Devel

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.81-alt1.1
- rebuild with new perl 5.26.1

* Wed Aug 30 2017 Igor Vlasenko <viy@altlinux.ru> 0.81-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.80-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.80-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.80-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.79-alt3.1
- rebuild with new perl 5.20.1

* Fri Dec 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.79-alt3
- added RT patches
- perl 5.20 ready

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.79-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.79-alt1
- automated CPAN update

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.78-alt1
- 0.77 -> 0.78
- built for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.77-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.77-alt1
- automated CPAN update

* Thu Nov 04 2010 Vladimir Lettiev <crux@altlinux.ru> 0.71-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.71-alt1
- automated CPAN update

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.69-alt1.1
- NMU for unknown reason

* Sun Jul 20 2008 Michael Bochkaryov <misha@altlinux.ru> 0.69-alt1
- first build for ALT Linux Sisyphus

