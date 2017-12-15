%define _unpackaged_files_terminate_build 1
%define dist Compress-LZF
Name: perl-%dist
Version: 3.8
Release: alt1.1.1.1
Epoch: 1

Summary: Extremely light-weight Lempel-Ziv-Free compression
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/ML/MLEHMANN/Compress-LZF-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-devel

%description
LZF is an extremely fast (not that much slower than a pure memcpy)
compression algorithm. It is ideal for applications where you want to save
*some* space but not at the cost of speed. It is ideal for repetitive
data as well. The module is self-contained and very small (no large
library to be pulled in). It is also free, so there should be no problems
incorporating this module into commercial programs.

I have no idea wether any patents in any countries apply to this
algorithm, but at the moment it is believed that it is free from any
patents.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README 
%perl_vendor_archlib/Compress
%perl_vendor_autolib/Compress

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.8-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1:3.8-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1:3.8-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1:3.8-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.7-alt1.1
- rebuild with new perl 5.20.1

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 1:3.7-alt1
- 3.43 -> 3.7

* Tue Aug 28 2012 Vladimir Lettiev <crux@altlinux.ru> 3.43-alt2
- rebuilt for perl-5.16

* Thu Oct 06 2011 Alexey Tourbin <at@altlinux.ru> 3.43-alt1.2
- rebuilt for perl-5.14

* Mon Oct 04 2010 Alexey Tourbin <at@altlinux.ru> 3.43-alt1.1
- rebuilt for perl-5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 3.43-alt1
- automated CPAN update

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 3.11-alt1.1
- NMU for unknown reason

* Tue Jul 22 2008 Michael Bochkaryov <misha@altlinux.ru> 3.11-alt1
- first build for ALT Linux Sisyphus
