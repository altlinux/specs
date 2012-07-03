%define dist Compress-LZF
Name: perl-%dist
Version: 3.43
Release: alt1.2

Summary: Extremely light-weight Lempel-Ziv-Free compression
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

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
