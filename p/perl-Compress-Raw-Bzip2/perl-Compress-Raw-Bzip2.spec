%define dist Compress-Raw-Bzip2
Name: perl-%dist
Version: 2.048
Release: alt1

Summary: Low-level interface to the bzip2 compression library
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Mon Feb 20 2012
BuildRequires: bzlib-devel perl-Test-NoWarnings perl-Test-Pod

%description
The Compress::Raw::Bzip2 module provides Perl interface to the in-memory
compression/uncompression functions from the bzip2 compression library.

%prep
%setup -q -n %dist-%version
rm -rv bzip2-src/
rm -rv t/Test/

# disable build dependency on IO-Compress
sed -i- 's/^BEGIN$/if (0)/' t/compress/CompTestUtils.pm

%build
export BUILD_BZIP2=0 BZIP2_INCLUDE=%_includedir BZIP2_LIB=%_libdir
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Compress
%perl_vendor_autolib/Compress

%changelog
* Mon Feb 20 2012 Alexey Tourbin <at@altlinux.ru> 2.048-alt1
- 2.037 -> 2.048

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 2.037-alt2
- rebuilt for perl-5.14

* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 2.037-alt1
- 2.033 -> 2.037
- rebuilt as plain src.rpm

* Fri Feb 11 2011 Alexey Tourbin <at@altlinux.ru> 2.033-alt1
- 2.030 -> 2.033

* Mon Sep 20 2010 Alexey Tourbin <at@altlinux.ru> 2.030-alt1.1
- rebuilt for perl-5.12

* Thu Aug 05 2010 Alexey Tourbin <at@altlinux.ru> 2.030-alt1
- 2.027 -> 2.030

* Tue May 04 2010 Alexey Tourbin <at@altlinux.ru> 2.027-alt1
- 2.025 -> 2.027

* Sun Apr 04 2010 Alexey Tourbin <at@altlinux.ru> 2.025-alt1
- 2.021 -> 2.025

* Wed Sep 16 2009 Alexey Tourbin <at@altlinux.ru> 2.021-alt1
- 2.020 -> 2.021

* Tue Jun 16 2009 Alexey Tourbin <at@altlinux.ru> 2.020-alt1
- 2.017 -> 2.020

* Wed Apr 08 2009 Alexey Tourbin <at@altlinux.ru> 2.017-alt1
- 2.011 -> 2.017

* Thu Jun 12 2008 Alexey Tourbin <at@altlinux.ru> 2.011-alt1
- initial revision
